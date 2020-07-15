
"""
Functions for pushing, pulling, and creating Library files
"""
import code
import json
import logging
import os

from paths import (
    create_named_path,
    create_operation_path,
    create_library_path,
    makedirectory
)
from definition import (
    write_library_definition_json
)


def create_library_path(category_path, library_name):
    """
    Create a path for a library within the directory for a category.

    Note: does not create the directory.

    Arguments:
      category_path (string): the path for the category
      library_name (string): the name of the library

    Returns:
      string: the path of the library
    """
    return create_named_path(
        os.path.join(category_path, 'libraries'),
        library_name
    )


def get_library(aq, path, category, library):
    """
    Retrieves a single Library Object

    Arguments:
        aq (Session Object): Aquarium session object
        path (String): the path to where the file will be written
        category (String): The category the Library is in
        library (String): The Library to be retrieved
    """
    retrieved_library = aq.Library.where(
        {
            "category": category,
            "name": library
        }
    )
    if not retrieved_library:
        logging.warning(
            "No Library named {} in Category {}".format(
                library, category)
        )
        return
    write_files(path, retrieved_library[0])


def get_code_file_names():
    return ['source']


def write_files(path, library):
    """
    Writes the files for the library to the path.

    Arguments:
      path (string): the path of the file to write
      library (Library): the library whose definition will be written
    """
    logging.info("writing library {}".format(library.name))

    category_path = create_named_path(path, library.category)
    makedirectory(category_path)
    library_path = create_library_path(category_path, library.name)
    makedirectory(library_path)

    code_object = library.code("source")
    if not code_object:
        logging.warning(
            "Ignored library {} missing library code".format(
                library.name)
        )
    file_name = 'source.rb'
    try:
        code.write(library_path, file_name, code_object)
    except OSError as error:
        logging.warning("Error {} writing file {} for library {}".format(
            error, file_name, library.name))
    except UnicodeError as error:
        logging.warning(
            "Encoding error {} writing file {} for library {}".format(
                error, file_name, library.name))

    write_library_definition_json(os.path.join(
        library_path, 'definition.json'), library)


def select_library(aq, category_path, library_name):
    """
    Locates the library to be pushed

    Arguments:
        aq (Session Object): Aquarium session object
        category_path (String): the path to the category containing the library
        library (string): the Library containing the files to be pushed
    """

    path = create_library_path(category_path, library_name)
    push(aq, path, ['source'])


# def create(aq, path, category, library):
#    """
#    Creates new library on the Aquarium instance.
#    Note: does not create the files locally, they need to be pulled.
#
#    Arguments:
#        aq (Session Object): Aquarium session object
#        path (String): the directory path where the new files will be written
#        category (String): the category for the operation type
#        library (String): name of the library to be created
#    """
#    code_objects = create_code_objects(aq, library_code_names())
#    new_library = aq.Library.new(
#        name=operation_type_name,
#        category=category,
#    aq.utils.create_operation_type(new_operation_type)
#

def push(aq, directory_path, component_names):
    """
    Pushes files to the Aquarium instance

    Arguments:
        aq (Session Object): Aquarium session object
        directory_path (String): Directory where files are to be found
        component_names (List): List of files to push
    """
    with open(os.path.join(directory_path, 'definition.json')) as f:
        definitions = json.load(f)

    user_id = aq.User.where({"login": aq.login})
    query = {
        "category": definitions['category'],
        "name": definitions['name']
    }
    if definitions['parent_class'] == 'Library':
        parent_object = aq.Library.where(query)
        parent_type_name = 'library'
    elif definitions['parent_class'] == 'OperationType':
        parent_object = aq.OperationType.where(query)
        parent_type_name = 'operation type'

    if not parent_object:
        logging.warning(
            "No {} {}/{} on {}".format(
                parent_type_name,
                definitions['category'],
                definitions['name'],
                # TODO: make the following specific to user instance
                "Aquarium instance"
            )
        )
        return

    for name in component_names:
        read_file = code.read(path=directory_path, name=name)
        if read_file is None:
            return

        new_code = aq.Code.new(
            name=name,
            parent_id=parent_object[0].id,
            parent_class=definitions['parent_class'],
            user_id=user_id,
            content=read_file
        )

        logging.info("writing file {}".format(parent_object[0].name))

        aq.utils.update_code(new_code)


def run_test(*, session, path, name):
    logging.error("Library tests are not currently available")

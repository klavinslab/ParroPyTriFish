"""
Utilities for operation types.
"""
# e.g. pulling one library -> call get_library or pull_library function -- or call a general get function with library or op type as an argument?
# in that function, make new, then go through the methods?
class OperationType():
    # Operation Type has a category and a name
    def get(aq, path, category, operation_type): # get form database 
        #operation_type = aq.OperationType.where("category": category, "name": operation_type})
        pass

    def write_code_objects(): # write operation type to file
        pass

    def write_json(): # write json data to file 
        pass 

    def create(): # create new ot
        pass

    def select(): # ot to push 
        pass

    def create_code_objects(): # create files 
        pass

#library = Library()
#library.get()
#library.write()
#library.write_json()

class Library():
    # library has a category and a name
    # Library has source.rb and a json file
    # write_library -- currently does a bunch of directory/path stuff
    # Find in Database  
    def get(aq, path, category, library):
       # library = Library aq.Library.where("category": category, "name": library})
        pass

    def write_code_object(): # Write source.rb
        file_name = "source.rb" # For libraries this will be the only file name 
        code_object = self.code("source")
        file_path = os.path.join(path, file_name)
        with open(file_path, 'w') as file:
            file.write(code_object.content)

    def write_json():
        pass

    def select(): # Find library to push
        pass 

    def create(): # Create library
        pass

    def create_code_objects(): # code with name=source in db  
        pass


# Category has operations_types and/or libraries 
class Category():
    pass


# get a category 
#    operation_types = aq.OperationType.where({"category": category})
#    libraries = aq.Library.where({"category": category})
#    pull(path, operation_types=operation_types, libraries=libraries)

# Get all -- everything in Aquarium Instance
# All has category or categories 
# Operation_types = aq.OperationType.all()
    # libraries = aq.Library.all()
    # pull(path, operation_types, libraries)

# pull calls write optype and write library 
# these write each associate filed (for library this is just source, for ot its the list)
# then the write functions call write json 
# Default should be just the protocol 
class AbstractEntity():
    #what code does the get functions have in common?
    #right now things are broken up by push/pull/create, but we want them broken up by library vs optype
    # Pulling: get functions (get from db), write functions (write to disk)
    # Pushing: find (select) files from disk, create code objects, push code objects 
    # Create: create op type, create code objects, push
    pass


# Not part of a class? But make one function that calls all the make directory stuff 
def create_file_structure(path, entity_type):
    category_path = create_named_path(path, entity_type.category)
    makedirectory(category_path)
    path = create_named_path(
            os.path.join(category_path, 'operation types' or 'libraries'
            ), entity_type.name)
    makedirectory(path)


def operation_type_code_names():
    return ['protocol', 'precondition', 'cost_model', 'documentation', 'test']

"""
Utilities for operation types.
"""

class AbstractEntity():
    #what code does the get functions have in common?
    # Pulling: get functions (get from db), write functions (write to disk)
    # Pushing: find (select) files from disk, create code objects, push code objects 
    # Create: create op type, create code objects, push
    def create_path():
        category_path = create_named_path(path, entity_type.category)
        makedirectory(category_path)
        # this should be overridden to make correct path -- library or ot
        path = create_named_path(
                os.path.join(category_path, 'operation types' or 'libraries'
                ), entity_type.name)

    def get():
        pass 

    def pull():
        pass

    def get_code_file_names():
        pass

    def write_code_objects():
        pass

    def write_json_defintion():
        pass

    def create(): # create new ot
        pass

    def select(): # ot to push 
        pass

    def create_code_objects(): # create files to push 
        pass

    def push():
        pass
        #push files


class OperationType(AbstractEntity):
    # Operation Type has a category and a name
    def create_path(): # specifics for OT path
        pass
    
    def get(aq, path, category, operation_type): # get from database 
        # am I just making a double of what's happening in Trident?
        #operation_type = aq.OperationType.where("category": category, "name": operation_type})
        pass

    def pull():
        pass # calls write code objects and write json 


    def get_code_file_names(): # get all the files to write -- default should be protocol
        return ['protocol', 'precondition', 'cost_model', 'documentation', 'test']

    def write_code_objects(): # write operation types to disk 
        file_path = os.path.join(path, file_name)
        with open(file_path, 'w') as file:
            file.write(code_object.content)

    def write_json_defintion(): # write json data to file 
        pass 

    def create(): # create new ot
        pass

    def select(): # ot to push 
        pass

    def create_code_objects(): # create files to push 
        pass

    def push():
        pass
        #push files

    #ot_ser = {}
    #ot_ser["id"] = operation_type.id
    #ot_ser["name"] = operation_type.name
    #ot_ser["parent_class"] = "OperationType"
    #ot_ser["category"] = operation_type.category
    #ot_ser["inputs"] = field_type_list(operation_type.field_types, 'input')
    #ot_ser["outputs"] = field_type_list(operation_type.field_types, 'output')
    #ot_ser["on_the_fly"] = operation_type.on_the_fly
    #ot_ser["user_id"] = operation_type.protocol.user_id

    #with open(file_path, 'w') as file:
    #    file.write(json.dumps(ot_ser, indent=2))

class Library(AbstractEntity):
    
    def create_path():
        # dirname/catname/libraries/library_name
        pass
    
    def get(aq, path, category, library):
       # library = Library aq.Library.where("category": category, "name": library})
        pass

    def pull():
        pass

    def get_code_file_names():
        return ['source']

    def write_code_objects(): # Write source.rb
        file_name = "source.rb" # For libraries this will be the only file name 
        code_object = self.code("source")
        file_path = os.path.join(path, file_name)
        with open(file_path, 'w') as file:
            file.write(code_object.content)

    def write_json_defintion():
        pass

    def create(): # Create library
        pass

    def select(): # Find library to push
        pass 

    def create_code_objects(): # code with name=source in db  
        pass
    
    def push():
        pass


class Category():
#   Has operation types and libraries 
#    operation_types = aq.OperationType.where({"category": category})
#    libraries = aq.Library.where({"category": category})
#    pull(path, operation_types=operation_types, libraries=libraries)
    def get():
        pass

class All():
    # All has category or categories 
    def get_all():
        # retrieve all op types and libraries
        operation_types = aq.OperationType.all()
        libraries = aq.Library.all()

        for operation_type in operation_types:
            operation_type = OperationType()
            operation_type.pull()
        # make OpType instance, call write on that instance
        # but how does my optype differ from trident op type?
        # Should I be pulling out just the relevant info that we want -- the code objects?

        for library in libraries:
            # make Library instance, call write on that instance
            library = Library()
            library.pull() 


def create_file_structure(path, entity_type):
    category_path = create_named_path(path, entity_type.category)
    makedirectory(category_path)
    path = create_named_path(
            os.path.join(category_path, 'operation types' or 'libraries'
            ), entity_type.name)
    makedirectory(path)

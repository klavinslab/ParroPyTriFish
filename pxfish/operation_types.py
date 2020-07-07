"""
Utilities for operation types.
"""

class AbstractEntity():
    # what code does the get functions have in common?
    # Pulling: get functions (get from db), write functions (write to disk)
    # Pushing: find (select) files from disk, create code objects, push code objects 
    # Create: create op type, create code objects, push
    def __init__(self, aq, path, category, name):
       self.aq = aq
       self.path = path
       self.category = category
       self.name = name

    def create_category_path(path): # path is the directory path ~/arg.dirname created in script specifics for OT path
        category_path = os.path.join(path, simplename(category_name))  # name here is the simple name cat_ot 
        makedirectory(category_path)
        
    def create_path():
        category_path = create_category_path()
        makedirectory(category_path)
        path = os.path.join(
                os.path.join(category_path, 'operation types' or 'libraries'
                ), entity_type.name)
    
    def simplename(name):
        return re.sub(r'\W|^(?=\d)', '_', name).lower()

    def makedirectory(directory_name):
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)
    
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

class OperationType(AbstractEntity):
    # CreateNamedPath returns os.path.join(path, simplename(name)) first for simplename(cat), then simplename(ot)
    def __init__(self, aq, path, category, name):
        super().__init__(aq, path, category, name)
        self.classification = "operation_type"

    def create_named_path()
        path = os.path.join(category_path, 'operation_types')
        op_type_path = os.path.join(path, operation_type_name) 
        makedirectory(op_type_path)

    def get(aq, path, category, operation_type): # get from database 
        # operation_type = aq.OperationType.where("category": category, "name": operation_type})
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
   
    def __init__(self, aq, path, category, name):
        super().__init__(aq, path, category, name)
        self.grouping = "libraries"
    
    def create_named_path()
        # dirname/catname/libraries/library_name
        path = os.path.join(category_path, 'libraries')
        library_path = os.path.join(path, self.name) 
        makedirectory(library_path)
    
    def get():
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
# Get everything in a category -- create instances of each and add to set, call write -- or whatever the function is  
    # Or maybe I don't need the sets here -- because it's just writing the files
    def __init__(self, name):
        self.name = name
        self.operation_types = []
        self.libraries = []
#    pull(path, operation_types=operation_types, libraries=libraries)
    def get():
        operation_types = aq.OperationType.where({"category": category})
        libraries = aq.Library.where({"category": category})
    # for ot in op_type, ot = OperationType() -- pull what's needed ot.pull() 


class Directory():
    # Directory has category or categories, categories have ots and libraries, ots and libraries have code objects
    def get_all():
        # retrieve all op types and libraries
        operation_types = aq.OperationType.all()
        libraries = aq.Library.all()

        for operation_type in operation_types:
            operation_type = OperationType()
            operation_type.pull()
        # make OpType instance, call write on that instance
        # Should I be pulling out just the relevant info that we want -- the code objects?

        for library in libraries:
            # make Library instance, call write on that instance
            library = Library()
            library.pull() 


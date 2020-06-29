"""
Utilities for operation types.
"""

class OperationType():
    # Operation Type has a category and a name
    # Get OperationType aq.OperationType.where("category": category, "name": operation_type})
    # OpType has files associated -- protocol.rb etc. and a json file
    # returns a single operation type instance 
    pass

class Library():
    # library has a category and a name
    # Library has source.rb and a json file
    # returns a single library instance 
    def get(aq, path, category, library #as in library name):
        library = Library aq.Library.where("category": category, "name": library})

    def pull():
        # for each library you want to retrieve -- so you're making an instance for each one you want to retrieve then calling pull/write?
        write_library(path, library)
        # write_code and write library json file 

# Category has operations_types and/or libraries 

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
    what code does the get functions have in common?
    right now things are broken up by push/pull/create, but we want them broken up by library vs optype
    # Pulling: get functions (get from db), write functions (write to disk)
    # Pushing: find (select) files from disk, create code objects, push code objects 
    # Create: create op type, create code objects, push
    pass

def operation_type_code_names():
    return ['protocol', 'precondition', 'cost_model', 'documentation', 'test']

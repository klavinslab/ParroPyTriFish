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
    # Get Library aq.Library.where("category": category, "name": library})
    # Library has source.rb and a json file
    # returns a single library instance 
    pass

# class Category():
# Category has operations_types and/or libraries 
# get a category 
#    operation_types = aq.OperationType.where({"category": category})
#    libraries = aq.Library.where({"category": category})
#    pull(path, operation_types=operation_types, libraries=libraries)

# get all -- everything in Aquarium Instance
# all has category or categories 
#     operation_types = aq.OperationType.all()
    # libraries = aq.Library.all()
    # pull(path, operation_types, libraries)

# pull calls write optype and write library 
# these write each associate filed (for library this is just source, for ot its the list)
# then the write functions call write json 
# Default should be just the protocol 
class AbstractEntity():
    # def get_entity():
    # get a library or an op type 
    pass

def operation_type_code_names():
    return ['protocol', 'precondition', 'cost_model', 'documentation', 'test']

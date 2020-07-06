from pxfish.operation_types import OperationType, Category, Library

# Can instantiate OperationType
def test_creates_optype_instance():
    op_type = OperationType()
    assert type(op_type) is OperationType

def test_creates_library_instance():
    library = Library()
    assert type(library) is Library

def test_creates_category():
    category = Category()
    assert type(category) is Category

def test_creates_directory():
    pass

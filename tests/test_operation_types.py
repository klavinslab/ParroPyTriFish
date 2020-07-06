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

def test_pulling_operation_type_creates_directory():
    """e.g. I want to test each part (it makes a directory, it writes the code files, but it will do all the steps each time)
    aha, that's what the fixtures are for I think"""
    path = os.path.normpath("test_name")
    directory_path = makedirectory(path)
    category = "category_name"
    operation_type = "operation_type_name"
    get_operation_type(aq, path, category, operation_type) 
    assert directory_path == ""

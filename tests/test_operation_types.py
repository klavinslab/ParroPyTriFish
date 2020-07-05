from pxfish.operation_types import OperationType 

# Can instantiate OperationType
# Test pytest!
def test_op_type_exists():
    op_type = OperationType()
    assert type(op_type) is OperationType



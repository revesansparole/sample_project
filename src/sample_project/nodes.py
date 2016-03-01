def int_cast(a=0):
    """Cast value to int type.

    __plugin__: node

    Args:
        a: (any) anything that valuate to an integer

    Returns:
        (int) integer value of parameter
    """
    ret = int(a)
    return ret


def plus(a=0, b=0):
    """Add two numbers together.

    __plugin__: node

    Args:
        a: (int) left operand
        b: (int) right operand

    Returns:
        (int) result of addition
    """
    ret = a + b
    return ret


def print_obj(x=None):
    """Print its parameter.

    __plugin__: node

    Args:
        x: (any) anything with a string representation

    Returns:
        (str) string representation of parameter
    """
    ret = str(x)
    print(ret)

    return ret


def read(url=""):
    """Read and return content of resource

    __plugin__: node

    Args:
        url: (url) path to resource

    Returns:
        (str) content of resource
    """
    with open(url, 'r') as f:
        cnt = f.read()

    return cnt

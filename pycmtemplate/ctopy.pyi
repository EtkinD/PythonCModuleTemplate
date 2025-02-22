"""
    Interface file for the C++ module. (pycmtemplate/ctopy.pyi)
    This file is used to define the interface of the C++ module.
    The interface file is used by the Python type checker to check the types of the C++ module.
"""

# Function definitions
def functionFromCPP() -> int: ...
def functionFromCPP2(a: int, b: int) -> int: ...

# Variable definitions
variableFromCPP: int
variableFromCPP2: str

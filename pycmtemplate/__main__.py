from . import ctopy

def main():
    print("Hello 'pycmtemplate' Module!")
    print("This is the main function of the module.")
    print("You can run this function by calling 'pycmtemplate' module.")
    print()
    print(ctopy.functionFromCPP())
    print(ctopy.functionFromCPP2(1, 2))
    print(ctopy.variableFromCPP)
    print(ctopy.variableFromCPP2)


if __name__ == '__main__':
    main()

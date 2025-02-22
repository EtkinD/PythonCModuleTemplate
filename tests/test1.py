import pycmtemplate_c


def run():
    print("Function calls")
    r1 = pycmtemplate_c.functionFromCPP()
    r2 = pycmtemplate_c.functionFromCPP2(3, 5)

    print("Print results")
    print(r1)
    print(r2)

    print("Print variables")
    print(pycmtemplate_c.variableFromCPP)
    print(pycmtemplate_c.variableFromCPP2)


if __name__ == "__main__":
    print("Running test1.py")
    run()

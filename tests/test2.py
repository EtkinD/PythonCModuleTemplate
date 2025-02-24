import pycmtemplate


def run():
    print("Function calls")
    r1 = pycmtemplate.functionFromCPP()
    r2 = pycmtemplate.functionFromCPP2(3, 5)

    print("Print results")
    print(r1)
    print(r2)

    print("Print variables")
    print(pycmtemplate.variableFromCPP)
    print(pycmtemplate.variableFromCPP2)


if __name__ == "__main__":
    print("Running test2.py")
    run()

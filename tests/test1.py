import pycmtemplate_c

print("Function calls")
r1 = pycmtemplate_c.functionFromCPP()
r2 = pycmtemplate_c.functionFromCPP2(3, 5)

print("Print results")
print(r1)
print(r2)

print("Print variables")
print(pycmtemplate_c.variableFromCPP)
print(pycmtemplate_c.variableFromCPP2)

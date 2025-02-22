
import tests.test1 as test1
import tests.test2 as test2

print("Running test1.py - Runs directly from C++ extension")
test1.run()

print('\n+-------------------------------------------+\n')

print("Running test2.py - Runs from Python extension")
test2.run()


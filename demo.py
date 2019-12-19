from coderunner import coderunner
import pprint

source_code = "testfiles/" + "test_python_input.py"
language = "Python"
output = "testfiles/output/" + "output2.txt"
Input = "testfiles/input/" + "input.txt"
r = coderunner.code(source_code, language, output, Input)

# run the code
r.run()

print("Status : " + r.getStatus())

# check if any error occured
if r.getError() is not None:
    pprint.pprint("Error : " + r.getError())
else:
    print("Standard Output : ")
    pprint.pprint(r.getOutput())
print("Execution Time : " + r.getTime())
print("Memory : " + str(r.getMemory()))

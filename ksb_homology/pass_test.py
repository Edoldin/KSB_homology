import sys, os, glob

print("------------------------------------- ")
print("Running all test:")
for test in glob.glob("**/test/*.py", recursive=True):
    print("    Running test: "+test)
    exec(open(test).read())
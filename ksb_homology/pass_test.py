import sys, os, glob

for test in glob.glob("./*/test/*.py"):
    print("Running test: "+test)
    exec(open(test).read())
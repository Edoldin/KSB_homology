import sys, os, glob

print("------------------------------------- ")
print("Running all test:")
for test in glob.glob("**/test*.py", recursive=True):
    print("    Running test: "+test)
    try:
        exec(open(test).read())
    except:
        print("###########  "+test+" failed ###########")
        continue
    print("###########  "+test+" finished ###########")

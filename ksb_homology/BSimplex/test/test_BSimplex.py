from BSimplex import BSimplex

print("-------------BSimplex test-------------")
a=BSimplex((1,2,4))
a.set_partial((1,2),2,6)
assert a.get_partial((1,2),2) == 6, "Should be 6"
assert a.get_partial((2,1),2) == False, "default value to False"
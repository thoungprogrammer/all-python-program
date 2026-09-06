# Just making a program to swap the variable value with the help of third variable 

glass1 = "milk"
glass2 = "juice"
print("=== Before Swap ===")
print("Glass 1 = " + glass1)
print("Glass 2 = " + glass2)
print("\n=== After Swap ===")
temp = glass2
glass2 = glass1
glass1 = temp
print("Glass 1 = " + glass1)
print("Glass 2 = " + glass2)
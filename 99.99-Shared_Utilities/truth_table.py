# Assigning boolean values to variables
A = True
B = False

# ---------------------------------------------------------
# 1. The AND Operator ('and')
# Rule: Only results in True if BOTH sides are True.
# ---------------------------------------------------------
print("--- Truth Table for AND ---")
print("True and True   =", A and A)
print("True and False  =", A and B)
print("False and True  =", B and A)
print("False and False =", B and B)
print() # Adds a blank line for readability

# ---------------------------------------------------------
# 2. The OR Operator ('or')
# Rule: Results in True if AT LEAST ONE side is True.
# ---------------------------------------------------------
print("--- Truth Table for OR ---")
print("True or True    =", A or A)
print("True or False   =", A or B)
print("False or True   =", B or A)
print("False or False  =", B or B)
print() 

# ---------------------------------------------------------
# 3. The NOT Operator ('not')
# Rule: Simply flips the value to the opposite.
# ---------------------------------------------------------
print("--- Truth Table for NOT ---")
print("not True        =", not A)
print("not False       =", not B)
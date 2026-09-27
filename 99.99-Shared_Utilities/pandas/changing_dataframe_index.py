"""
=============================================================================
Changing Index in a DataFrame
=============================================================================
Demonstrates various methods to set, modify, name, and reset row indices 
in a Pandas DataFrame.
"""

import pandas as pd

# Initial Data Setup
data = {
    'ID': [101, 102, 103],
    'Name': ['Aarav', 'Sneha', 'Raj'],
    'Age': [25, 28, 22]
}


# -------------------------------------------------------------------
# Method 1: Set index DURING DataFrame creation
# -------------------------------------------------------------------
df = pd.DataFrame(data, index=['Emp_A', 'Emp_B', 'Emp_C'])

print("1. Set index during creation:")
print(df)
# Output:
#         ID   Name  Age
# Emp_A  101  Aarav   25
# Emp_B  102  Sneha   28
# Emp_C  103    Raj   22
print("\n" + "=" * 50 + "\n")


# -------------------------------------------------------------------
# Method 2: Modify df.index DIRECTLY on an existing DataFrame
# -------------------------------------------------------------------
df.index = ['Row_1', 'Row_2', 'Row_3']

print("2. Direct index reassignment:")
print(df)
# Output:
#         ID   Name  Age
# Row_1  101  Aarav   25
# Row_2  102  Sneha   28
# Row_3  103    Raj   22
print("\n" + "=" * 50 + "\n")


# -------------------------------------------------------------------
# Method 3: Promote an existing column to index using set_index()
# -------------------------------------------------------------------
df = df.set_index('ID')

print("3. Promote 'ID' column to index:")
print(df)
# Output:
#       Name  Age
# ID             
# 101  Aarav   25
# 102  Sneha   28
# 103    Raj   22
print("\n" + "=" * 50 + "\n")


# -------------------------------------------------------------------
# Method 4: Assign a descriptive NAME to the index axis
# -------------------------------------------------------------------
df.index.name = 'Employee_ID'

print("4. Set name for the index axis:")
print(df)
# Output:
#               Name  Age
# Employee_ID            
# 101          Aarav   25
# 102          Sneha   28
# 103            Raj   22
print("\n" + "=" * 50 + "\n")


# -------------------------------------------------------------------
# Method 5: Reset index by CONVERTING the index back into a column
# -------------------------------------------------------------------
df = df.reset_index()

print("5. Reset index and convert 'Employee_ID' back to a column:")
print(df)
# Output:
#    Employee_ID   Name  Age
# 0          101  Aarav   25
# 1          102  Sneha   28
# 2          103    Raj   22
print("\n" + "=" * 50 + "\n")


# -------------------------------------------------------------------
# Method 6: Reset index by DROPPING the current index completely
# -------------------------------------------------------------------
# (First set the index to demonstrate discarding it)
df = df.set_index('Employee_ID')

df = df.reset_index(drop=True)

print("6. Reset index by DROPPING the index column:")
print(df)
# Output:
#     Name  Age
# 0  Aarav   25
# 1  Sneha   28
# 2    Raj   22
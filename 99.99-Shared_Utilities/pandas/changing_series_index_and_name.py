"""
=============================================================================
Changing Index and Name in a Pandas Series
=============================================================================
In a 1D Pandas Series, the 'Series Name' functions as the column header,
while the 'Index' provides the row labels. Demonstrates how to manipulate both 
using .rename(), .name, .index, .index.str, .set_axis(), .rename_axis(), 
and .reset_index().
"""

import pandas as pd

# Initial Series with custom index and a Series name
s = pd.Series([25, 28, 22], index=['aarav', 'sneha', 'raj'], name='age')

print("Original Series:")
print(s)
# Output:
# aarav    25
# sneha    28
# raj      22
# Name: age, dtype: int64
print("\n" + "=" * 50 + "\n")


# -------------------------------------------------------------------
# Method 1: Change the Series Name ("column header" equivalent)
# (Useful to update what the data represents; using .rename() or .name)
# -------------------------------------------------------------------
s = s.rename('Age_Years')
# Alternatively: s.name = 'Age_Years'

print("1. Change Series Name using .rename():")
print(s)
# Output:
# aarav    25
# sneha    28
# raj      22
# Name: Age_Years, dtype: int64
print("\n" + "=" * 50 + "\n")


# -------------------------------------------------------------------
# Method 2: Rename SPECIFIC index labels using a dictionary with .rename()
# (Best when you only need to change a few row labels)
# -------------------------------------------------------------------
s = s.rename({'aarav': 'Aarav_K', 'sneha': 'Sneha_M'})

print("2. Rename specific index labels using .rename():")
print(s)
# Output:
# Aarav_K    25
# Sneha_M    28
# raj        22
# Name: Age_Years, dtype: int64
print("\n" + "=" * 50 + "\n")


# -------------------------------------------------------------------
# Method 3: Overwrite ALL index labels by assigning a new list to s.index
# (List length must match the exact length of the Series)
# -------------------------------------------------------------------
s.index = ['Emp_1', 'Emp_2', 'Emp_3']

print("3. Direct reassignment of s.index:")
print(s)
# Output:
# Emp_1    25
# Emp_2    28
# Emp_3    22
# Name: Age_Years, dtype: int64
print("\n" + "=" * 50 + "\n")


# -------------------------------------------------------------------
# Method 4: Clean/Transform index labels using .index.str methods
# (Essential for string manipulation like casing or replacing characters)
# -------------------------------------------------------------------
s.index = s.index.str.upper()

print("4. Convert index labels to uppercase using .index.str.upper():")
print(s)
# Output:
# EMP_1    25
# EMP_2    28
# EMP_3    22
# Name: Age_Years, dtype: int64
print("\n" + "=" * 50 + "\n")


# -------------------------------------------------------------------
# Method 5: Dynamic transformation of index labels using a lambda function
# -------------------------------------------------------------------
s = s.rename(lambda idx: f"ID_{idx}")

print("5. Rename index using a lambda function inside .rename():")
print(s)
# Output:
# ID_EMP_1    25
# ID_EMP_2    28
# ID_EMP_3    22
# Name: Age_Years, dtype: int64
print("\n" + "=" * 50 + "\n")


# -------------------------------------------------------------------
# Method 6: Change index labels using .set_axis()
# -------------------------------------------------------------------
s = s.set_axis(['A', 'B', 'C'], axis=0)

print("6. Replace index labels using .set_axis():")
print(s)
# Output:
# A    25
# B    28
# C    22
# Name: Age_Years, dtype: int64
print("\n" + "=" * 50 + "\n")


# -------------------------------------------------------------------
# Method 7: Assign a name to the Index Axis itself using .rename_axis()
# (Labels the index axis itself rather than changing row names)
# -------------------------------------------------------------------
s = s.rename_axis('Employee_Code')
# Alternatively: s.index.name = 'Employee_Code'

print("7. Add an Index Axis Name using .rename_axis():")
print(s)
# Output:
# Employee_Code
# A    25
# B    28
# C    22
# Name: Age_Years, dtype: int64
print("\n" + "=" * 50 + "\n")


# -------------------------------------------------------------------
# Method 8A: Reset index to convert Series into a DataFrame
# (Converts index values into an explicit column in a DataFrame)
# -------------------------------------------------------------------
df_from_s = s.reset_index()

print("8A. Reset index without drop (Converts Series -> DataFrame):")
print(df_from_s)
# Output:
#   Employee_Code  Age_Years
# 0             A         25
# 1             B         28
# 2             C         22
print("\n" + "=" * 50 + "\n")


# -------------------------------------------------------------------
# Method 8B: Reset index while DROPPING old labels (remains a Series)
# (Resets the Series back to standard 0, 1, 2... integer index)
# -------------------------------------------------------------------
s_reset = s.reset_index(drop=True)

print("8B. Reset index with drop=True (Restores default integer index):")
print(s_reset)
# Output:
# 0    25
# 1    28
# 2    22
# Name: Age_Years, dtype: int64
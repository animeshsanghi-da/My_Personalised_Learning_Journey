"""
=============================================================================
Changing Column Names in a DataFrame
=============================================================================
Demonstrates various methods to rename, clean, transform, and prefix column 
names in a Pandas DataFrame.
"""

import pandas as pd

# Initial DataFrame with messy column names
data = {
    'emp id': [101, 102, 103],
    'FIRST NAME': ['Aarav', 'Sneha', 'Raj'],
    'age_years': [25, 28, 22]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
# Output:
#    emp id FIRST NAME  age_years
# 0     101      Aarav         25
# 1     102      Sneha         28
# 2     103        Raj         22
print("\n" + "=" * 50 + "\n")


# -------------------------------------------------------------------
# Method 1: Rename SPECIFIC columns using a dictionary with .rename()
# (Best when you only need to change a few column names)
# -------------------------------------------------------------------
df = df.rename(columns={'emp id': 'Emp_ID', 'FIRST NAME': 'First_Name'})

print("1. Rename specific columns using .rename():")
print(df)
# Output:
#    Emp_ID First_Name  age_years
# 0     101      Aarav         25
# 1     102      Sneha         28
# 2     103        Raj         22
print("\n" + "=" * 50 + "\n")


# -------------------------------------------------------------------
# Method 2: Overwrite ALL column names by assigning a new list to df.columns
# (Requires the new list length to match the exact number of columns)
# -------------------------------------------------------------------
df.columns = ['ID', 'Name', 'Age']

print("2. Direct reassignment of df.columns:")
print(df)
# Output:
#     ID   Name  Age
# 0  101  Aarav   25
# 1  102  Sneha   28
# 2  103    Raj   22
print("\n" + "=" * 50 + "\n")


# -------------------------------------------------------------------
# Method 3: Clean/Transform column names using .columns.str methods
# (Essential in data cleaning pipelines for stripping spaces, lowercasing, etc.)
# -------------------------------------------------------------------
df.columns = df.columns.str.lower()

print("3. Convert column names to lowercase using .columns.str.lower():")
print(df)
# Output:
#     id   name  age
# 0  101  Aarav   25
# 1  102  Sneha   28
# 2  103    Raj   22
print("\n" + "=" * 50 + "\n")


# -------------------------------------------------------------------
# Method 4: Apply a function or lambda inside .rename()
# (Useful for dynamic transformations across all columns)
# -------------------------------------------------------------------
df = df.rename(columns=lambda col: col.upper())

print("4. Rename columns using a lambda function inside .rename():")
print(df)
# Output:
#     ID   NAME  AGE
# 0  101  Aarav   25
# 1  102  Sneha   28
# 2  103    Raj   22
print("\n" + "=" * 50 + "\n")


# -------------------------------------------------------------------
# Method 5: Rename columns using .set_axis()
# (An explicit method to replace column names along axis=1 or axis='columns')
# -------------------------------------------------------------------
df = df.set_axis(['Emp_ID', 'Emp_Name', 'Emp_Age'], axis=1)

print("5. Replace column names using .set_axis():")
print(df)
# Output:
#    Emp_ID Emp_Name  Emp_Age
# 0     101    Aarav       25
# 1     102    Sneha       28
# 2     103      Raj       22
print("\n" + "=" * 50 + "\n")


# -------------------------------------------------------------------
# Method 6: Add a prefix or suffix to all column names using .add_prefix() / .add_suffix()
# (Commonly used before joining/merging DataFrames to prevent collisions)
# -------------------------------------------------------------------
df = df.add_prefix('Data_')

print("6. Add a prefix to all column names using .add_prefix():")
print(df)
# Output:
#    Data_Emp_ID  Data_Emp_Name  Data_Emp_Age
# 0          101          Aarav            25
# 1          102          Sneha            28
# 2          103            Raj            22
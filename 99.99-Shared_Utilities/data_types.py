# 1. Numeric Types: Used for mathematical values.
#    1. int: Whole numbers of unlimited precision
print(10)       # INT: 10
#    2. float: Decimal or floating-point numbers
print(3.14)     # FLOAT: 3.14
#    3. complex: Numbers with real and imaginary parts
print(2+3j)     # COMPLEX: (2+3j)

# 2. Sequence Types: Ordered collections of items.
#    1. str: Textual data enclosed in quotes
print("Animesh")        # STR: Animesh
#    2. list: Mutable (changeable) ordered collections
print([])               # Empty list
print([1])              # List of a single item
print([1, 'a', True])   # List of multiple items
#    3. tuple: Immutable (unchangeable) ordered collections
print(())               # Empty tuple
print((1,))             # Single tuple (comma is required!)
print((1, 'a', True))   # Tuple of multiple items
#    4. range: Represents a sequence of numbers, commonly used in loops.
print(range(0, 5))      # RANGE

# 3. Mapping Type:
#    1. dict: Unordered collections of key-value pairs
print({})               # Empty DICT
print({1: 'a'})         # Single DICT (one key-value pair)
print({1: 'a', 2: 'b'}) # DICT of multiple values

# 4. Set Types: Unordered collections of unique items.
#    1. set: Mutable collection
print(set())            # Empty set
print({1})              # Single set
print({2, 'a', True})   # Set of multiple unique values (Note: 1 and True evaluate as duplicates in Sets)
#    2. frozenset: Immutable version of a set.
print(frozenset())               # Empty Frozenset
print(frozenset([1]))            # Single Frozenset
print(frozenset([2, 'a', True])) # Frozenset of multiple unique values

# 5. Boolean Type:
#    1. bool: Represents truth values, True or False.
print(True)     # BOOL: True
print(False)    # BOOL: False

# 6. Binary Types: For handling raw binary data.
# While bytes, bytearrays, and memoryview are essential low-level tools, modern data analysts primarily use Pandas and NumPy for their efficiency, ease of use, and specialized analytical features.
#    1. bytes: Immutable sequence of bytes.
print(b"Hello")             # BYTES
#    2. bytearray: Mutable sequence of bytes.
print(bytearray(b"Hello"))  # BYTEARRAY
#    3. memoryview: Allows accessing an object's internal data without copying.
print(memoryview(b"Hello")) # MEMORYVIEW

# 7. None Type:
#    1. NoneType: Represented by the constant None, indicating the absence of a value.
print(None)     # NoneType: None

# Key Concept:
#     1. Mutable types (list, dict, set) can be changed after creation
#     2. Immutable types (int, float, str, tuple) cannot.
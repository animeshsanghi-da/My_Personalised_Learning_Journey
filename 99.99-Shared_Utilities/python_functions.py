import asyncio

def heading(text):
    print(f"\n{'='*30}\n{text}\n{'='*30}")

"""
The 71 Python 3.13 Built-in Functions: A Data Scientist's Guide
Organized by functional category for readability.
"""

# ==========================================
# 1. DATA TYPES & CONVERSIONS (Crucial for Data Cleaning)
# ==========================================
heading("--- Types & Conversions ---")

# int([x]) / int(x, base=10)
# float([x])
# str(object='') / str(object=b'', encoding='utf-8', errors='strict')
# bool([x])
# complex([real[, imag]])
# DS TIP: Essential for casting columns (e.g., converting '1.5' to float).
x_int = int("42")
x_float = float("3.14")
x_str = str(42)
x_bool = bool(1)                # 1 is True, 0 is False
x_complex = complex(1, 2)       # Used in advanced signal processing (e.g., Fourier transforms)

# list([iterable])
# tuple([iterable])
# set([iterable])
# dict(**kwarg) / dict(mapping, **kwarg) / dict(iterable, **kwarg)
# DS TIP: The building blocks of data. Dictionaries are often used to map/replace values in pandas.
data_list = list((1, 2, 3))
data_tuple = tuple([1, 2, 3])   # Immutable, memory-efficient
data_set = set([1, 2, 2, 3])    # Fast O(1) lookups, great for finding unique items
data_dict = dict(a=1, b=2)

# frozenset([iterable])
# DS TIP: Like a set, but immutable. Useful if you need to use a set as a key in a dictionary (e.g., grouping combinations of features).
f_set = frozenset([1, 2, 3])

# bytes([source[, encoding[, errors]]])
# bytearray([source[, encoding[, errors]]])
# DS TIP: Used when handling raw image data, audio files, or serialized model files (Pickle).
raw_bytes = bytes([65, 66]) 
mut_bytes = bytearray([65, 66])

print_list = [x_int, x_float, x_str, x_bool, x_complex, data_list, data_tuple, data_set, data_dict, f_set, raw_bytes, mut_bytes]
for i in print_list:
    print(f"{i}")

# ==========================================
# 2. MATH & STATISTICS (Feature Engineering Basics)
# ==========================================
heading("--- Math & Stats ---")

# abs(x)
# round(number[, ndigits])
# sum(iterable, /, start=0)
# DS TIP: Used for calculating errors (MAE), rounding predictions, or aggregating totals.
print(abs(-15.5))       # 15.5
print(round(3.1415, 2)) # 3.14
print(sum([10, 20, 30]))# 60

# min(iterable, *[, key, default]) / min(arg1, arg2, *args[, key])
# max(iterable, *[, key, default]) / max(arg1, arg2, *args[, key])
# DS TIP: Vital for finding outliers, or implementing custom Min-Max scaling for machine learning.
print(min([1, 5, -2]))  # -2
print(max([1, 5, -2]))  # 5

# pow(base, exp[, mod])
# divmod(a, b)
# DS TIP: divmod is great for time-series math (e.g., converting total seconds into minutes and seconds).
print(pow(2, 3))        # 8      --> (2^3)
print(divmod(10, 3))    # (3, 1) --> 3 goes into 10 three times with a remainder of one

# ==========================================
# 3. ITERABLES & SEQUENCES (Data Processing)
# ==========================================
heading("--- Iterables & Sequences ---")

# all(iterable)
# any(iterable)
# DS TIP: Perfect for data quality checks. all() checks if there are no missing/zero values; any() checks if at least one condition triggered.
print(all([True, True, True]))   # True
print(any([False, True, False])) # True

# len(s)
# range(stop) / range(start, stop[, step])
# reversed(seq)
# sorted(iterable, /, *, key=None, reverse=False)
# DS TIP: sorted() is heavily used to rank data before creating ordinal features.
print(len(data_list))          # 3
print(list(range(0, 5, 2)))    # [0, 2, 4]
print(list(reversed([1, 3])))  # [3, 1]
print(sorted([3, 1, 2]))       # [1, 2, 3]

# enumerate(iterable, start=0)
# zip(*iterables, strict=False)
# DS TIP: zip() is the best way to combine two lists (e.g., feature names and importances) into a dictionary.
print(list(enumerate(['a', 'b'])))          # [(0, 'a'), (1, 'b')]
print(list(zip(['age', 'hw'], [25, 180])))  # [('age', 25), ('hw', 180)]
print(tuple(zip(['age', 'hw'], [25, 180]))) # (('age', 25), ('hw', 180))
print(dict(zip(['age', 'hw'], [25, 180])))  # {'age': 25, 'hw': 180}

# filter(function, iterable)
# map(function, iterable, *iterables)
# DS TIP: Often replaced by list comprehensions or pandas .apply(), but memory efficient for massive text corpora.
print(list(filter(lambda x: x > 1, [1, 2, 3]))) # [2, 3]
print(list(map(lambda x: x**2, [1, 2, 3])))     # [1, 4, 9]

# iter(object[, sentinel])
# next(iterator[, default])
# These are designed to retrieve elements from a collection one by one
# DS TIP: Used when processing massive datasets (like chunks of a huge CSV) that don't fit into RAM.
my_iter = iter([10, 20, 30])
print(next(my_iter)) # 10
print(next(my_iter)) # 20  ... and so on

# slice(stop) / slice(start, stop[, step])
# DS TIP: Core to pandas `.iloc`. You can save a slice object to reuse the same crop on multiple arrays.
s = slice(0, 2)
print([10, 20, 30, 40][s]) # [10, 20]

# ==========================================
# 4. INSPECTION & VALIDATION (Pipeline Debugging)
# ==========================================
heading("--- Inspection & Validation ---")

# type(object) / type(name, bases, dict, **kwds)
# isinstance(object, classinfo)
# issubclass(class, classinfo)
# DS TIP: isinstance() is safer than type() == X for input validation in custom scikit-learn transformers.
print(type(42))                  # <class 'int'>
print(isinstance(42, int))       # True
print(issubclass(bool, int))     # True

# dir([object])
# vars([object])
# callable(object)
# hasattr(object, name)
# getattr(object, name[, default])
# setattr(object, name, value)
# delattr(object, name)
# DS TIP: getattr() is heavily used in building dynamic ML pipelines where the model type is passed as a string.
class Model:
    weights = [0.1, 0.5]
    def predict(self): pass

m = Model()
print(callable(m.predict))       # True (is it a function/method?)
print(hasattr(m, 'weights'))     # True
print(getattr(m, 'weights'))     # [0.1, 0.5]
setattr(m, 'bias', 0.5)          # Adds new attribute dynamically
delattr(m, 'bias')               # Removes it
# dir(m) shows all methods; vars(m) shows dictionary of attributes.

# id(object)
# hash(object)
# DS TIP: hash() is used internally by pandas/sets to find unique values rapidly.
print(id(m))      # Memory address
print(hash("ID_1")) # Integer representation of the string

# ==========================================
# 5. STRING & I/O (Reporting & Formatting)
# ==========================================
heading("--- Strings & I/O ---")

# print(*objects, sep=' ', end='\n', file=None, flush=False)
# input([prompt])
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# format(value[, format_spec])
# DS TIP: format() is great for standardizing logging outputs during model training.
# with open('data.csv', 'r') as f: pass # Standard file reading
# input("Enter value: ") # Pauses for user text
print(format(0.9567, '.2%')) # 95.67%

# repr(object)
# ascii(object)
# chr(i)
# ord(c)
# DS TIP: repr() is vital in error logs to show exact data types (e.g., '1' vs 1). chr/ord are used in NLP text cleaning.
print(repr("Data\n")) # "'Data\n'" (keeps escape chars visible)
print(ascii("ñ"))     # '\xf1'
print(chr(97))        # 'a'
print(ord('a'))       # 97

# bin(x)
# hex(x)
# oct(x)
# DS TIP: Rarely used in standard DS, but useful in network security analytics or low-level bitwise operations.
print(bin(10)) # 0b1010
print(hex(15)) # 0xf
print(oct(8))  # 0o10

# ==========================================
# 6. OBJECT-ORIENTED PROGRAMMING (Custom Models)
# ==========================================
heading("--- OOP Fundamentals ---")

# object()
# super([type[, object_or_type]])
# property(fget=None, fset=None, fdel=None, doc=None)
# classmethod(function)
# staticmethod(function)
# DS TIP: property() is great for caching heavy computations in a class (like a covariance matrix).
class Parent(object):
    def get_name(self): return "Base"

class Child(Parent):
    def __init__(self): self._score = 0
        
    def get_name(self): return super().get_name() + " Model"
    
    @property
    def score(self): return self._score # Getter
    
    @classmethod
    def from_csv(cls): pass # Alternative constructor
    
    @staticmethod
    def calc_rmse(y, y_pred): pass # Utility function, no 'self' needed

# help([object])
# DS TIP: Use this in Jupyter Notebooks to instantly see a function's parameters without going to Google.
# help(Child) 

# ==========================================
# 7. ADVANCED / SYSTEM / DYNAMIC EXECUTION
# ==========================================
heading("--- Advanced & System ---")

# globals()
# locals()
# DS TIP: Avoid using these in production, but they are useful for debugging namespace issues in messy Jupyter notebooks.
# print(locals().keys())

# eval(expression[, globals[, locals]])
# exec(object[, globals[, locals]])
# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
# DS TIP: DANGEROUS! eval() is sometimes (riskily) used to parse stringified arrays in CSVs (e.g., "[1, 2]"). Use ast.literal_eval instead!
code = compile("10 + 10", "<string>", "eval")
print(eval(code)) # 20
exec("x_exec = 50") # Executes statement

# memoryview(object)
# DS TIP: Used for zero-copy operations on large datasets (like image matrices) to save RAM.
v = memoryview(b"Hello")
print(v[0]) # 72

# __import__(name, globals=None, locals=None, fromlist=(), level=0)
# DS TIP: Used when you need to load a specific ML library dynamically based on user config.
np_dummy = __import__('math') 

# breakpoint(*args, **kws)
# DS TIP: Put this in a complex pandas .apply() function or custom PyTorch loop to pause execution and inspect variables.
# breakpoint() 

# ==========================================
# 8. ASYNC ITERATION (Python 3.10+)
# ==========================================
heading("--- Asynchronous Iteration ---")

# aiter(async_iterable)
# anext(async_iterator[, default])
# DS TIP: Used in modern data engineering (e.g., fetching paginated data from REST APIs asynchronously to build your dataset faster).
async def fetch_data():
    class AsyncDataStream:
        def __init__(self): self.data = [1, 2]
        def __aiter__(self): return self
        async def __anext__(self):
            if self.data: return self.data.pop(0)
            raise StopAsyncIteration

    # aiter() gets the async iterator, anext() awaits the next value
    stream = aiter(AsyncDataStream())
    print("Async fetch 1:", await anext(stream)) # 1
    print("Async fetch 2:", await anext(stream)) # 2

asyncio.run(fetch_data())
import numpy as np

def heading(title):
    print(f"\n{"-"*40} \n{title} \n{"-"*40}")

# Let's create a few base arrays to use in our examples
arr_1d = np.array([1, 2, 3, 4, 5], dtype=np.int32)
arr_2d = np.array([[1.5, 2.5, 3.5], [4.5, 5.5, 6.5]], dtype=np.float64)
arr_complex = np.array([1 + 2j, 3 + 4j])

print("--- Base Arrays Created ---")
print("arr_1d:\n", arr_1d)
print("arr_2d:\n", arr_2d)
print("arr_complex:\n", arr_complex, "\n")


# ------------------------------------------
heading("1. Structure & Dimensions")
# These attributes help you understand the physical shape and total number of elements within the array.
# ------------------------------------------

# ndarray.ndim: Returns the number of dimensions (axes) of the array. (e.g., 1 for a 1D array, 2 for a matrix).
print("\n--- ndarray.ndim ---")
print(f"Dimensions of arr_1d: {arr_1d.ndim}")
print(f"Dimensions of arr_2d: {arr_2d.ndim}")
# Explanation: arr_1d is a simple list (1 axis), while arr_2d has rows and columns (2 axes).


# ndarray.shape: Returns a tuple of integers indicating the size of the array in each dimension. For a matrix with n rows and m columns, the shape will be (n, m).
print("\n--- ndarray.shape ---")
print(f"Shape of arr_2d: {arr_2d.shape}")
# Explanation: arr_2d has 2 rows and 3 columns, returning (2, 3).


# ndarray.size: Returns the total number of elements in the array. This is equal to the product of the elements of shape.
print("\n--- ndarray.size ---")
print(f"Total elements in arr_2d: {arr_2d.size}")
# Explanation: 2 rows * 3 columns = 6 total elements.


# ndarray.T: Returns the transposed array. While often used as an operation, it is an attribute that provides a view of the array with its axes reversed.
print("\n--- ndarray.T ---")
print(f"Original shape: {arr_2d.shape}")
print(f"Transposed shape: {arr_2d.T.shape}")
print("Transposed array:\n", arr_2d.T)
# Explanation: The rows become columns, and the columns become rows.


# ------------------------------------------
heading("2. Data Types")
# These attributes tell you exactly how the data inside the array is being interpreted.
# ------------------------------------------

# ndarray.dtype: Returns an object describing the data type of the elements in the array (e.g., int32, float64, bool). This dictates how the raw bytes in memory are interpreted.
print("\n--- ndarray.dtype ---")
print(f"Data type of arr_1d: {arr_1d.dtype}")
print(f"Data type of arr_2d: {arr_2d.dtype}")


# ndarray.real: Returns the real part of the array (useful if the dtype is complex).
print("\n--- ndarray.real ---")
print(f"Real part of arr_complex: {arr_complex.real}")
# Explanation: Extracts the '1' and '3' from [1+2j, 3+4j].


# ndarray.imag: Returns the imaginary part of the array.
print("\n--- ndarray.imag ---")
print(f"Imaginary part of arr_complex: {arr_complex.imag}")
# Explanation: Extracts the '2' and '4' from [1+2j, 3+4j].


# ------------------------------------------
heading("3. Memory Consumption & Layout")
# These are the most critical attributes for understanding how much RAM your array is using and how it is physically arranged in memory.
# ------------------------------------------

# ndarray.itemsize: Returns the length of one array element in bytes.
print("\n--- ndarray.itemsize ---")
print(f"Bytes per element in arr_2d (float64): {arr_2d.itemsize}")
# Explanation: A float64 takes up 64 bits, which is exactly 8 bytes (64 / 8).


# ndarray.nbytes: Returns the total number of bytes consumed by the elements of the array. It is generally equal to ndarray.size * ndarray.itemsize.
print("\n--- ndarray.nbytes ---")
print(f"Total bytes consumed by arr_2d: {arr_2d.nbytes}")
# Explanation: 6 elements * 8 bytes per element = 48 bytes total.


# ndarray.strides: Returns a tuple of bytes to step in each dimension when traversing the array.
print("\n--- ndarray.strides ---")
print(f"Strides of arr_2d: {arr_2d.strides}")
# Explanation: The output is (24, 8). 
# To move to the next column (next item in the row), you jump 8 bytes (1 float64). 
# To move to the next row, you must jump past 3 columns (3 * 8 = 24 bytes).


# ndarray.flags: Returns a dictionary-like object containing information about the memory layout of the array.
print("\n--- ndarray.flags ---")
print(arr_2d.flags)
# Explanation: Shows memory configurations. C_CONTIGUOUS being True means data is stored sequentially in memory (C-style).


# ndarray.base: Returns the base object if the array's memory comes from some other object. If the array owns its own data, this returns None.
print("\n--- ndarray.base ---")
arr_view = arr_2d[0:1, :] # Creating a view (slice) of arr_2d
print(f"Base of original arr_2d: {arr_2d.base}")
print(f"Base of arr_view: {arr_view.base is arr_2d}")
# Explanation: arr_2d owns its memory, so its base is None. arr_view is just a slice, so its memory belongs to (is based on) arr_2d.


# ndarray.data: A Python buffer object pointing to the start of the array's data. 
print("\n--- ndarray.data ---")
print(f"Memory buffer object: {arr_1d.data}")
# Explanation: This simply returns the memory address reference. It's rarely used directly in high-level Python code.


# ndarray.ctypes: An object containing properties of the array needed for interacting with the ctypes module.
print("\n--- ndarray.ctypes ---")
print(f"ctypes data pointer: {arr_1d.ctypes.data}")
# Explanation: Returns the raw memory address as an integer, which is required if you are passing this array into a compiled C/C++ library.
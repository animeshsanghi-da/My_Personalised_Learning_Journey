import numpy as np
import io # Used for simulating files in memory
import os # Used for temporary file operations

def heading(title):
    print(f"\n\n{'-'*30} \n{title} \n{'-'*30}")

# ----------------------------------------
heading("1. Ones and Zeros (and Fillers)")
# ----------------------------------------

# np.empty(shape): Returns a new array of given shape and type, without initializing entries.
arr_empty = np.empty((2, 2))
print("np.empty:\n", arr_empty)
# Explanation: The output will contain whatever garbage values were already in that memory space.

# np.empty_like(prototype): Returns a new array with the same shape and type as a given array.
proto = np.array([[1, 2], [3, 4]])
arr_empty_like = np.empty_like(proto)
print("\nnp.empty_like:\n", arr_empty_like)

# np.eye(N): Returns a 2-D array with ones on the diagonal and zeros elsewhere.
arr_eye = np.eye(3)
print("\nnp.eye:\n", arr_eye)

# np.identity(n): Returns the identity array (a square array with ones on the main diagonal).
arr_identity = np.identity(3)
print("\nnp.identity:\n", arr_identity)
# Explanation: Very similar to np.eye, but strictly square (n x n).

# np.ones(shape): Returns a new array of given shape and type, filled with ones.
arr_ones = np.ones((2, 3))
print("\nnp.ones:\n", arr_ones)

# np.ones_like(prototype): Returns an array of ones with the same shape and type as a given array.
arr_ones_like = np.ones_like(proto)
print("\nnp.ones_like:\n", arr_ones_like)

# np.zeros(shape): Returns a new array of given shape and type, filled with zeros.
arr_zeros = np.zeros((2, 2))
print("\nnp.zeros:\n", arr_zeros)

# np.zeros_like(prototype): Returns an array of zeros with the same shape and type as a given array.
arr_zeros_like = np.zeros_like(proto)
print("\nnp.zeros_like:\n", arr_zeros_like)

# np.full(shape, fill_value): Returns a new array of given shape and type, filled with fill_value.
arr_full = np.full((2, 2), 7)
print("\nnp.full:\n", arr_full)

# np.full_like(prototype, fill_value): Returns a full array with the same shape and type as a given array.
arr_full_like = np.full_like(proto, 9)
print("\nnp.full_like:\n", arr_full_like)


# ----------------------------------------
heading("2. Numerical Ranges")
# ----------------------------------------

# np.arange([start,] stop[, step]): Return evenly spaced values within a given interval.
arr_arange = np.arange(0, 10, 2)
print("\nnp.arange:\n", arr_arange)

# np.linspace(start, stop, num): Returns evenly spaced numbers over a specified interval.
arr_linspace = np.linspace(0, 1, 5)
print("\nnp.linspace:\n", arr_linspace)
# Explanation: Generates exactly 5 numbers evenly spaced between 0 and 1 (inclusive).

# np.logspace(start, stop, num): Returns numbers spaced evenly on a log scale.
arr_logspace = np.logspace(1, 3, 3)
print("\nnp.logspace:\n", arr_logspace)
# Explanation: Returns 10^1, 10^2, 10^3.

# np.geomspace(start, stop, num): Returns numbers spaced evenly on a log scale (a geometric progression).
arr_geomspace = np.geomspace(1, 100, 3)
print("\nnp.geomspace:\n", arr_geomspace)
# Explanation: Starts at 1, ends at 100, multiplies by a constant factor (10 in this case).

# np.meshgrid(*xi): Return coordinate matrices from coordinate vectors.
x = np.array([1, 2])
y = np.array([3, 4, 5])
X, Y = np.meshgrid(x, y)
print("\nnp.meshgrid X:\n", X)
print("np.meshgrid Y:\n", Y)

# np.mgrid: An instance which returns a dense multi-dimensional "meshgrid".
arr_mgrid = np.mgrid[0:2, 0:3]
print("\nnp.mgrid:\n", arr_mgrid)
# Explanation: Uses slice notation directly rather than function arguments.

# np.ogrid: An instance which returns an open multi-dimensional "meshgrid".
arr_ogrid = np.ogrid[0:2, 0:3]
print("\nnp.ogrid:\n", arr_ogrid)
# Explanation: Returns open (sparse) grids to save memory before broadcasting.


# ----------------------------------------
heading("3. From Existing Data")
# ----------------------------------------

# np.array(object): Creates an array from an array-like object (e.g., a Python list or tuple).
arr_array = np.array([1, 2, 3])
print("\nnp.array:\n", arr_array)

# np.asarray(a): Converts the input to an array (does not copy if the input is already an ndarray).
arr_asarray = np.asarray([1, 2, 3])
print("\nnp.asarray:\n", arr_asarray)

# np.asanyarray(a): Converts the input to an ndarray, but passes ndarray subclasses through.
matrix_subclass = np.matrix([[1, 2], [3, 4]])
arr_asanyarray = np.asanyarray(matrix_subclass)
print("\nnp.asanyarray:\n", type(arr_asanyarray))
# Explanation: Retains the 'matrix' subclass type, whereas np.asarray would convert it to a base ndarray.

# np.ascontiguousarray(a): Returns a contiguous array (C-order) in memory.
arr_ascontiguous = np.ascontiguousarray(np.ones((2, 2)).T)
print("\nnp.ascontiguousarray:\n", arr_ascontiguous.flags['C_CONTIGUOUS'])

# np.asmatrix(data): Interprets the input as a matrix.
arr_asmatrix = np.asmatrix([[1, 2], [3, 4]])
print("\nnp.asmatrix:\n", type(arr_asmatrix))

# np.copy(a): Returns an array copy of the given object.
original = np.array([1, 2, 3])
arr_copy = np.copy(original)
print("\nnp.copy:\n", arr_copy)

# np.frombuffer(buffer): Interprets a buffer as a 1-dimensional array.
byte_string = b'hello world'
arr_frombuffer = np.frombuffer(byte_string, dtype='S1')
print("\nnp.frombuffer:\n", arr_frombuffer)

# np.fromfile(file): Constructs an array from data in a text or binary file.
with open('temp.dat', 'wb') as f:
    f.write(np.array([1.5, 2.5, 3.5]).tobytes())
arr_fromfile = np.fromfile('temp.dat', dtype=float)
print("\nnp.fromfile:\n", arr_fromfile)
os.remove('temp.dat') # clean up

# np.fromfunction(function, shape): Constructs an array by executing a function over each coordinate.
arr_fromfunc = np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int)
print("\nnp.fromfunction:\n", arr_fromfunc)
# Explanation: Value at index (i, j) is calculated as i + j.

# np.fromiter(iterable, dtype): Creates a new 1-dimensional array from an iterable object.
iterable = (x*x for x in range(5))
arr_fromiter = np.fromiter(iterable, float)
print("\nnp.fromiter:\n", arr_fromiter)

# np.fromstring(string): A new 1-D array initialized from text data in a string.
arr_fromstring = np.fromstring('1 2 3 4', dtype=int, sep=' ')
print("\nnp.fromstring:\n", arr_fromstring)

# np.loadtxt(fname): Loads data from a text file.
mock_file = io.StringIO("1 2\n3 4")
arr_loadtxt = np.loadtxt(mock_file)
print("\nnp.loadtxt:\n", arr_loadtxt)

# np.genfromtxt(fname): Loads data from a text file, with missing values handled as specified.
mock_csv = io.StringIO("1, 2\n3, ") # Notice the missing value
arr_genfromtxt = np.genfromtxt(mock_csv, delimiter=',', filling_values=-99)
print("\nnp.genfromtxt:\n", arr_genfromtxt)


# ----------------------------------------
heading("4. Building Matrices (2D Arrays)")
# ----------------------------------------

# np.diag(v): Extracts a diagonal or constructs a diagonal array.
arr_diag = np.diag([1, 2, 3])
print("\nnp.diag:\n", arr_diag)

# np.diagflat(v): Creates a two-dimensional array with the flattened input as a diagonal.
arr_diagflat = np.diagflat([[1, 2], [3, 4]])
print("\nnp.diagflat:\n", arr_diagflat)
# Explanation: Flattens the 2D input into [1, 2, 3, 4] and makes a 4x4 diagonal matrix.

# np.tri(N): An array with ones at and below the given diagonal and zeros elsewhere.
arr_tri = np.tri(3)
print("\nnp.tri:\n", arr_tri)

# np.tril(m): Lower triangle of an array.
m = np.ones((3, 3))
arr_tril = np.tril(m)
print("\nnp.tril:\n", arr_tril)

# np.triu(m): Upper triangle of an array.
arr_triu = np.triu(m)
print("\nnp.triu:\n", arr_triu)

# np.vander(x): Generates a Vandermonde matrix.
x_vander = np.array([1, 2, 3])
arr_vander = np.vander(x_vander, 3)
print("\nnp.vander:\n", arr_vander)
# Explanation: The columns are powers of the input vector (x^2, x^1, x^0).

# np.asmatrix(data): Interprets the input as a matrix.
arr_mat = np.asmatrix([[1, 2], [3, 4]])
print("\nnp.asmatrix:\n", arr_mat)

# np.bmat(obj): Builds a matrix object from a nested sequence or array.
# (Using standard arrays for the blocks is the modern standard)
A = np.array([[1, 1], [1, 1]])
B = np.array([[2, 2], [2, 2]])
arr_bmat = np.bmat([[A, B], [B, A]])
print("\nnp.bmat:\n", arr_bmat)
# Explanation: Concatenates blocks of arrays/matrices into a single larger matrix.

# ----------------------------------------
heading("5. Random Arrays (The numpy.random Module)")
# ----------------------------------------

# np.random.rand(d0, d1, ...): Random values in a given shape (uniform distribution over [0, 1)).
arr_rand = np.random.rand(2, 2)
print("\nnp.random.rand:\n", arr_rand)

# np.random.randn(d0, d1, ...): Returns a sample from the "standard normal" distribution.
arr_randn = np.random.randn(2, 2)
print("\nnp.random.randn:\n", arr_randn)

# np.random.randint(low, high, size): Returns random integers from low (inclusive) to high (exclusive).
arr_randint = np.random.randint(0, 10, size=(2, 2))
print("\nnp.random.randint:\n", arr_randint)

# np.random.default_rng().random(size): The modern, recommended way to generate random floats.
rng = np.random.default_rng()
arr_rng = rng.random((2, 2))
print("\nnp.random.default_rng().random:\n", arr_rng)
# Explanation: This is the updated Generator API introduced in NumPy 1.17, preferred over np.random.rand().
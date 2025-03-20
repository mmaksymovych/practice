# --- MOST USED DATA TYPES ---

# String (str) - Text data
name = "Alice"  # A sequence of characters

# Integer (int) - Whole numbers
age = 25  # No decimal point

# Float (float) - Decimal numbers
price = 19.99  # Contains a decimal point

# Boolean (bool) - True or False values
is_active = True  # Represents a true/false condition

# List (list) - Ordered, mutable collection
fruits = ["apple", "banana", "cherry"]  # Can be modified
vegetables = ['cucumber', 'tomato', 'lettuce']

food = [fruits, vegetables]


# Tuple (tuple) - Ordered, immutable collection
coordinates = (10.0, 20.0)  # Cannot be changed

# Dictionary (dict) - Key-value pairs
person = {
    "name": "Alice", 
    "age": 25,
    "maried": False
}  # Key-value mapping

# Set (set) - Unordered collection of unique items
unique_numbers = {1, 2, 3, 4, 4}  # Duplicates are removed

# --- LESS COMMON BUT STILL USED DATA TYPES ---

# Complex (complex) - Numbers with real and imaginary parts
z = 2 + 3j  # Used in advanced math operations

# Range (range) - Sequence of numbers
numbers = range(5)  # Generates numbers from 0 to 4

# Frozen Set (frozenset) - Immutable set
immutable_set = frozenset({1, 2, 3})  # Cannot be modified

# Bytes (bytes) - Immutable sequence of bytes
byte_data = b"hello"  # Used for binary data

# Bytearray (bytearray) - Mutable sequence of bytes
mutable_bytes = bytearray(b"hello")  # Can be modified

# Memoryview (memoryview) - View of a byte sequence
mem_view = memoryview(byte_data)  # Efficiently handle binary data

# NoneType (None) - Represents the absence of a value
result = None  # Used when a variable has no value
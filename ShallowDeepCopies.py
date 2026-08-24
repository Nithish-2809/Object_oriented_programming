# In Python, assignment (y = x) never creates a copy of an object—it only binds a new name to the existing object in memory.
#  When you need a distinct object, you choose between a shallow copy and a deep copy.

# Core Difference
# Shallow Copy: Creates a new outer collection object, but inserts references to the objects found in the original.
#  The inner/nested objects are shared in memory.

# Deep Copy: Creates a new outer collection object and recursively copies all nested objects found inside.
#  The original and copied objects share zero mutable child references.

# Original Outer List [0x100] ---> Outer List Object
#   ├── Index 0: 10 (Primitive)
#   └── Index 1: [0x200] ---------> [1, 2] (Nested List Object)

# Shallow Copy [0x300] ----------> New Outer List Object
#   ├── Index 0: 10
#   └── Index 1: [0x200] ---------> (Points to SAME Nested List Object)

# Deep Copy [0x400] -------------> New Outer List Object
#   ├── Index 0: 10
#   └── Index 1: [0x500] ---------> [1, 2] (NEW Nested List Object)


import copy

original = [1, [2, 3]]

# 1. Shallow Copy
shallow_a = copy.copy(original)
shallow_b = original.copy()  # Built-in list method
shallow_c = original[:]       # Slicing creates shallow copy

# 2. Deep Copy
deep_a = copy.deepcopy(original)
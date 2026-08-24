# # Python Methods — Complete Notes

# ## 🛠️ 1. Instance Method

# ### What it is

# The standard method used by default in Object-Oriented Programming.

# ### Arguments

# Automatically takes `self` (the specific object instance) as the first argument.

# ### Access

# * Can read and modify **instance data**
# * Can read and modify **class data**

# ### Use Case

# Handling unique data belonging to a specific object.

# ### Example

# ```python
# class Student:
#     def __init__(self, name):
#         self.name = name

#     def display(self):  # Instance Method
#         print(self.name)

# s1 = Student("Nithish")
# s1.display()
# ```

# ---

# ## 🏢 2. Class Method

# ### What it is

# A method bound to the **class itself**, not to any individual object.

# ### Arguments

# Automatically takes `cls` (the class) as the first argument.

# ### Access

# * Can read and modify **class-wide data**
# * Cannot directly access individual instance data

# ### Use Case

# Creating alternative constructors (factory methods) or managing class-level information.

# ### Example

# ```python
# class Student:
#     college = "ABC College"

#     @classmethod
#     def change_college(cls, name):
#         cls.college = name

# Student.change_college("XYZ College")

# print(Student.college)
# ```

# ---

# ## 🧮 3. Static Method

# ### What it is

# An independent utility function placed inside a class for logical organization.

# ### Arguments

# Takes **no automatic arguments** — neither `self` nor `cls`.

# ### Access

# * Cannot directly access instance data
# * Cannot directly access class data

# ### Use Case

# Performing calculations or helper/utility tasks related to the class.

# ### Example

# ```python
# class Math:

#     @staticmethod
#     def add(a, b):
#         return a + b

# print(Math.add(5, 3))
# ```

# ---

# ## 🧱 4. Concrete Method

# ### What it is

# A method that contains a **complete implementation** (actual executable code).

# ### Contrast

# It is the opposite of an **abstract method**, which defines a required behavior that child classes must implement.

# ### Access

# A concrete method can be:

# * Instance Method
# * Class Method
# * Static Method

# As long as it has a complete implementation.

# ### Use Case

# Providing ready-to-use behavior that child classes can inherit or override.

# ### Example

# ```python
# class Animal:

#     def sound(self):  # Concrete Method
#         print("Some sound")
# ```

# ---

# # ⚡ Quick Comparison

# | Method              | First Argument | Works With           | Decorator       | Main Use                              |
# | ------------------- | -------------- | -------------------- | --------------- | ------------------------------------- |
# | **Instance Method** | `self`         | Object/instance data | None            | Object-specific behavior              |
# | **Class Method**    | `cls`          | Class-level data     | `@classmethod`  | Class data & alternative constructors |
# | **Static Method**   | None           | Independent logic    | `@staticmethod` | Utility/helper functions              |
# | **Concrete Method** | Depends        | Depends              | Depends         | Fully implemented behavior            |

# ---

# # 🎯 Interview One-Liners

# * **Instance Method** → Works with object-specific data using `self`.
# * **Class Method** → Works with class-level data using `cls`.
# * **Static Method** → Utility function inside a class; uses neither `self` nor `cls`.
# * **Concrete Method** → A method with a complete implementation.

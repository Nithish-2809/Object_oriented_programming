#Serialization
#The process of converting python datatypes to json format is know as serialization.
#Deserialization
#The process of converting json to python datatypes is known as deserialization.

import json

data = {"name": "Amit", "role": "Intern", "stipend": 25000}

# --- SERIALIZATION (Writing to a file) ---
# 'w' means write mode. 'f' is our temporary file variable name.
with open("user_data.json", "w") as f:
    json.dump(data, f)  # Generates a physical 'user_data.json' file

print("Data successfully serialized to file.")


# --- DESERIALIZATION (Reading from a file) ---
# 'r' means read mode.
with open("user_data.json", "r") as f:
    loaded_data = json.load(f)  # Reads the file and converts it to a dict

print("\nDeserialized Data from file:")
print(loaded_data)
print(loaded_data["name"])  # Output: Amit

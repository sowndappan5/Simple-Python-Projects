import re

def addressVal(address):
    # Check if there's exactly one "@" and one "."
    if address.count("@") != 1:
        return "Invalid: Email should contain exactly one '@' symbol."
    if address.count(".") < 1:
        return "Invalid: Email should contain at least one '.' symbol."

    # Find positions of "@" and "."
    at_pos = address.find("@")
    dot_pos = address.rfind(".")

    # Check if "@" comes before "." and both are within appropriate positions
    if at_pos > dot_pos or at_pos == 0 or dot_pos == len(address) - 1:
        return "Invalid: '@' must come before '.' and both must be in valid positions."

    # Ensure email does not contain spaces or unsupported characters
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', address):
        return "Invalid: Email contains unsupported characters."

    # If all checks pass
    return "Valid"

print("This program will decide if your input is a valid email address.")
print("Type 'exit' to quit.")

while True:
    print("\nA valid email address needs an '@' symbol and a '.' in appropriate places.")
    x = input("Input your email address: ")
    
    if x.lower() == "exit":
        print("Exiting the program.")
        break
    
    # Validate and provide feedback
    result = addressVal(x)
    print(result)

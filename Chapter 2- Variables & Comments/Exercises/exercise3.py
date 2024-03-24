# Define the person's name with whitespace characters
name = "\t\t\tJohn Doe\n"

# Print the name with whitespace
print("Name with Whitespace:")
print(name)

# Print the name using each stripping function
print("\nAfter Stripping:")
print("Using lstrip():", name.lstrip())
print("Using rstrip():", name.rstrip())
print("Using strip():", name.strip())

# Initialize an empty list to store pizza toppings
toppings = []

# Prompt the user to enter pizza toppings
print("Enter pizza toppings (enter 'quit' to finish):")
while True:
    topping = input("Enter a topping: ")
    if topping.lower() == 'quit':
        break  # Exit the loop if 'quit' is entered
    else:
        toppings.append(topping)
        print("Adding", topping, "to your pizza.")

# Print the list of pizza toppings
print("\nYour pizza will have the following toppings:")
for topping in toppings:
    print("- " + topping)

# Loop to ask users their age and determine ticket cost
while True:
    age = input("Please enter your age (or 'quit' to exit): ")
    if age.lower() == 'quit':
        break  # Exit the loop if 'quit' is entered
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free.")
        elif age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")

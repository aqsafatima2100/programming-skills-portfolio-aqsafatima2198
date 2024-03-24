
# Make a list called sandwich_orders and fill it with the names of various sandwiches
sandwich_orders = ['tuna', 'pastrami', 'turkey', 'pastrami', 'ham', 'pastrami', 'chicken', 'pastrami']

# Make an empty list called finished_sandwiches
finished_sandwiches = []

# Print a message saying the deli has run out of pastrami
print("Sorry, the deli has run out of pastrami.")

# Remove all occurrences of 'pastrami' from sandwich_orders using a while loop
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through the list of sandwich orders
while sandwich_orders:
    # Get the next sandwich order
    current_order = sandwich_orders.pop(0)
    # Make the sandwich
    print("I made your " + current_order + " sandwich.")
    # Move the made sandwich to the list of finished sandwiches
    finished_sandwiches.append(current_order)

# Print a message listing each sandwich that was made
print("\nList of sandwiches made:")
for sandwich in finished_sandwiches:
    print("- " + sandwich.title())

# Make a list called sandwich_orders and fill it with the names of various sandwiches
sandwich_orders = ['olive', 'lettuce', 'mayo', 'cucumber', 'chicken']

# Make an empty list called finished_sandwiches
finished_sandwiches = []

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

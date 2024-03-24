# Make several dictionaries representing different pets
pet1 = {'animal': 'dog', 'owner': 'Ayesha'}
pet2 = {'animal': 'cat', 'owner': 'Aqsa'}
pet3 = {'animal': 'rabbit', 'owner': 'Rajaa'}
pet4 = {'animal': 'hamster', 'owner': 'Samia'}

# Store the dictionaries in a list called pets
pets = [pet1, pet2, pet3, pet4]

# Loop through the list and print everything known about each pet
for pet in pets:
    print("Animal:", pet['animal'].title())
    print("Owner:", pet['owner'].title())
    print()  # Print a blank line to separate information about each pet

# Define a dictionary of rivers and the countries they run through
rivers = {
    'nile': 'Egypt',
    'amazon': 'Brazil',
    'indus': 'Pakistan'
}

# Print a sentence about each river
print("Sentences about each river:")
for river, country in rivers.items():
    print("The", river.title(), "runs through", country + ".")

# Print the name of each river
print("\nNames of each river:")
for river in rivers.keys():
    print(river.title())

# Print the name of each country
print("\nNames of each country:")
for country in rivers.values():
    print(country)

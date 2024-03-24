def describe_city(city, country="default country"):
    """Prints a simple sentence describing the city and its country."""
    print(city.title() + " is in " + country.title())

# Call the function for three different cities
describe_city("karachi", "islamabad")
describe_city("tokyo", "japan")
describe_city("new york")

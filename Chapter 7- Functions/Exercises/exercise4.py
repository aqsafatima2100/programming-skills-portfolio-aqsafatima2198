def make_shirt(size="large", message="I love Python"):
    """Prints a sentence summarizing the size of the shirt and the message printed on it."""
    print("Size:", size)
    print("Message:", message)

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt(size="medium")

# Make a shirt of any size with a different message
make_shirt(size="small", message="Keep calm and code on")

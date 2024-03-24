def make_shirt(size, message):
    """Prints a sentence summarizing the size of the shirt and the message printed on it."""
    print("Size:", size)
    print("Message:", message)

# Call the function once using positional arguments
make_shirt("medium", "I love Coding")

# Call the function a second time using keyword arguments
make_shirt(size="large", message="Keep calm and code on")

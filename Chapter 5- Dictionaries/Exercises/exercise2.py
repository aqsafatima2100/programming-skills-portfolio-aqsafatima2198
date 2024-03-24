# Define a glossary with programming words and their meanings
glossary = {
    'variable': 'A named storage location in memory used to store data that can be manipulated during program execution.',
    'function': 'A named block of code that performs a specific task. Functions are reusable and can be called multiple times in a program.',
    'loop': 'A programming construct that repeats a block of code multiple times until a certain condition is met.',
    'list': 'A data structure in Python that stores a collection of items. Lists are ordered, mutable, and can contain elements of different data types.',
    'dictionary': 'A data structure in Python that stores key-value pairs. Dictionaries are unordered, mutable, and can contain elements of different data types.'
}

# Print each word and its meaning as neatly formatted output
for word, meaning in glossary.items():
    print(word.title() + ":\n" + meaning + "\n")

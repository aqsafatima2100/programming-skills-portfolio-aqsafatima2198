# Define the initial glossary with programming words and their meanings
glossary = {
    'variable': 'A named storage location in memory used to store data that can be manipulated during program execution.',
    'function': 'A named block of code that performs a specific task. Functions are reusable and can be called multiple times in a program.',
    'loop': 'A programming construct that repeats a block of code multiple times until a certain condition is met.',
    'list': 'A data structure in Python that stores a collection of items. Lists are ordered, mutable, and can contain elements of different data types.',
    'dictionary': 'A data structure in Python that stores key-value pairs. Dictionaries are unordered, mutable, and can contain elements of different data types.'
}

# Add five more Python terms and their meanings to the glossary
glossary['tuple'] = 'An immutable data structure in Python that stores a collection of items. Tuples are ordered and can contain elements of different data types.'
glossary['set'] = 'A data structure in Python that stores a collection of unique elements. Sets are unordered and mutable.'
glossary['method'] = 'A function associated with an object in Python. Methods are called using dot notation and act on the object itself.'
glossary['module'] = 'A file containing Python code that can be imported and used in other Python programs.'
glossary['class'] = 'A blueprint for creating objects in Python. Classes define the properties and behaviors of objects.'

# Print each word and its meaning using a loop
for word, meaning in glossary.items():
    print(word.title() + ":\n" + meaning + "\n")

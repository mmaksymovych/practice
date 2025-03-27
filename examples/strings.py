# Common Examples of Working with Strings in Python

# Example of concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

# Example of formatting
age = 30
formatted_string = f"My name is {full_name} and I am {age} years old."
print(formatted_string)

# Example of splitting a string
sentence = "Hello how are you?"
words = sentence.split(" ")
print(words)

# Example of joining strings
words_joined = "-".join(words)
print(words_joined)

# Example of replacing substrings
original_string = "I like apples"
modified_string = original_string.replace("apples", "bananas")
print(modified_string)

# Example of uppercase and lowercase conversion
print(original_string.upper())
print(original_string.lower())

# Example of checking substring
print("apples" in original_string)

# Example of getting character by index
char_at_index = original_string[2]
print(char_at_index)

# Example of going over the string
for char in original_string:
    print(char, end=" ")

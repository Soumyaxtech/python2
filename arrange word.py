# Accept input from the user
input_sequence = input("Enter a hyphen-separated sequence of words: ")

# Split the input into a list of words
words = input_sequence.split('-')

# Sort the words alphabetically
sorted_words = sorted(words)

# Join the sorted words into a hyphen-separated sequence
output_sequence = '-'.join(sorted_words)

# Print the result
print("Output:", output_sequence)

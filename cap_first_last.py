# Step 1: Input string
string = "hello world welcome"

# Step 2: Split the string into words
words = string.split()

# Step 3: Create a result list to hold modified words
result = []

# Step 4: Process each word
for word in words:
    if len(word) == 1:
        # For single-letter words, just capitalize
        result.append(word.upper())
    else:
        # Capitalize first and last character, keep middle part unchanged
        new_word = word[0].upper() + word[1:-1] + word[-1].upper()
        result.append(new_word)

# Step 5: Join the modified words back into a string
final_string = ' '.join(result)

# Step 6: Print result
print(final_string)

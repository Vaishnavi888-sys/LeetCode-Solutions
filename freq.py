# Step 1: Input string
string = "hello world"

# Step 2: Create empty dictionary
freq = {}

# Step 3: Loop through each character
for char in string:
    if char in freq:  # If character already in dict
        freq[char] += 1
    else:             # First time seeing this character
        freq[char] = 1

# Step 4: Print result
print(freq)

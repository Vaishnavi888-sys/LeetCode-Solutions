# Step 1: Input a number
num = 5794213

# Step 2: Convert number to string to access each digit
num_str = str(num)

# Step 3: Assume first digit as min and max
max_digit = int(num_str[0])
min_digit = int(num_str[0])

# Step 4: Loop through each digit
for digit in num_str:
    digit = int(digit)
    if digit > max_digit:
        max_digit = digit
    if digit < min_digit:
        min_digit = digit

# Step 5: Print results
print("Maximum digit:", max_digit)
print("Minimum digit:", min_digit)

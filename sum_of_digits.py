# Step 1: Input a number
num = 12345

# Step 2: Initialize sum
sum_digits = 0

# Step 3: Loop through each digit
while num > 0:
    digit = num % 10           # Get last digit
    sum_digits += digit        # Add digit to sum
    num = num // 10            # Remove last digit

# Step 4: Print result
print("Sum of digits:", sum_digits)

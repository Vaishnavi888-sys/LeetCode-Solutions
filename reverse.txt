# Step 1: Input a number
num = 12345

# Step 2: Initialize reversed number
reversed_num = 0

# Step 3: Loop to reverse the number
while num > 0:
    digit = num % 10           # Get the last digit
    reversed_num = reversed_num * 10 + digit  # Build the reversed number
    num = num // 10            # Remove the last digit from original number

# Step 4: Print the reversed number
print("Reversed number:", reversed_num)

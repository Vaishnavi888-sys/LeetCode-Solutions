# Step 1: Define the range
start = 10
end = 200

# Step 2: Loop through the range
for num in range(start, end + 1):
    original = num  # Store the original number
    reversed_num = 0  # To build the reversed number
    temp = num  # Temporary number for manipulation

    # Step 3: Reverse the number using math
    while temp > 0:
        digit = temp % 10  # Extract last digit
        reversed_num = reversed_num * 10 + digit  # Build reversed number
        temp = temp // 10  # Remove last digit

    # Step 4: Check if original equals reversed
    if original == reversed_num:
        print(original, end=' ')  # Print palindrome number

# Define the range
start = 10
end = 50

# Loop through each number in the range
for num in range(start, end + 1):
    if num > 1:  # Primes start from 2
        is_prime = True

        # Check divisibility up to sqrt(num)
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break  # No need to continue if a divisor is found

        if is_prime:
            print(num, end=' ')  # Print prime numbers in one line

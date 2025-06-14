# Step 1: Input a year
year = 2024

# Step 2: Check leap year conditions
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is Not a Leap Year")

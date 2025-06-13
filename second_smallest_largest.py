arr = [5, 2, 9, 1, 7]
unique = list(set(arr))  # remove duplicates
unique.sort()

second_smallest = unique[1]
second_largest = unique[-2]

print("Second Smallest:", second_smallest)  # Output: 2
print("Second Largest:", second_largest)    # Output: 7

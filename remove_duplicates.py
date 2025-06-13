def remove_duplicates(arr):
    if not arr:
        return 0

    i = 0  # pointer for unique index

    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]

    return i + 1  # length of unique portion

string = "Beautiful Day"
chars = list(string)  # Convert to list

vowels = 'aeiouAEIOU'

for vowel in vowels:
    while vowel in chars:
        chars.remove(vowel)  # Remove all instances of each vowel

result = ''.join(chars)  # Convert back to string
print(result)

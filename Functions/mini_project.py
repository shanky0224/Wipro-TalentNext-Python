'''
1. WAf that accepts a hyphen-separated sequence of colors
as input and returns the colors in a hyphen-separated 
sequence after sorting them alphabatically.
'''
def sort_colors(color_sequence):
    colors = color_sequence.split('-')
    colors.sort()
    return '-'.join(colors)

print(sort_colors('blue-red-green-white-yellow')) 





'''
2. Create a python module with following functions:
ispalindrome(name): Given the user name as input, this function should 
tell us whether the name is a palindrome or not.

count_the_vowels(name): Given the user name as input, this function should 
tell us how many vowels are present in it.

frequency_of_letters(name): Given the user as input, this function should
tell us how many times each letter appears in the name.

Sample input: bob
Sample output:
Yes it is a palindrome
No of vowels: 1
Frequency of letters: b-2, o-1
'''
def ispalindrome(name):
    name = name.lower()
    if name == name[::-1]:
        return "Yes it is a palindrome"
    else:
        return "No it is not a palindrome"

def count_the_vowels(name):
    name = name.lower()
    vowels = 'aeiou'
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    return f"No of vowels: {count}"

def frequency_of_letters(name):
    name = name.lower()
    frequency = {}
    for char in name:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    freq_str = ', '.join(f"{key}-{value}" for key, value in frequency.items())
    return f"Frequency of letters: {freq_str}"


name="bob"
print(ispalindrome(name))
print(count_the_vowels(name))
print(frequency_of_letters(name))
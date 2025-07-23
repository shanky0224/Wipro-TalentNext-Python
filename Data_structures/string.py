# 1. WAP to count no. of upper and lower case letters in a string
s1="Hello WorLd"
count_upper=0
count_lower=0
for i in s1:
    if i.isupper():
        count_upper+=1
    else:
        count_lower+=1
print(count_upper)
print(count_lower)


# 2. WAP that will check whether a given string is palindrome or not
s1="madam"
if s1==s1[::-1]:
    print(f"{s1} is palindrome")
else:
    print(f"{s1} is not palindrome")



'''
3. Given a string, return a new string made of n copies of first 2 chars
of the original string where n is the length of the string. The string length
will be >=2. 
If input is "Wipro" then o/p should be "WiWiWiWiWi"   
'''
s1="Wipro"
n=len(s1)
s2=s1[:2]*n
print(s2)


'''
4. Given a string, if the first or last char is 'x', return the string 
without those 'x', else return the string unchanged. If the i/p is
"xHix", then o/p is "Hi"
'''
s1="xxHixx"
if s1.startswith('x'):
    s1=s1[1:]
if s1.endswith('x'):
    s1=s1[:-1]
print(s1)


'''
5. Given a string and an integer n, return a string made of n repetitions
of the last n chars of the string. You may assume that n is b/w 0 and length
of string. If i/p are "Wipro" and 3, then o/p should be "propropro" 
'''
s1="Wipro"
n=3
s2=s1[-n:]*n
print(s2)
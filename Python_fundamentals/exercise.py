# 1. WAP to check if given no is pos, neg or zero
a = int(input("Enter a number: "))
if a > 0:
    print("Number is positive")
elif a < 0:
    print("Number is negative")
else:
    print("Number is zero")


# 2. WAP to check if given no is odd or even
a = int(input("Enter a number: "))
if a % 2 == 0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")


# 3. Given two non negative values, print true if they have same last digit.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if(a%10 == b%10):
    print(f"True, they have same last digit: {a%10}")
else:
    print(f"False, they have different last digit: {a%10} and {b%10}")


# 4. WAP to print nos. from 1 to 10 in a single row with one tab space
for i in range(1, 11):
    print(i, end='\t')


# 5. WAP to print even nos. b/w 27 and 57. Each no. should be printed in a separate row
for i in range(27, 58):
    if i % 2 == 0:
        print(i, '\n')


# 6. WAP to check given no. is prime or not
flag=0
a = int(input("Enter a number: "))
for i in range(2,a):
    if (a % i) == 0:
        flag=1
if(flag==1):
    print(f"{a} is not a prime number")
else:
    print(f"{a} is a prime number")


# 7. WAP to print prime numbers b/w 10 and 99
for i in range(10, 100):
    flag = 0
    for j in range(2, i):
        if (i % j) == 0:
            flag=1
            break
    if flag==0:
        print(i)
        

# 8. WAP to print sum of all digits
a = int(input("Enter a number: "))
sum = 0
while(a>0):
    sum = sum + a%10
    a = a//10
print(sum)


# 9. WAP to reverse a given no. and print
a = int(input("Enter a number: "))
rev = 0
while(a>0):
    rev = rev*10 + a%10
    a = a//10
print(rev)


# 10. WAP to check given no. is palindrome or not
a = int(input("Enter a number: "))
rev = 0
s=a
while(s>0):
    rev = rev*10 + s%10
    s = s//10
if(rev==a):
    print(f"{a} is a palindrome number")
else:
    print(f"{a} is not a palindrome number")
    
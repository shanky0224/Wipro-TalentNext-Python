# 1. WAF to return the sum of all nos. in a list
def addNos(nums):
    sum=0
    for num in nums:
        sum += num
    return sum

nums=[1,2,3,4,5]
print(addNos(nums))


# 2. WAF to return the reverse of a string
def reverseString(s):
    return s[::-1]

s1="Hello World"
print(reverseString(s1))


# 3. WAF to calculate and return the factorial of a no.
def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num-1)

print(fact(5))


# 4. WAF that accepts a string and prints the no. of upper case and lower caes letters in it
def countLetters(s):
    count_upper=0
    count_lower=0
    for i in s:
        if i.isupper():
            count_upper += 1
        else:
            count_lower += 1
    return count_upper, count_lower
    
s="Hello WOrlD GoodBye"
a,b=countLetters(s)
print("Upper case letters: ", a)
print("Lower case letters: ", b)


'''
5. WAF to print the even nos. from a given list. List is passed to the 
function as an argument.
Sample List: [1,2,3,4,5,6,7,8,9]
Output: [2,4,6,8]
'''
def countEven(l1):
    for i in l1:
        if i%2!=0:
            l1.remove(i)
    print(l1)

l1=[1,2,3,4,5,6,7,8,9]
countEven(l1)


# 6. WAF that takes a num as an parameter and checks whether the num is prime or not
def isPrime(num):
    flag=0
    for i in range(2,num):
        if num%i==0:
            flag=1
            break
    if flag==0:
        return True
    return False

print(isPrime(9))


'''
1.WAP to accept two nums from user and perform division. If any 
exception occurs, print an error message else print result.
'''
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid integers.")
except Exception as e:
    print("An unexpected error occurred:", e)
else:
    print("Result of division:", result)


'''
2. WAP a program to accept a number from the user and check whether
it's prime or not. If user enters anything other than number, handle 
exception and print an error message.
'''
try:
    num=int(input("enter a num: "))
    def isPrime(num):
        flag=0
        for i in range(2,num):
            if num%i==0:
                flag=1
                break
        if flag==0:
            return True
        return False
except ValueError:
    print("Error: Please enter a valid integer.")
except Exception as e:
    print("An unexpected error occurred:", e)
else:
    if isPrime(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")


'''
3. WAP to accept the file name to be opened from the user, 
if file exists print the contents of the file in title case or else
handle the exception and print an error message.
'''
try:
    filename = input("Enter the filename to be opened: ")
    with open(filename, 'r') as file:
        contents = file.read()
        print(contents.title())
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")


'''
4. Declare a list with 10 integers and ask the user to enter an 
index. Check whether the number in that index is positive or negative
number. If any invalid index is entered, handle the exception and print
an error message.
'''
try:
    l=[1,2,-4,-69,18,-269,33,-44]
    index=int(input("enter index: "))
    if l[index]>0:
        print(f"Number at index {index} is positive: {l[index]}")
    elif l[index]<0:
        print(f"Number at index {index} is negative: {l[index]}")
except IndexError:
    print("Error: Invalid index. Please enter a valid index.")

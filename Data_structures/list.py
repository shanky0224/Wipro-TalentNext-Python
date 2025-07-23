# 1. WAP to create list of 5 integers and display the list elements. Access individual elements through index
a=[]
for i in range(5):
    x=int(input("enter no.: "))
    a.append(x)
print(a)

print("\naccessing individual elements")
for i in range(5):
    print(f"element at index {i}: {a[i]}")


# 2. WAP to append new item to the end of the list
a=[]
for i in range(5):
    x=int(input("enter no.: "))
    a.append(x)
print(a)


# 3. WAP to reverse the order of items in the list
a=[]
for i in range(5):
    x=int(input("enter no.: "))
    a.append(x)
print(a)

a.reverse()
print("reversed list: ", a)


# 4. WAP to print no. of occurences of a specified element in a list
a=[]
for i in range(5):
    x=int(input("enter no.: "))
    a.append(x)
print(a)
print(a.count(2))


# 5. WAP to append the items of list1 to list2 in the front
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
l1.reverse()
for i in range(len(l2)):
    l1.append(l2[i])
l1.reverse()
print(l1)


# 6. WAP to insert a new item before second element in an existing list
l1=[1,2,3,4,5]
l1.insert(1,6)
print(l1)


# 7. WAP to remove item from a specified index in a list
l1=[1,2,3,4,5]
l1.pop(1)
print(l1)


# 8. WAP to remove first occurence of a specified element from a list
l1=[1,2,2,4,5]
l1.remove(2)
print(l1)
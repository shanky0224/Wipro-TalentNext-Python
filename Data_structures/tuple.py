# 1. WAP to print 4th element from first and 4th element from last in tuple
tup = (1, 2, 3, 4, 5, 6)
print(tup[3])
print(tup[-4])

# 2. WAP to check whether an element exists in a tuple or not
tup = (1, 2, 3, 4, 5, 6)
val=int (input("enter element: "))
if val in tup:
    print(f"{val} exists in tuple")
else:
    print(f"{val} does not exist in tuple")


# 3. WAP to convert a list into a tuple
l1=[1,2,4,5,6]
tup=tuple(l1)
print(tup)


# 4. WAP to find index of an item in a tuple
tup = (1, 2, 3, 4, 5, 6)
val=int (input("enter element: "))
if val in tup:
    print(f"{val} exists in tuple at index {tup.index(val)}")
else:
    print(f"{val} does not exist in tuple")


# 5. WAP to replace value of tuples in a list to 100
#Sample list: [(10,20,40), (40,50,60), (70,80,90)]
#Expected O/p: [(10,20,100), (40,50,100), (70,80,100)]
l1=[(10,20,40), (40,50,60), (70,80,90)]
for i in range(len(l1)):
    temp=list(l1[i])
    temp[2]=100
    l1[i]=tuple(temp)
print(l1)
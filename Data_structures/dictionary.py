# 1. WAP to add a key and value to a dictionary
d={1:'A', 2:'B'}
d[3]='C'
print(d)


# 2. WAP to concatenate following dictionaries to create a new one
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)


# 3. WAP to check if a given key already exists in a dictionary
dic={1:'A', 2:'B', 3:'C'}
key=int(input("enter key to search: "))
if key in dic:
    print(f"{key} is present in dictionary")
else:
    print(f"{key} is not present in dictionary")


# 4. WAP to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values
dict1={1:'A', 2:'B', 3:'C'}
print("keys:")
for i in dict1.keys():
    print(i)

print("\nvalues:")
for i in dict1.values():
    print(i)

print("\nboth keys and values: ")
for key, value in dict1.items():
    print(key, value)


# 5. WAP to prepare a dictionary where the keys are nos. b/w 1 and 15 (both included) and the values are square of the keys
dict1={}
for i in range(1,16):
    dict1[i]=i**2
print(dict1)


# 6. WAP to sum all the values in a dictionary, considering the values wil be of int type
dict1={1:10, 2:20, 3:30}
sum=0
for i in dict1.values():
    sum+=i
print(sum)
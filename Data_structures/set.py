# 1. WAP to remove a given item from the set
s1={10, 'admin', 45, 'dev', 10.5, 12, 'user'}
print("Original set: ", s1)
s1.remove(10.5)
print(s1)


# 2. WAP to create an intersection of sets
s1={10, 'admin', 45, 'dev', 10.5, 12, 'user'}
s2={13, 'user', 12, 11, 'comp', 269, 'abc'}
ans=s1.intersection(s2)
print(f"intersection of {s1} and {s2}: {ans}")


# 3. WAP to create a union of sets
s1={10, 'admin', 45, 'dev', 10.5, 12, 'user'}
s2={13, 'user', 12, 11, 'comp', 269, 'abc'}
ans=s1.union(s2)
print(f"union of s1 and s2: {ans}")


# 4. WAP to find the max and min value in a set
s1={10, 18, 45, 269, 10, 12, 39}
print(f"max value in s1: {max(s1)}")
print(f"min value in s1: {min(s1)}")
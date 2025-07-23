'''
1. WAP to resd the entire content from a txt file and display
it to the user.
'''
with open('students.txt', 'r') as file:
    content = file.read()
    print(content)  


'''
2. WAP to read first n lines from a txt file. Get n as user input.
'''
n = int(input("Enter the number of lines to read: "))
with open('students.txt', 'r') as file:
    for i in range(n): 
        print(file.readline())


'''
3. WAP to accept input from user and append it to a text file
'''
with open('students.txt', 'a') as file:
    name = input("Enter text: ")
    file.write(name + "\n")


'''
4. WAP to read contents fro a text file line by line and store
each line into a list.
'''
lineList=[]
with open('students.txt', 'r') as file:
    lines=file.readlines()
    for i in range(len(lines)):
        lineList.append(lines[i].strip('\n'))
print(lineList)


'''
5. WAP to find longest word from the txt file contents, 
assuming that the file will have only one longest word in it.
'''
with open('students.txt', 'r') as file:
    content = file.read()
    words = content.split()
    longest_word = max(words, key=len)
    print(longest_word)



'''
6. WAP  to count the frequency of a user entered word in a txt file
'''
word = input("Enter the word to search: ")
with open('students.txt', 'r') as file:
    content = file.read()
    words = content.split()
    count = words.count(word)
    print(f"The word '{word}' appears {count} times in the file.")
    
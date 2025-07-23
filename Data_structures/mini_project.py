'''
1. Create a dictionary that contains a list of people and one interesting
fact about each of them. Display esach person and his or her interesting 
fact to the screen. Next, change a fact about one of the people. Also add 
an additional person and correspoding fact. Display the new list of people
and facts. Run the program multiple times and notice if the order changes.

Sample O/p:
Jeff: Is afraid of Dogs
David: Plays the piano
Jason: Can fly an airplane
'''
dic={}
dic['Jeff']='Is afraid of Dogs'
dic['David']='Plays the piano'
dic['Jason']='Can fly an airplane'

for key,value in dic.items():
    print(key,':',value)

dic['David']='Speaks German fluently'

dic['Emily']='Is a great dancer'
print('\nupdated list')
for key,value in dic.items():
    print(key,':',value)




'''
2. Given the participant's score sheet for your University Sport's Day, 
you are required to find the runner-up score. You have scores. Store
them in a list and find the score of the runner-up.

Sample I/p: [2,3,6,6,5]
O/p: 5
'''
sc=[]
for i in range(5):
    sc.append(int(input("Enter the score: ")))
    sc.sort()
scores=sc[::-1]
max_score=scores[0]
for score in scores:
    if score<max_score:
        runner_up=score
        break
print(f"Runner-up score: {runner_up}")






'''
3. You have a record of n students. Each record contains the student's
name, and their percent marks in Math, Physics and Chemistry. The 
marks can be floating values. You are required to save the record in a 
dictionary data type.

Student's name is the key. Marks stored in a list is the value. The 
user enters a student's name. Output average percentage marks obtained
by that student.
'''
student_records = {
    "Alice": [85.5, 90.0, 78.5],
    "Bob": [76.0, 82.5, 89.0],
    "Charlie": [92.0, 88.5, 94.0],
}

student_name = input("Enter student's name: ")

if student_name in student_records:
    marks = student_records[student_name]
    average = sum(marks) / len(marks)
    print(f"{student_name}'s average marks: {average:.2f}%")
else:
    print("Student not found in records.")





'''
4. Given a string of n words, help ALex to find out how many times his
name appears in the string.

Constraint: 1<=n<=200
Sample Input: Hi Alex WelcomeAlex Bye Alex.
Sample Output: 3
'''
string = input("Enter a string of words: ")
words = string.split()
name = "Alex"
count = 0

for word in words:
    if word == name:
        count += 1
print(f"Name '{name}' appears {count} times.")
'''
Project: 1
Create a python program that asks the user how far they want to travel. 
If they want to travel less than three miles tell them to ride Bicycle.
If they want to travel more than three miles but less than three hundred miles, 
tell them to ride Motor-Cycle. If they want travel three hundred miles or 
more tell them to drive Super-Car
'''
dis=int(input("How far would you like to travel in miles? "))
if dis<3:
    print("I suggest you ride a Bicycle")
elif dis>=3 or dis<300:
    print("I suggest you ride a Motor-Cycle")
elif dis>=300:
    print("I suggest you drive a Super-Car")




'''
Project: 2
Let's assume you are planning to use Python skills to build a PBLApp 
for Mobile. You decide to host your appllication on servers running
in the cloud. You pick a hosting provider that charges $0.51 per hour.
You will launch your service using one server and want to know how 
much it will cost to operate per day, per week, per month.

Write a python program that displays answers to following ques:
How much does ot cost to operate one server per day?
How much does it cost to operate one server per week?
How much does it cost to operate one server per month?
How many days can I operate one server with $918?
'''
hourly_cost = 0.51
server_per_day = 24 * hourly_cost
server_per_week = 7 * server_per_day
server_per_month = 30 * server_per_day
print(f"Cost to operate one server per day: ${server_per_day:.2f}")
print(f"Cost to operate one server per week: ${server_per_week:.2f}")
print(f"Cost to operate one server per month: ${server_per_month:.2f}")
print(f"With $918, you can operate one server for {918/server_per_day:.2f}")


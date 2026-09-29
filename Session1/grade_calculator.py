"""Write a program that:

Prompts the user to enter the total number of points possible for an assignment.
Prompts the user to enter the number of points earned.
Cast the user input to a numerical datatype
Calculates the resulting grade percentage: (points_earned / points_possible * 100)
Rounds the grade to two decimal places.
Prints the result to the console in the following format: "Your grade: 87.50%"""

print("Welcome to the grade calculator")
totalStr = input("Please enter the total number of points possible: ")
total = 0
while total == 0:
    try:
        total = float(totalStr)
    except ValueError:
        totalStr = input("Please enter a number: ")
    if total <= 0:
        total = 0
        totalStr = input("Please enter a positive number: ")

        
earnedStr = input("Please enter the total number of points earned: ")
earned = -1
while earned == -1:
    try:
        earned = float(earnedStr)
    except ValueError:
        earnedStr = input("Please enter a number: ")
    if earned < 0: #allows an entry of 0 points earned
        earned = -1
        earnedStr = input("Please enter a positive number: ")
    elif earned > total:
        earnedStr = input("Earned is greater than total. Enter 'y' to allow extra credit or enter the correct number otf earned points: ")
        if earnedStr.lower()!="y":
            earned = -1


percent = (earned/total)*100
rounded = round(percent,2)

print(f"Your grade: {percent:.2f}%")

if rounded >=90:
    grade = "A"
elif rounded >= 80:
    grade = "B"
elif rounded >= 70:
    grade = "C"
elif rounded >= 60:
    grade = "D"
else:
    grade = "F"

"""Write a program that:

Prompts the user to enter the total number of points possible for an assignment.
Prompts the user to enter the number of points earned.
Cast the user input to a numerical datatype
Calculates the resulting grade percentage: (points_earned / points_possible * 100)
Rounds the grade to two decimal places.
Prints the result to the console in the following format: "Your grade: 87.50%"""

print("Welcome to the grade calculator")
totalStr = input("Please enter the total number of points possible: ")
while not(totalStr.isnumeric()):
    print("That is not a number. Try again.")
    totalStr = input("Please enter the total number of points possible: ")
total = float(totalStr)

earnedStr = input("Please enter the total number of points earned: ")
while not(earnedStr.isnumeric()):
    print("That is not a number. Try again.")
    earnedStr = input("Please enter the total number of points earned: ")

earned = float(earnedStr)

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

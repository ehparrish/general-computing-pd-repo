"""Write a program that:

Prompts the user to enter the total number of points possible for an assignment.
Prompts the user to enter the number of points earned.
Cast the user input to a numerical datatype
Calculates the resulting grade percentage: (points_earned / points_possible * 100)
Rounds the grade to two decimal places.
Prints the result to the console in the following format: "Your grade: 87.50%"""

print("Welcome to the grade calculator")
totalStr = input("Please enter the total number of points possible: ")
earnedStr = input("Please enter the total number of points earned: ")

total = float(totalStr)
earned = float(earnedStr)

percent = (earned/total)*100
rounded = round(percent,2)

print("Your grade: "+str(rounded)+"%")

#Here is a change
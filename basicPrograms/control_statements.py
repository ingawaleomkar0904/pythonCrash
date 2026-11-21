
#--------------If statement----------------
"""
This is a simple program to demonstrate the use of if statement in python. The program checks the score of a 
student and prints the corresponding grade based on the score. The program also checks if the student has 
submitted the project or not. If the student has submitted the project and has scored 90 or above, it prints 
"Outstanding". If the student has scored between 80 and 89, it prints "Distinction". If the student has scored 
between 70 and 79, it prints "First Class". If the student has scored between 60 and 69, it prints "Second Class".
If the student has scored below 60, it does not print anything.   
"""
score = 100
submitted_project = True
if score >= 90:
    if(submitted_project):
        print("Outstanding")
    print("Excellent")
elif score >= 80:
    print("Distinction")
elif score >= 70:
    print("First Class")
elif score >= 60:
    print("Second Class")   


#--------------Match statement----------------
"""
This is a simple program to demonstrate the use of match statement in python. The program checks the
country variable and prints the corresponding message based on the value of the country variable. The program
also checks if the country variable is equal to "Austrelia", "India" or "USA". If the country variable is equal to "Austrelia",
it prints "Country is Austrelia". If the country variable is equal to "India", it prints "Country is India".
If the country variable is equal to "USA", it prints "Country is USA". If the country variable is not equal to 
any of these values, it does not print anything.
"""

country = "India"
match country:
    case "Austrelia":
        print("Country is Austrelia")
    case "India":
        print("Country is India")
    case "USA":
        print("Country is USA")

                

        
# ------------for loop--------------------------------------------------------------------------------------
# """
# for loop is used to iterate over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# """
# items = ["apple", "banana", "cherry"]
# for item in items:
#     print(f"value of i is {item}")


# #----------------------------------------------------------------------------------------------------------------

# name = "Anay"
# for char in name:
#     print(f"Character is {char}")
# #----------------------------------------------------------------------------------------------------------------

# scores = [40,50,70,80]
# total = 0

# for number in scores:
#     total += number
#     print(f"Addition of score is {total}")

# print(f"Total score is {total}")

# #----------------------------------------------------------------------------------------------------------------

# """
# This is a simple program to demonstrate the use of for loop in python. The program uses for loop to iterate over
# a range of numbers from 1 to 10 and prints the value of i
# """

# for i in range(1, 11):
#     print(f"Value of i is {i}")

# #----------------------------------------------------------------------------------------------------------------

# for x in range(10):
#     print(f"Square of {x} is {x * x}")

# squares = [ x * x for x in range(10)]
# print(f"Squares of numbers from 0 to 9 is {squares}")

#----------------------------------------------------------------------------------------------------------------

rows = input("Enter number of rows:")

for i in range(1, int(rows) + 1, 1):
    for j in range(1, i+1):
        print("*", end="")
    print("\n")

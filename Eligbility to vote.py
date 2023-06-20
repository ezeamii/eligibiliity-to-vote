# This program is to check whether a citizen is eligible to vote or not
print("----WELCOME TO NIGERIA'S VOTERS DATABASE----")
print("Please fill in the necessary information")


def spacing():
    print("---------------------------------------")


spacing()

fname = input("Please input your first name: ")
spacing()
lname = input("Please input your last name: ")
spacing()
gender = input("Please input your gender(M or F): ")
spacing()
state = input("In what state do you reside: ")
spacing()
age = int(input("Please input your age: "))


spacing()
if age < 18:
    print("Sorry", fname, "you are not eligible to vote in this year's presidential election"
                                 " for you are", age, "years old.")
else:
    print("Your details have been recorded and you are eligible to vote in"
          " this year's presidential election.")

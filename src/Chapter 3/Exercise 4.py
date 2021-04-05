# Age Input
user_age = input("Please input your age")
# Numeric input
try:
    verified_age = int(user_age)
    if verified_age >= 18:
        print("You can vote")
    elif 0 < verified_age <= 17:
        print("Too young to vote")
    elif verified_age < 0:
        print("You are a time traveller")
# error message
except:
    print("Error, please enter a numeric input")

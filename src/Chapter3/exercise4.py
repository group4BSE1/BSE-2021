age = input("enter age:")
try:
    age_input = int(age)
    if 18 < age_input:
        print("you can vote.")

    if 17 > age_input:
        print("too young to vote.")

        if 0 > age_input:
            print("you're a time traveller")

except:
    print("please enter integer value:")
# def
def computegrade(grade):
    if not(0.0 <= grade <= 1.0):
        print("Bad Score")
        exit()
    else:
        if grade >= 0.9:
            print("A")
# elif
        elif grade >= 0.8:
            print("B")
        elif grade >= 0.7:
            print("C")
        elif grade >= 0.6:
            print("D")
        else:
            print("F")


try:
    score = input("Please input your marks:\n")
    grade = float(score)
    computegrade(grade)
# Error message

except:
    print("please enter numeric input;")
    print("Bad score")
    exit()


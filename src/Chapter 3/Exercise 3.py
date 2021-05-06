# Prompt for a score
score = input("Please input your marks")
# Grading
try:
    grade = float(score)
    if grade >= 0.9:
        print("A")
    elif grade >= 0.8:
        print("B")
    elif grade >= 0.7:
        print("C")
    elif grade >= 0.6:
        print("D")
    elif grade < 0.6:
        print("F")
# Error message
except:
    print("Bad score")

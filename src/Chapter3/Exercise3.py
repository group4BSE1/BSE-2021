score = input("enter score:")
try:
    score_input = float(score)
    if 0 < score_input < 1.0:

        if score_input >= 0.9:
            print(score_input, "A")
        elif score_input >= 0.8:
            print(score_input, "B")
        elif score_input >= 0.7:
            print(score_input, "C")
        elif score_input >= 0.6:
            print(score_input, "D")
        elif score_input < 0.6:
            print(score_input, "F")
    else:
        print("Error, Out of range")


except:
    print("please enter float number")
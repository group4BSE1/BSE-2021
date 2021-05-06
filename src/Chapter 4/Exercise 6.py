def compute_pay(hours, rate):
    if hours <= 40:
        pay = rate * 40
    else:
        pay = ((hours - 40) * (1.5 * rate)) + (40 * rate)
    return pay


try:
    hrs = float(input('Enter Hours:\n'))
    rate = float(input('Enter Rate:\n'))
    print(compute_pay(hrs, rate))
except:
    print("Please enter numeric input")
    exit()


# Hours worked and rate
try:
    hrs = float(input('Enter Hours:\n'))
# rate
    rate = float(input('Enter Rate:\n'))
# Try and except
# print of hrs and rate
    print('Hours:', hrs)
    print('Rate:', rate)
# On 40 hours
    f = rate * 40
    print(f)
# Extra hours
    x = hrs-40
# 1.5 hourly rate
    y = float((x * 10) * 1.5)
    print(y)
# pay
    Pay = f+y
# print y
    print(Pay)
except:
    print("Error, please enter numeric input")
    try:
        hrs = float(input('EnterHours:\n'))
    except:
        print("Error, please enter numeric input")

finally:
    print('Done')
print('Done')

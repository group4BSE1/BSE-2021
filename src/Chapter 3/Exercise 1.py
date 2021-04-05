# Hours worked and rate
hrs = float(input('Hours: \n'))
print(hrs)
# rate
rate = float(input('Rate: \n'))
print(rate)
# On 40 hours
f = rate * 40
print(f)
# Extra hours
x = hrs-40
print(x)
# 1.5 hourly rate
y = float((x * 10) * 1.5)
print(y)
# pay
Pay = f+y
# print y
print(Pay)

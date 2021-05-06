c_init = int(input("Enter initial amount:"))

rate = float(input("Enter the rate:"))

yrs = int(input("Enter the no of years:"))

times = int(input("Enter the number of times:"))

# formula
# p = c(1 + r/n)^tn after round off to 2 decimal places

final = c_init * (1 + (rate/times)) ** (yrs*times)

print("The final value is:", final)

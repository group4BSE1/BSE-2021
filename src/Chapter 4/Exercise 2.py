# formula
# p = c(1 + r/n)^tn after round off to 2 decimal points
def investment(c, r, n, t):
    final_value = c * (1 + (r / t)) ** (t * n)
    return final_value

try:
    principal = int(input("Enter initial amount:\n"))
    rate = float(input("Enter the rate:\n"))
    years_t = int(input("Enter the no of years:\n"))
    times_n = int(input("Enter the number of times:\n"))
    amount = investment(principal, rate, years_t, times_n)
    print(f'Final amount of investment is: {amount:.2f}')
except:
    print("Please Input numeric value:")
    exit()

hours = input("enter hours:")
rate = input("enter rate:")
try:
    hour_exact = float(hours)

    rate_exact = float(rate)

    gross_pay = hour_exact * rate_exact

    print("Pay:", gross_pay)

except:
    print("Error, Please enter numeric input" )
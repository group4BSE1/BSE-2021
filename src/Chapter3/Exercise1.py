# prompt for the hours from the user
hours = float(input("Enter hours:"))

rate = float(input("Enter rate:"))

# check if the hours are greater than 40
# if the hours are > 40 we multiply the rate by 1.5 and use that new rate to compute the pay
if hours > 40:
    new_rate = rate * 1.5
    gross_pay = new_rate * hours
    print("Pay:", gross_pay)
else:
    gross_pay = hours * rate
    print("Pay:", gross_pay)
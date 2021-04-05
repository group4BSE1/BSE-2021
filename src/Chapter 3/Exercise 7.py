# location
location = input("Job Location:\n")
pay = input("Payment:\n")
# Prints For decisions
no = "No thanks,I can find something Better"
doubt = "Without a doubt I'll take it"
sure = "Sure, I can work with that"
no_way = "No way!"

# Try and Except
try:
    location = str(location)
    pay = float(pay)
except:
    print("Error, Invalid input")
# After Except
if location == "Mbarara":
    if pay == 4000000:
        print(no)
    else:
        if pay > 4000000:
            print(sure)
elif location == "Kampala":
    if pay == 10000000:
        print(no_way)
    else:
        if pay >= 10000000:
            print(sure)
elif location == "space":
    print(doubt)
else:
    if pay >= 6000000:
        print(sure)

# Input for Number of Guests
guest_number = input("Enter number of guests:\n")
# Check for numeric Input
try:
    guests = int(guest_number)
    if guests <= 50:
        print("It costs $4000")
    else:
        if guests <= 100:
            print("It costs $10000")
        else:
            if guests <= 200:
                print("It costs $15000")
            else:
                if guests > 200:
                    print("It will cost $20000")
# Error
except:
    print("Error, Please insert a numeric input")
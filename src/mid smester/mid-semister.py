# we prompt the user for the code.
# enters beginning meter reading
# Enters ending meter reading.
# we compute the gallons of water as a 10th of the gotten gallons.
# we print  out the bill meant to be paid the user

def bill_calculator(code, gallons):
    if code == "r":
        bill = 5.00 + (gallons * 0.0005)
        return round(bill, 2)
    elif code == "c":
        if gallons <= 4000000:
            bill = 1000.00
            return round(bill, 2)
        else:
            first_half = 1000.00
            sec_half = (gallons - 4000000) * 0.00025
            summed_bill = first_half + sec_half
            return round(summed_bill, 2)
    elif code == "i":
        if gallons <= 10000000:
            bill = 1000.00
            return round(bill, 2)
        elif 4000000 < gallons < 10000000:
            bill = 2000.00
            return round(bill, 2)
        elif gallons > 10000000:
            first_half = 2000.00
            sec_half = (gallons - 10000000) * 0.00025
            summed_bill = first_half + sec_half
            return round(summed_bill, 2)



while True:
    # promp the user for the code.
    list_codes = ['r', 'c', 'i']

    customer_code = input("\nEnter customer  code:")

    if len(customer_code) > 0 and customer_code.lower() in list_codes:

        cus_code = customer_code.lower()
        begin_exact = 0
        end_exact = 0
        while True:
            begin_r = input("\nEnter Beginning meter reading:")
            if len(begin_r) > 0 and begin_r.isnumeric() and 0 < int(begin_r) < 999999999:
                begin_exact = int(begin_r)
                break
            else:
                print("Enter valid input or meter reading!")
                continue
        while True:
            end_r = input("\nEnter End meter reading:")
            if len(end_r) > 0 and end_r.isnumeric() and 0 < int(end_r) < 999999999:
                end_exact = int(end_r)
                break
            else:
                print("Enter valid input or meter reading!")
                continue

        gallons = (end_exact - begin_exact) / 10

        customer_bill = bill_calculator(cus_code, gallons)

        print("\nCustomer Code:", cus_code)
        print("Beginning meter reading:", begin_exact)
        print("Ending meter reading:", end_exact)
        print("Gallons of water used:", str(gallons))
        print("Amount billed:$" + str(customer_bill))





    else:
        print("Please enter a valid customer code!")
        continue





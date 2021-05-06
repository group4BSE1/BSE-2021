while True:
    # promp the user for the code.
    list_codes = ['r', 'c', 'i']

    customer_code = input("\nEnter customer  code:")

    if len(customer_code) > 0 and customer_code.lower() in list_codes:

        cus_code = customer_code.lower()
        print("Customer code:", cus_code)
    else:
        continue
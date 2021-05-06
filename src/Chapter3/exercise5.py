people = input("enter people:")
try:
    people_input = int(people)
    if people_input <= 50:
        print(people, "$4000")

        if people_input <= 100:
            print(people, "$10000")

            if people_input <= 200:
                print(people_input, "$15000")

                if people_input > 200:
                    print(people, "$20000")
except:
    print("error")
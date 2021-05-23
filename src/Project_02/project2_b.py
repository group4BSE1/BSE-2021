def open_file():
    while True:
        file = input('Enter input file:  ')
        if file == "measles.txt":
            return file
        else:
            print("File should be \"measles.txt\"")
            continue


def ref(income):
    if income == 1:
        income = "WB_LI"
        return income
    elif income == 2:
        income = "WB_LMI"
        return income
    elif income == 3:
        income = "WB_UMI"
        return income
    elif income == 4:
        income = "WB_HI"
        return income
    else:
        print("Invalid income!!!")

while True:
    try:
        file = open_file()
        year = int(input('Enter year:'))
        year = str(year)
        income = int(input('Enter income level:'))
        income2 = ref(income)
        measles = open(file, 'r')
        count = 0
        add = 0
        lowest = 99
        highest = 0
        for line in measles:
            if (income2 in line[51:57]) and (year == line[88:92]):
                child = line[59:62]
                child2 = int(child)
                if child2 > highest:
                    highest = child2
                if child2 < lowest:
                    lowest = child2
                add += child2
                count += 1
        average = add/count
        print("Lowest percentage =", lowest)
        print("Highest percentage =", highest)
        print("Average percentage =", average)
        print("Success!!")
        break
    except:
        print("Error!! , Invalid Input!!")
        continue

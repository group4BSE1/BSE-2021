# the program prompts the user to enter numbers
# it stores the numbers in the list then calculate the max and min number in the list

list = []
number = 0
while True:
    x = input("Enter a number: ")
    print(x.lower())
    if x == 'done':
        print("its done")
        break

    else:
        try:
            number = float(x)
            list.append(x)

        except ValueError:
            print("Invalid input, this is not a number !!!!")


print(f'Minimum number: {min(list)}, Maximum number: {max(list)}')

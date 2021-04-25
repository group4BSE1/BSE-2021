count = 0
total = 0
while True:
    Enter = input('Enter a number:\n')
    try:
        if Enter == "Done":
            break
        else:
            inp = int(Enter)
            total = total + inp
            count = count + 1
            average = total / count
    except:
        print('Invalid input')
print('Total:', total, 'Count:', count, 'Average:', average)

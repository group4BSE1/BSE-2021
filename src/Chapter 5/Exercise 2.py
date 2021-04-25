largest = None
smallest = None
while True:
    Enter = input('Enter a number:\n')
    if Enter == 'Done':
        break
    elif largest is None or Enter > largest:
        largest = Enter
    elif smallest is None or Enter < smallest:
        smallest = Enter
print('Maximum:\n', largest)
print('Minimum:\n', smallest)

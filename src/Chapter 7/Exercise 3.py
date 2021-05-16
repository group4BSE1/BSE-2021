# files in existence
file = input('Enter the file name: ')
try:
    file_handle = open(file, 'r')
    count = 0
    for line in file_handle:
        count = count + 1
    print('There were', count, 'lines in', file)
except:
    if file == 'na na boo boo':
        print('NA NA BOO BOO TO YOU -You have been punk, ink\'d!')
    else:
        print('file cannot be opened', file)

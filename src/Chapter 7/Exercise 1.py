# mbox-short.txt
file = input('Enter a file name: ')
try:
    handle = open(file, 'r')
except:
    print('File cant be opened, probably missing')
    exit()
read_file = handle.read()
print(read_file.upper())

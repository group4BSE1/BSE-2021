file_name = input('Enter the file name:  ')
try:
    file_update = open(file_name)

except:
    print('Invalid file name')
    file_update = None
    quit()
unique = []
# reading lines in the file
for line in file_update:
    words = line.split()
# reading each line to split it>>> words
    for each in words:
        exact = each.split()
        unique.append(each)
# list of unique words
unique.sort()
print(unique)
# romeo.txt

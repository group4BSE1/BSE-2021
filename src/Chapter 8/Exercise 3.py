# using logical operator eliminating use of two ifs
text = input("Enter the file name: ")
file = open(text)
for line in file:
    words = line.split()
    if len(words) < 3 or words[0] != "From":
        continue
    print(words[2])
# mbox.txt

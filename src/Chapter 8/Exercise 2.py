text = input("Enter file name: ")
file = open(text)

for line in file:
    words = line.split()
    if len(words) < 3:
        continue
    if words[0] != "From":
        continue
    print(words[2])
# mbox.txt & mbox-short.txt

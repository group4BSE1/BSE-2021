# prompts the user to enter to file path and the executes it
text = input("Enter the file name: ")
file = open(text)
count = 0
for line in file:
    words = line.split()
    if len(words) < 3:
        continue
    if words[0] != "From":
        continue
    print(words[2])
    count = count + 1
print(f"there were {count}")

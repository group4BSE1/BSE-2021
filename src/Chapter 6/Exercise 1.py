# Program that works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.
word_txt = input("Enter a text:\n")
length = len(word_txt)
index = 0
while length > index:
    length = length - 1
    print(word_txt[length])
# Done

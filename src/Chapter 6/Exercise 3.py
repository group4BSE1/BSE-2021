txt_word = input("Enter a text:\n").lower()
character = input("Enter letter to find its number of times:\n").lower()
# def
# making a count of a letter in word


def count(txt_word, character):
    count_w = 0
    for letter in txt_word:
        if letter == character:
            count_w = count_w + 1
    print(count_w)


count(txt_word, character)

print("Looping and counting\nExercise 4")
txt_word = input("Enter a text:").lower()
character = input("Enter letter to find its number of times:").lower()
# def
# making a count of a letter in word


def count(text_word, character_s):
    count_wst = 0
    for text in text_word:
        if text == character_s:
            count_wst = count_wst + 1
            # break gives a zero print
            continue
    print(count_wst)


count(txt_word, character)

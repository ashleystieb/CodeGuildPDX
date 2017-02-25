def main():
    words = str(input("Input Sentence:")).split(" ")
    new_words = []
    for word in words:
        if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
            new_words.append(word[1:] + word[0] + 'yay')
        elif word[0] == "A" or word[0] == "E" or word[0] == "I" or word[0] == "O" or word[0] == "U":
            new_words.append(word[1:] + word[0] + 'yay')
        else:
            new_words.append(word[1:] + word[0] + 'ay')
    print(" ".join(new_words))


main()
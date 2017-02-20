def translate(word):
    '''
    >>> translate("hello")
    'ellohay'
    >>> translate("Apple")
    'ppleAay'
    '''
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
        return word[1:] + word[0] + 'yay'
    if word[0] == "A" or word[0] == "E" or word[0] == "I" or word[0] == "O" or word[0] == "U":
        return word[1:] + word[0] + 'yay'
    else:
        return word[1:] + word[0] + 'ay'

def main():
    user_word = input("Enter a word to convert to pig latin: ").lower()
    print(translate(user_word))

main()

if __name__ == '__main__':
    import doctest

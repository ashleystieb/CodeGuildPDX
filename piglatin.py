def translate(word):
    '''
    >>> translate("hello")
    'ellohay'
    >>> translate("Apple")
    'ppleAay'
    '''
    if word[0] is "aeiou":
        return word[1:] + word[0] + 'yay'
    if word[0] is "AEIOU":
        return word[1:] + word[0] + 'yay'
    else:
        return word[1:] + word[0] + 'ay'

def main():
    user_word = input("Enter a word to convert to pig latin: ").lower()
    print(translate(user_word))

main()

if __name__ == '__main__':
    import doctest

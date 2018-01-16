def camelcase(word):
    ''' Convert word to have uppercase first letter, rest in lowercase'''
    return word[0:1].upper() + word[1:].lower()
    # Slices don't produce index out of bounds errors.
    # So this still works on empty strings, strings of length 1

def display_banner():
    '''Display program name in a banner'''
    msg = 'AWESOME camelCaseGenerator PROGRAM'
    stars = '*' * len(msg)
    print('\n', stars, '\n', msg, '\n', stars, '\n')

def main():

    display_banner()

    sentence = input('Enter your sentence:  ')
    words = sentence.split(' ')                               # Break by spaces
    camelcased_words = [ camelcase(word) for word in words ]  # camelCase everything
    camelcased_words[0] = camelcased_words[0].lower()         # Lowercase first word
    output = ''.join(camelcased_words)                        # Put words back together
    print(output)


if __name__ == '__main__':
    main()

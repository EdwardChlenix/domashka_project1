def upper():
    word = input("Введите слово")
    print(word.upper())

def capitalineachword():
    s = input("Введите строку")
    words = s.split()
    result = ' '.join(word.capitalize() for word in words)
    print(result)

'''
Docstring for second function
'''
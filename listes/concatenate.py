#, affichez les "mots" : aa, ab, ac, ba, bb, bc, ca, cb, cc

ab = ['a', 'b', 'c']
textToRender = ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']

def makeTextFromVar(alphabet:list, textToRender:list):
    textResult = ""
    for text in textToRender: # pour chaque élément dans la liste textToRender
        for i in range(len(text)): # pour la longueur du texte
            char = text[0:i] # récupérer la lettre à i
            print(i)
            for letter in alphabet:
                if letter == char:
                    textResult = textResult+letter
        print(textResult)

makeTextFromVar(ab, textToRender)

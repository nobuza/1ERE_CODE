def alphabet_position(text):
    bannedChars = ["", "'", ".", ",", ";", "/"]
    indexes = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lettersList = [ch for ch in text]
    print(lettersList)
    for i in range(len(lettersList)):
        for n in range(len(alphabet)):
            for char in bannedChars:
                if lettersList[n] == char:
                    pass
                else:
                    continue
                print(n, ":", alphabet[n],i,":", lettersList[i])
                if alphabet[n] == lettersList[i]:
                    indexes.append(n)
                    pass
            else:
                pass
    return indexes


print(alphabet_position("The sunset sets at twelve o' clock."))
# ANSWER:  "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")

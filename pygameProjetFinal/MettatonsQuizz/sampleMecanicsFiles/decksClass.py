import csv

# csv header
fieldnames = ["question", "correctAnswer", "wrongAnswer1", "wrongAnswer2", "wrongAnswer3"]

# csv data
rows = []

'''
# VISUAL OF A CARD IN DECK
rows = [
    {"question": "ARPANET",
    "correctAnswer": "1er réseau distant en 1968",
    "wrongAnswer1": "noot", 
    "wrongAnswer2": "noot", 
    "wrongAnswer3": "noot"},
]
'''


def renderDeck(deckName):
    deckNameWithCsvExtension = "{}.csv".format(deckName)
    with open(deckNameWithCsvExtension, "w", encoding="UTF8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def addCards():
    continueLooping = True


    while continueLooping:
        dictToAppend = {}

        dictToAppend.clear()
        inputText = input("Enter the question of the card\n>")

        if inputText == "rendernow":
            continueLooping = False
            renderDeck()
        else:
            dictToAppend["question"] = inputText

            # correct answer
            inputText = input("Enter the correct answer to the question of the card\n>")
            dictToAppend["correctAnswer"] = inputText

            # 1st wrong answer
            inputText = input("Enter the first wrong answer to the question of the card\n>")
            dictToAppend["wrongAnswer1"] = inputText

            # 2nd wrong answer
            inputText = input("Enter the second wrong answer to the question of the card.\n>")
            dictToAppend["wrongAnswer2"] = inputText

            # 3rd wrong answer
            inputText = input("Enter the third wrong answer to the question of the card.\n>")
            dictToAppend["wrongAnswer3"] = inputText

            inputText = input("Type 'c' to make a new card, or 'r' to render the deck and exit the program.\n>")
            if inputText == "c":
                continueLooping = False
                rows.append(dictToAppend)

                deckName = input("Enter the deck's name.\n>")
                renderDeck(deckName)
            else:
                rows.append(dictToAppend)

addCards()
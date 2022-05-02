'''
CONSIGNE:
Ecrire un algorithme Python, qui à partir de 3 boucles bornées imbriquées et de la fonction sleep(n) qui 
permet d'attendre/faire une pause de n seconde(s), qui crée un minuteur de 1 heure.
'''

import string
import time

#################################################################
'''
1 hour clock V1
- V1.0
- No GUI, no visuals, just a simple print for each second.
'''
#################################################################
def timer():
    for hour in range(0, 1):
        for minute in range(0, 60):
            for second in range(0, 60):
                time.sleep(1)
                print("sleeping for one second")

#timer()


#################################################################
'''
1 hour clock V2
- No GUI, no visuals, just a simple print for each second.
'''
#################################################################
def oneHourClockWithDecimalCountingUsingOnlyASingleVariable():
    timeCounted = 0
    '''
    We will use the following format:
    0, the first unit, corresponds to the hours
    0.00, the two first decimals, corresponds to the minutes
    0,0000, the two last numbers will correspond to seconds
    '''

    for hour in range(0, 1):
        for minute in range(0, 60):
            for second in range(0, 60):
                time.sleep(1)
                timeCounted = timeCounted + 0.0001
                print(timeCounted)

#oneHourClockWithDecimalCounting()

'''
But computers DO SUCK AT FLOATING POINT NUMBERS.
We'll go for another format.
'''

#################################################################
'''
1 hour clock V2.2
- Basic clock visual output
'''
#################################################################
def oneHourClockUsingMultipleVariables():
    hours = 0
    minutes = 0
    seconds = 0

    for hour in range(0, 1):
        for minute in range(0, 60):
            for second in range(0, 60):
                time.sleep(1)
                seconds = seconds +1
                if seconds == 60:
                    seconds = 0
                    minutes = minutes + 1
                    if minutes == 60:
                        hour = hour + 1
                print(hours,":",minutes,":",seconds)

oneHourClockUsingMultipleVariables()
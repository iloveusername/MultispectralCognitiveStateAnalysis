# Steps:
# Ask user for gamemode, either baseline or flow.
# Users have 15 seconds to put in their answer.
# Baseline will be kept at 3 numbers, all being one digit long.
# Flow will scale based on how well you are performing.
# Level = 1 + round(numCorrect / 4).
# 
# [1 1 1] [2 1 1] [2 2 1] [2 2 2] [3 2 2] [3 3 2] [3 3 3] [4 3 3] [4 4 3] [4 4 4]...
#
# On level up, compare first value with second. If not equal, increase second value by one. 
# If Equal, check first value with third. If not equal, increase third value by one. 
# If Equal, increase first value by one.

import math
import random
from time import time

scaleGamemode = False
diff = [1, 1, 1]

while True:
    inp = input("Enter Gamemode (B or F): ").upper()

    if inp != 'B' and inp != 'F':
        print("Invalid Choice, Try Again...")
        continue
    
    if inp == 'B':
        break

    if inp == 'F':
        scaleGamemode = True
        diff = [2, 2, 1]
        break


numCorrect = 1
prevLevel = 1

numQuestions = 500

print(scaleGamemode)

for x in range(numQuestions):
    if scaleGamemode:
        firstVar = random.randrange(10**diff[0])
        secondVar = random.randrange(10**diff[1])
        thirdVar = random.randrange(10**diff[2])

        ans = firstVar + secondVar + thirdVar

        startTime = time()
        try:
            userInp = int(input(f'{firstVar} + {secondVar} + {thirdVar} =\n'))
        except Exception as e:
            userInp = 0
        print('\n')

        if userInp == ans and (time() - startTime) < 18:
            numCorrect += 1
        else:
            numCorrect -= 1
        
        if numCorrect < 1:
            numCorrect = 1
    
        currentLevel = 1 + math.floor(numCorrect/4)

        if currentLevel > prevLevel:
            if diff[0] == diff[1]:
                if diff[0] == diff[2]:
                    diff[0] += 1
                else:
                    diff[2] += 1
            else:
                diff[1] += 1
            prevLevel = currentLevel
        if currentLevel < prevLevel:
            if diff[0] == diff[2]:
                diff[2] -= 1
            else:
                if diff[0] == diff[1]:
                    diff[1] -= 1
                else:
                    diff[0] -= 1
            prevLevel = currentLevel
    
    else:
        firstVar = random.randrange(10**diff[0])
        secondVar = random.randrange(10**diff[1])
            
        ans = firstVar + secondVar

        try:
            userInp = int(input(f'{firstVar} + {secondVar} =\n'))
        except Exception as e:
            userInp = 0
        print('\n')
import os.path
import random


haveItem = False
haveKey = False
havePotion = False
win = True
persuaded = False 
considered = False


#opening scenario
scenario = 'scenario.txt'
infile = open(scenario, 'r')    
outputFile = infile.read()
print(outputFile)

#opening setting off
settingoff = 'settingoff.txt'
infile = open(settingoff, 'r')    
outputFile = infile.read()
print(outputFile)

while win != False:
    #first encounter
    isInt = False

    while isInt != True:
        print('What would you like to do?')
        userInput = input('Would you like to open the door (1) or flee (2)?: ')

        #validating
        try:
            convertInt = int (userInput)
            if convertInt>2:
                print('invalid. try again')
            else:
                isInt = True

        except:
            print('invalid. try again')

    #fleeing
    if convertInt == 2:
        print ('you flee')
        win = False

    #entering 2
    else:
        timeloop = True
        while timeloop == True:
            descriptionroom = 'descriptionroom.txt'
            infile = open(descriptionroom, 'r')    
            outputFile = infile.read()
            print(outputFile)

            inRoom = True
            while inRoom == True:
                    isInt = False
                    while isInt != True:
                        print('What would you like to do?')
                        userInput = input('Would you like to search the table (1), enter the left door (2), or enter the right door(3)?: ')

                    #validating
                        try:
                            convertInt = int (userInput)
                            if convertInt>3:
                                print('invalid. try again')
                            else:
                                isInt = True

                        except:
                            print('invalid. try again')

                    #gaining item
                    if convertInt == 1:
                        if haveItem != True:
                            tabledescription = 'tabledescription.txt'
                            infile = open(tabledescription, 'r')    
                            outputFile = infile.read()
                            print(outputFile)
                            print('you gain +1 dagger of oblivion\n')
                            haveItem = True
                        else:
                            print('you have searched the table all you can\n')
                                
                    #entering kitchen
                    elif convertInt == 2:
                        inRoom = False
                        inKitchen = True
                        
                        print('you enter the left door. It leads to a kitchen')
                        descriptionkitchen = 'descriptionkitchen.txt'
                        infile = open(descriptionkitchen, 'r')    
                        outputFile = infile.read()
                        print(outputFile)

                        while inKitchen == True:            
                            isInt = False
                            while isInt != True:
                                print('What would you like to do?')
                                userInput = input('Would you like to search the room (1), exit (2), or go down the stairs (3)?: ')
                                #validating
                                try:
                                    convertInt = int (userInput)
                                    if convertInt>4:
                                        print('invalid. try again')
                                    else:
                                        isInt = True

                                except:
                                    print('invalid. try again')

                            #searching        
                            if convertInt == 1:
                                print('you search the room. there is nothing there.\n')
                            #exiting    
                            elif convertInt == 2:
                                print('you exit the room.') 
                                inKitchen = False
                            #stairs
                            elif convertInt == 3:
                                inKitchen = False
                                inBasement = True
                                print('\nyou go down the stairs')
                                descriptionbasement = 'descriptionbasement.txt'
                                infile = open(descriptionbasement, 'r')    
                                outputFile = infile.read()
                                print(outputFile)

                                #encountering Gryla
                                while inBasement == True:
                                    print('What would you like to do?')
                                    userInput = input('Would you like to attack (1), persuade Gryla (2), consider Gryla more carefully (3), or flee (4)?: ')
                                    #validating
                                    try:
                                        convertInt = int (userInput)
                                        if convertInt>4:
                                            print('invalid. try again')
                                        else:
                                            isInt = True

                                    except:
                                        print('invalid. try again')

                                    considered = False    

                                    #gryla moment
                                    key = 'key.txt'
                                    infile = open(key, 'r')    
                                    outputFile = infile.read()
 
                                    #attacking    
                                    attackWin = False
                                    numIncrease = 1
                                    grylaIncrese = 1
                                    if convertInt == 1:
                                        print('\nyou attack')
                                        while numIncrease <= 2:
                                            #user roll
                                            userRoll = random.randrange(int(20))+1
                                            if haveItem == True:
                                                userFinal = userRoll + 1
                                            else:
                                                userFinal = userRoll
                                            print('You roll a', userFinal)
                                            if userRoll >= 12:
                                                numIncrease += 1
                                                print('you hit!\n')
                                                if userRoll == 20:
                                                    print('Its a critical hit! gryla dissapears')
                                                    print(outputFile)
                                                    haveKey = True
                                                    inBasement = False
                                                    numIncrease = 4
                                            else:
                                                print('you miss!\n')  
                                            #gryla roll
                                            grylaRoll = random.randrange(int(20))+1
                                            grylaFinal= grylaRoll - 4
                                            if grylaFinal <= 0:
                                                print('gryla rolls a 1')
                                            else:    
                                                print('gryla rolls a', grylaFinal)
                                            if grylaFinal >= 12:
                                                print('gryla hits!\n')
                                                grylaIncrese += 1
                                                if grylaIncrese >= 3:
                                                    print('you are hit one last time. gryla prevails over you')
                                                    win = False
                                            else:
                                                print('gryla misses!\n')   
                                        print('You win! gyla dissapears')  
                                        print(outputFile)
                                        inBasement = False       
                                                   


         
                                    #persuading    
                                    elif convertInt == 2:
                                        print('you attempt to persuade Gryla')
                                        if persuaded == False:
                                            #user roll
                                            userRoll = random.randrange(int(20))+1
                                            if haveItem == True:
                                                userFinal = userRoll +1
                                            else:
                                                userFinal = userRoll
                                            #gyrla roll
                                            grylaRoll = random.randrange(int(20))+1
                                            grylaFinal = grylaRoll + 4
                                            if userFinal > grylaFinal: #checking for crit USING IF
                                                haveKey = True
                                                print('Your persuasion works! You are not scared of Gryla. She dissapears!')
                                                print(outputFile)
                                                inBasement = False
                                            else:
                                                print('your persuasion did not work\n')    
                                            persuaded = True
                                        else:
                                            print('you cannot do this again.\n')                                                   
                                    #considering    
                                    elif convertInt == 3:
                                        print('you consider Gyla more carefully')
                                        if considered == False:
                                            #user roll
                                            userRoll = random.randrange(int(20))+1
                                            if haveItem == True:
                                                userFinal = userRoll +1
                                            else:
                                                userFinal = userRoll
                                            #gyrla roll
                                            grylaRoll = random.randrange(int(20))+1
                                            grylaFinal = grylaRoll - 2
                                            if userFinal > grylaFinal: #checking for crit USING IF
                                                haveKey = True
                                                print('You discover Gryla is cursed. You can cure her.')
                                                print(outputFile)
                                                inBasement = False
                                            else:
                                                print('you discover nothing\n')    
                                            considered = True
                                        else:
                                            print('you cannot do this again\n.')


                                    #fleeing    
                                    elif convertInt == 4:
                                        print('you flee')
                                        win = False           

                

                    #entering bedroom
                    elif convertInt == 3:
                        inRoom = False
                        inBedroom = True
                        print('You enter the right door. It leads to a bedroom.')
                        descriptionbedroom = 'descriptionbedroom.txt'
                        infile = open(descriptionbedroom, 'r')    
                        outputFile = infile.read()
                        print(outputFile)

                        while inBedroom == True:            
                            isInt = False
                            while isInt != True:
                                print('What would you like to do?')
                                userInput = input('Would you like to search the room (1), exit (2), or open the chest (3)?: ')
                                #validating
                                try:
                                    convertInt = int (userInput)
                                    if convertInt>4:
                                        print('invalid. try again')
                                    else:
                                        isInt = True
                                except:
                                    print('invalid. try again')

                            #searching        
                            if convertInt == 1:
                                print('you search the room. there is nothing there.\n')
                            #exiting    
                            elif convertInt == 2:
                                print('you exit the room')
                                inBedroom = False
                            #opening chest
                            elif convertInt == 3:
                                if havePotion == False:
                                    print('you approach the dusty chest and attempt to open it')
                                    if haveKey == False:
                                        print('nothing happens')
                                    else:
                                        potion = 'potion.txt'
                                        infile = open(potion, 'r')    
                                        outputFile = infile.read()
                                        print(outputFile)
                                        print('you recieve +1 Potion of Protection')
                                        win = True
                                else:
                                    print('there is nothing left in the chest')

if win == False:
    print('Game over. You lose')
else:
    print('Game over. You win!')
    win = 'win.txt'
    infile = open(win, 'r')    
    outputFile = infile.read()
    print(outputFile)    
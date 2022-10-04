import random
from copy import deepcopy

Letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#The values of the 5 rotors. These were generated randomly using the function enigmaGenerateRandomVals. These were kept standard, but three of them were chosen at random, and in a random order.
Rotors= [[[0, 3], [1, 7], [2, 21], [3, 10], [4, 25], [5, 15], [6, 12], [7, 13], [8, 19], [9, 1], [10, 8], [11, 22], [12, 23], [13, 16], [14, 5], [15, 0], [16, 24], [17, 17], [18, 11], [19, 2], [20, 20], [21, 6], [22, 9], [23, 18], [24, 14], [25, 4]], [[0, 6], [1, 0], [2, 7], [3, 23], [4, 8], [5, 17], [6, 11], [7, 4], [8, 20], [9, 22], [10, 5], [11, 1], [12, 25], [13, 10], [14, 21], [15, 19], [16, 18], [17, 3], [18, 24], [19, 16], [20, 12], [21, 13], [22, 9], [23, 2], [24, 15], [25, 14]], [[0, 18], [1, 16], [2, 1], [3, 19], [4, 2], [5, 25], [6, 21], [7, 14], [8, 0], [9, 23], [10, 9], [11, 7], [12, 11], [13, 8], [14, 13], [15, 20], [16, 24], [17, 15], [18, 5], [19, 17], [20, 10], [21, 22], [22, 12], [23, 3], [24, 6], [25, 4]], [[0, 10], [1, 6], [2, 13], [3, 25], [4, 19], [5, 12], [6, 1], [7, 15], [8, 24], [9, 11], [10, 18], [11, 4], [12, 21], [13, 5], [14, 22], [15, 17], [16, 14], [17, 23], [18, 9], [19, 16], [20, 3], [21, 2], [22, 0], [23, 7], [24, 8], [25, 20]], [[0, 4], [1, 16], [2, 25], [3, 13], [4, 18], [5, 5], [6, 19], [7, 15], [8, 10], [9, 1], [10, 12], [11, 6], [12, 23], [13, 20], [14, 7], [15, 17], [16, 24], [17, 0], [18, 14], [19, 3], [20, 2], [21, 22], [22, 8], [23, 21], [24, 9], [25, 11]]]

#The values of the 5 rotors. These were generated randomly using the function enigmaGenerateRandomVals. They were kept constant
Reflector = [[24, 8], [12, 16], [7, 0], [15, 21], [11, 17], [1, 10], [9, 6], [5, 14], [22, 4], [13, 25], [19, 3], [18, 2], [23, 20]]




#These values are not known
Plugboard= [[6, 24], [10, 12], [13, 23], [17, 9], [8, 2], [19, 16], [15, 7], [18, 21], [5, 11], [22, 4]]

#These values are not known and need to be found
#[order of rotors, position of each rotor, manual adjusment to each rotor]
rotorValues=[[3,1,4],[2,16,21],[0,0,0]]









def randomizePlugBoard(pairs):
  boardPairs=list()
  numbersSeen=list()
  for letNum in range(0,pairs):
    while(1):
      ranNum1=random.randint(0,25)
      ranNum2=random.randint(0,25)
      if (ranNum1 not in numbersSeen) and (ranNum2 not in numbersSeen) and (ranNum1!=ranNum2):
        numbersSeen.append(ranNum1)
        numbersSeen.append(ranNum2)
        entry=[ranNum1,ranNum2]
        boardPairs.append(entry)
        break
        
  return boardPairs

#Randomize a rotor. Create 26 unique pairs of numbers fomr 0 to 26, each number representing a letter
def randomizeRotor():
  rotorPairs=list()
  numbersSeen=list()
  for letNum in range(0,len(Letters)):
    while(1):
      ranNum=random.randint(0,25)
      if ranNum not in numbersSeen:
        numbersSeen.append(ranNum)
        entry=[letNum,ranNum]
        rotorPairs.append(entry)
        break
      
  return rotorPairs
  
def chooseRotorOrder():
  order=list()
  for i in range(0,3):
    while True:
      ranNum=random.randint(0,4)
      if ranNum not in order:
        order.append(ranNum)
        break
        
  return order
  
def applyMovement(rotors,movement):
  #Loop through the movement list. Each entry represents how many positions each rotor should be manually moved. i.e. rotor1=[[0,16],[1,2],...,[25,8]] and movement=[1,0,0] then rotor1=[[0,8],[1,16],...]
    
  newRotors=deepcopy(rotors)
  for i in range(0,len(movement)):
    spacesToMove=movement[i]
    #print spacesToMove
    if spacesToMove!=0: #If movement is specified
      for j in range(0,len(rotors[i])):

        if (j+spacesToMove)>=0 and (j+spacesToMove)<=25:
          newRotors[i][j][1] = rotors[i][j+spacesToMove][1]
        elif j+spacesToMove>25 :
          newRotors[i][j][1] = rotors[i][j+spacesToMove-26][1]
        elif j+spacesToMove<0:
          newRotors[i][j][1] = rotors[i][j+spacesToMove+26][1]

  return newRotors
        
        
#The difference between the rotors and the reflector, is that in the reflector, we can't map a letter to itself. That is why in the if statement we include the "and (ranNum != letNum)" part
def randomizeReflector():
  reflectorPairs=list()
  numbersSeen=list()
  for letNum in range(0,13):
    while(1):
      ranNum1=random.randint(0,25)
      ranNum2=random.randint(0,25)
      if (ranNum1 not in numbersSeen) and (ranNum2 not in numbersSeen) and (ranNum1!=ranNum2):
        numbersSeen.append(ranNum1)
        numbersSeen.append(ranNum2)
        entry=[ranNum1,ranNum2]
        reflectorPairs.append(entry)
        break
      
  return reflectorPairs
  


def enigmaGenerateRandomVals(plugPairs):

  if plugPairs <0 or plugPairs >10:
    print "Please enter a number between 0 and ten, to specify the number of pairs on the plibboard"
    exit(0)

  #------Create Plugboard------
  #Create plugoard. Create up to 10 pairs of letter indices. An index cannot be paired with itself. An index cannot appear twice in all pairs
  plugboard=randomizePlugBoard(plugPairs)
  #----------------------------
  
  
  
  #------Create the 3 rotor wheels------
  #Create 5 rotors where each letter index(0-25) randomly assigns to another. An index can be paired with itself.
  rotor1=randomizeRotor()
  rotor2=randomizeRotor()
  rotor3=randomizeRotor()
  rotor4=randomizeRotor()
  rotor5=randomizeRotor()
  allRotors=[rotor1,rotor2,rotor3,rotor4,rotor5]
  
  #Randomly choose 3 out of the 5 rotors, and place them in a random order
  rotorsOrder=chooseRotorOrder()
  randomThreeRotors=[allRotors[rotorsOrder[0]],allRotors[rotorsOrder[1]],allRotors[rotorsOrder[2]]]
    
  #Apply manual movement to the rotors, i.e. move rotor 1, 2 positions to the right and rotor 2, -2 positions (2 positions to the left).
  rotorMovement=[1,-2,0]
  rotors=applyMovement(randomThreeRotors,rotorMovement)
  #-------------------------------------
  
  
  
  #------Create the reflector/scrambler------
  #Create the reflector. Create 13 pairs of indices, spanning all 26 indices of the alphabet. No index can appear twice
  reflector=randomizeReflector()
  #------------------------------------------
  
  print "Plugboard index pairs: ", plugboard
  print "Rotors index pairs (three): ", rotors
  print "Reflector index pairs: ", reflector
  


def rePositionRotors(positions):
  
  positions[2]+=1
  if positions[2]>25:
    positions[2]-=26
    positions[1]+=1

    if positions[1]>25:
      positions[1]-=26
      positions[0]+=1

      if positions[0]>25:
        return [1,1,1]
        
    return [0,1,1]
      
  else:
    return[0,0,1]
    


def enigmaEncrypt(rotorValues,text):
  
  encryption=""
  
  rotorOrder=rotorValues[0]
  rotorPositions=rotorValues[1]
  manualRotations=rotorValues[2]
  
  #Put three rotors in order
  rotors=[Rotors[rotorOrder[0]],Rotors[rotorOrder[1]],Rotors[rotorOrder[2]]]
    
  #Set rotors to initial values (i.e. positions 0, 4, 6)
  rotors=applyMovement(rotors,rotorPositions)
  
  #Apply further manual rotations
  rotors=applyMovement(rotors,manualRotations)
  
  for char in text:
    for i in range(0,len(Letters)):
      if char==Letters[i]:
        
        num=i
        
        for pPair in Plugboard:
          if num in pPair:
            newPair=deepcopy(pPair)
            newPair.remove(num)
            num=newPair[0]
            break
          
        #Pass number through the three rotors
        for rotor in rotors:
          for rPair in rotor:
            if num==rPair[0]:
              num=rPair[1]
              break
        
        #Pass number through reflector
        for refPair in Reflector:
          if num in refPair:
            newPair=deepcopy(refPair)
            newPair.remove(num)
            num=newPair[0]
            break
              
        #Pass number through rotors in the opposite direction
        for rotor in reversed(rotors):
          for rPair in rotor:
            if num==rPair[1]:
              num=rPair[0]
              break
        
        #Pass number throught plugboard again
        for pPair in Plugboard:
          if num in pPair:
            newPair=deepcopy(pPair)
            newPair.remove(num)
            num=newPair[0]
            break
      
        #Add ecnrypted letter to string
        encryption+=Letters[num]
        
        #print rotorPositions
                
        #Find new position of rotors [2,4,21] goes to [2,4,22]. Also finds how many positions each rotor should rotate, in this case [0, 0, 1]
        rotorMovement=rePositionRotors(rotorPositions)
        
        #Applies the changes to the rotors by the specified ammount
        rotors=applyMovement(rotors,rotorMovement)
        
  return encryption



#Use this function to generate a new set of random pairs for the plugboard, rotors and reflector. The variable should be equal or less than 10, which specifies how many pairs to create in the plugboard
#enigmaGenerateRandomVals(10)
#exit(0)

#Write you text to encrypt here with small letters, capital letters will be ignored
#text="let's see if alan turing can crack this code"
##text="usmajowhkfolzfjdlgmrbwhgozdpajbyqnc"
#text="weather report. twenty six degrees, a partly cloudy and warm day is expected. lowest relative humidity near thirtythree percent. expect thirteen hours of sunshine which is eightyseven percent of possible sunshine. heil hitler"
##text="vsdezoqdlxlgifenzyteslgnruriqhxstijqxkuochyqvelnhbdhkcceamrsijnmicuoccnccvoqxtcolvldrzovyvecicywbuxeojubxitptsexixyhmccmeetvjeyezmtttygmbkefranwcgnjvwbctktllkwlczlrxbuchfanviuakftkahuxhbzf"
#
##rotorValues are a list of lists where the first list is the order of the rotors (5 total, 0-4) and the second list is the position of each rotor (26 positions 0-25, one for each letter). These where the secret values passed by the German army every month and changed daily. The other variable changed daily is the plugboard connections, that can be found at the top of the page.
##The third list shows the manual rotations that could be done to the rotors, i.e. the position remains the same, but each letter maps to the one previous to it. For now it is set to 0,0,0.
#rotorValues=[[3,1,4],[2,16,21],[0,0,0]]
#
#encryptedText=enigmaEncrypt(rotorValues,text)#list of lists, where first list represents order of rotors, second list represents position of each rotor from 0 to 25
#
#print encryptedText

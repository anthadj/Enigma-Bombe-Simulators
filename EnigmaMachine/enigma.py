import os
import sys
import random
from copy import deepcopy

Letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#---------------------------------------------------------------------------------
#----------------Defualt values for Plugboard Rotors and Reflector----------------
#---------------------------------------------------------------------------------

#The values of the plugboard, up to ten pairs allowed. These were generated randomly using the function enigmaGenerateRandomVals. These were changed every day, but for simplicity we will assume to be the default values
Plugboard= [[6, 24], [10, 12], [13, 23], [17, 9], [8, 2], [19, 16], [15, 7], [18, 21], [5, 11], [22, 4]]

#List of lists making the connections of the 5 rotors. These were generated randomly using the function enigmaGenerateRandomVals. These are considered the default rotor values. Three must be chosen at random when the machine runs. Their order must also be random.
Rotors= [[[0, 3], [1, 7], [2, 21], [3, 10], [4, 25], [5, 15], [6, 12], [7, 13], [8, 19], [9, 1], [10, 8], [11, 22], [12, 23], [13, 16], [14, 5], [15, 0], [16, 24], [17, 17], [18, 11], [19, 2], [20, 20], [21, 6], [22, 9], [23, 18], [24, 14], [25, 4]], [[0, 6], [1, 0], [2, 7], [3, 23], [4, 8], [5, 17], [6, 11], [7, 4], [8, 20], [9, 22], [10, 5], [11, 1], [12, 25], [13, 10], [14, 21], [15, 19], [16, 18], [17, 3], [18, 24], [19, 16], [20, 12], [21, 13], [22, 9], [23, 2], [24, 15], [25, 14]], [[0, 18], [1, 16], [2, 1], [3, 19], [4, 2], [5, 25], [6, 21], [7, 14], [8, 0], [9, 23], [10, 9], [11, 7], [12, 11], [13, 8], [14, 13], [15, 20], [16, 24], [17, 15], [18, 5], [19, 17], [20, 10], [21, 22], [22, 12], [23, 3], [24, 6], [25, 4]], [[0, 10], [1, 6], [2, 13], [3, 25], [4, 19], [5, 12], [6, 1], [7, 15], [8, 24], [9, 11], [10, 18], [11, 4], [12, 21], [13, 5], [14, 22], [15, 17], [16, 14], [17, 23], [18, 9], [19, 16], [20, 3], [21, 2], [22, 0], [23, 7], [24, 8], [25, 20]], [[0, 4], [1, 16], [2, 25], [3, 13], [4, 18], [5, 5], [6, 19], [7, 15], [8, 10], [9, 1], [10, 12], [11, 6], [12, 23], [13, 20], [14, 7], [15, 17], [16, 24], [17, 0], [18, 14], [19, 3], [20, 2], [21, 22], [22, 8], [23, 21], [24, 9], [25, 11]]]

#The values of the 5 rotors. These were generated randomly using the function enigmaGenerateRandomVals. They are considered the default values
Reflector = [[24, 8], [12, 16], [7, 0], [15, 21], [11, 17], [1, 10], [9, 6], [5, 14], [22, 4], [13, 25], [19, 3], [18, 2], [23, 20]]

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------





#--------------------------------------------------------------------------------
#--Methods used to randomize Plugboard Rotors and Reflectors if user chooses to--
#--------------------------------------------------------------------------------

#Randomize the plugboard. Up to 10 pairs allowed
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
  
#Method that ranndomly chooses rotor order. Not used at the moment
def chooseRotorOrder():
  order=list()
  for i in range(0,3):
    while True:
      ranNum=random.randint(0,4)
      if ranNum not in order:
        order.append(ranNum)
        break
        
  return order
        
#Randomize refletor
#In the reflector, we can't map a letter to itself. That is why in the if statement we include the "and (ranNum != letNum)" part
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
    print ('Please enter a number between 0 and ten, to specify the number of pairs on the plibboard')
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
  rotors=[rotor1,rotor2,rotor3,rotor4,rotor5]
  
#  allRotors=[rotor1,rotor2,rotor3,rotor4,rotor5]
  
  #Randomly choose 3 out of the 5 rotors, and place them in a random order
#  rotorsOrder=chooseRotorOrder()
#  randomThreeRotors=[allRotors[rotorsOrder[0]],allRotors[rotorsOrder[1]],allRotors[rotorsOrder[2]]]
    
  #Apply manual movement to the rotors, i.e. move rotor 1, 2 positions to the right and rotor 2, -2 positions (2 positions to the left).
#  rotorMovement=[1,-2,0]
#  rotors=applyMovement(randomThreeRotors,rotorMovement)
  #-------------------------------------
  
  
  
  #------Create the reflector/scrambler------
  #Create the reflector. Create 13 pairs of indices, spanning all 26 indices of the alphabet. No index can appear twice
  reflector=randomizeReflector()
  #------------------------------------------
  
  print ('Plugboard index pairs: ', plugboard)
  print ('Rotors index pairs (three): ', rotors)
  print ('Reflector index pairs: ', reflector)
    
  outputRandomConnections(plugboard,rotors,reflector)
  
  #Finally, change the global values of the plugboard, reflector and rotors to the newly generated ones
  global Plugboard
  global Rotors
  global Reflector
  
  Plugboard = plugboard
  Rotors = rotors
  Reflector = reflector
  
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------





#--------------------------------------------------------------------------------
#---------------------Methods used for encyption of text-------------------------
#--------------------------------------------------------------------------------

#Applied movement of rotors
#Each entry represents how many positions each rotor should be manually moved.
#i.e. rotor1=[[0,16],[1,2],...,[25,8]] and movement=[1,0,0] then rotor1=[[0,8],[1,16],...] rotor2 and rotor3 would remain unchanged under this movement.
#Important: movement of rotors occurs every time a letter is encrypted. In that case the movement is always [0,0,1].
#If third rotor rotates 26 times the movement becomes [0,1,1] and so on like a clock.
def applyMovement(rotors,movement):
  newRotors=deepcopy(rotors)
  for i in range(0,len(movement)):
    spacesToMove=movement[i]
    #print (spacesToMove)
    if spacesToMove!=0: #If movement should occur
      for j in range(0,len(rotors[i])):

        if (j+spacesToMove)>=0 and (j+spacesToMove)<=25:
          newRotors[i][j][1] = rotors[i][j+spacesToMove][1]
        elif j+spacesToMove>25 :
          newRotors[i][j][1] = rotors[i][j+spacesToMove-26][1]
        elif j+spacesToMove<0:
          newRotors[i][j][1] = rotors[i][j+spacesToMove+26][1]

  return newRotors
        

#After a letter is encrypted, the rotors need to rotate. This method carries out this rotation
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
    


#The method that encrypts the inputted text
def enigmaEncrypt(rotorValues,text):
  
  encryption=""
  
  rotorOrder=rotorValues[0]
  rotorPositions=rotorValues[1]
  manualRotations=rotorValues[2]
  
  #Put three rotors in order
  rotors=[Rotors[rotorOrder[0]],Rotors[rotorOrder[1]],Rotors[rotorOrder[2]]]

  #Set rotors to initial positions (i.e. positions 0, 4, 6)
  rotors=applyMovement(rotors,rotorPositions)
  
  #Apply manual rotations to rotors
  rotors=applyMovement(rotors,manualRotations)
  
  #Loop through each character in the text
  for char in text:
    for i in range(len(Letters)):
      if char==Letters[i]:
        
        num=i
        #Pass number throught plugboard
        for pPair in Plugboard:
          if num in pPair:
            for entry in pPair:
              if entry!=num:
                num=entry
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
            for entry in refPair:
              if entry!=num:
                num=entry
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
            for entry in pPair:
                if entry!=num:
                    num=entry
                    break
      
        #Add ecnrypted letter to string
        encryption+=Letters[num]
        
        #Find how each rotor should rotate. e.g. [2,4,21] goes to [2,4,22], therefore rotors should move by [0,0,1] positions.
        #If positions are [2,4,25] it goes to [2,5,0] therefore rotors should rotate by [0,1,1] positions, and so on
        rotorMovement=rePositionRotors(rotorPositions)
        
        #Applies the changes to the rotors by the specified ammount
        rotors=applyMovement(rotors,rotorMovement)
        
  return encryption
  
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
  
  
  
  
  
#--------------------------------------------------------------------------------
#----------------Small functions used to read and output data--------------------
#--------------------------------------------------------------------------------
def readPreExistingRotorValues():
  rotorVals=list()
  with open('rotorValues.txt','r') as f:
    allLines = f.readlines()
    for line in allLines:
      temp=line.split(' ')[:-1] #Split into values, ignor \n at end of line
      temp = list(map(int,temp)) #Change strings to ints
      rotorVals.append(temp)
    f.close()
  return rotorVals
  
def readPreExistingConnections():
  plugboard=list()
  reflector=list()
  rotors=list()
  
  lines=''
  with open('randomConnections.txt','r') as f:
    lines=f.readlines()
    
  for index in range(len(lines)):
    if index==0 or index==2 or (index>3 and index<9): #Reading plugboard values
      temp = lines[index].split(' ')[:-1]
      
      for i in range(len(temp)):
        newList=list()
        newList.append(int(temp[i].split(',')[0]))
        newList.append(int(temp[i].split(',')[1]))
        temp[i]=newList
      
      if index==0:
        plugboard=temp
      elif index==2:
        reflector=temp
      else:
        rotors.append(temp)
            
  return plugboard,reflector,rotors

def readText():
  textToRead=''
  for file in os.listdir('.'):
    if file=='inputText.txt':
      with open(file,'r') as f:
        textToRead=f.read()
        f.close()
  return textToRead
                
def outputEncyptedText(text):
  with open('encryptedText.txt','w') as f:
    f.write(text)

def outputManualRotorvalues(rotorValues):
  with open('rotorValues.txt','w') as f:
    for vals in rotorValues:
      for val in vals:
        f.write(str(val)+' ')
      f.write('\n')
      
def outputRandomConnections(plugboardVals,rotorVals,reflectorVals):
  with open('randomConnections.txt','w') as f:
    
    for vals in plugboardVals: #Output plug values
      f.write(str(vals[0])+','+str(vals[1])+' ')
    
    f.write('\n\n')
    for vals in reflectorVals:
      f.write(str(vals[0])+','+str(vals[1])+' ')
      
    f.write('\n\n')
    for vals in rotorVals:
      for val in vals:
        f.write(str(val[0])+','+str(val[1])+' ')
      f.write('\n')
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
  
  
  
  
  
  

#----------------------------------------------------------------------------------------------------------------------
#---Three encryption methods. One using default values, one using user inputs and one using pre-existing user inputs---
#----------------------------------------------------------------------------------------------------------------------

#Method added for completion. The user is adviced to use default values (encryptWithDefaultValues)
#This method produces new random connections for pluhboard, reflector and rotors
#It then lets the user choose the initial rotor values.
#It outputs all variables to files 'randomConnections.txt' and 'rotorValues.txt' which
#are needed for method encryptWithPreExistingValues
def encryptWithUserInput(text):

  #Use this function to generate a new set of random pairs for the plugboard, rotors and reflector. The variable should be equal or less than 10, which specifies how many pairs to create in the plugboard
  print ('Creating new randomly generated connections for the plugboard, rotors and reflector')
  print ('Number of plugboard connections will also be randomised between 1 and 10 \n\n')
  numOfPlugConnections=random.randint(1,10)
  enigmaGenerateRandomVals(numOfPlugConnections)
    
    
    
  #------User inputs values------
  print ('\n\nUser needs to manually input the 3 sets of rotor values, consisting of order of rotors, position of each rotor and manual adjustment to each rotor')
  print ('There are 5 rotors, choose 3 by pressing a number from 0 to 4 and pressing enter. Rotors must be different from each other, i.e. 0,0,3 wont be accepted')
    
  rotorList=list()
  while(len(rotorList) < 3):
    rotorNum = input()
    if rotorNum.isdigit(): #Check value given is integer
      rotorInt=int(rotorNum) #Change input to integer
      if (rotorInt < 5 and rotorInt >= 0) and (rotorInt not in rotorList): #Check value is within correct range and is not used again
        rotorList.append(rotorInt)
  print (rotorList)
    
    
  print ('Each rotor can start from a position from 1 to 26, where each position represents a letter of the english alphabet')
  print ('Input one number from 0 to 25 as the position of each rotor. First entry will be for the first rotor and so on')
    
  rotorPositionList=list()
  while(len(rotorPositionList) < 3):
    rotorPositionNum = input()
    if rotorPositionNum.isdigit(): #Check value given is integer
      rotorPositionInt=int(rotorPositionNum) #Change input to integer
      if rotorPositionInt < 26 and rotorPositionInt >= 0: #Check rotor position is within accepted range
        rotorPositionList.append(rotorPositionInt)
  print (rotorPositionList)


  print ('Finally, manual rotations could be made to the rotor positions. This would be in added as an extra precaution for the war')
  print ('Extra rotations would basically act to change the rotorPositions. For example, if a rotor was placed at position 14, and you apply ')
  print ('a manual adjustment of 4 positions. Adjustments have no limit, you can do positive, or negative adjustments and it can be any number of them')
  print ('Please enter the manual adjustments for each rotor. 1st adjustmnet will be done on rotor 1 and so on')

  rotorManualAdjustmentList=list()
  while(len(rotorManualAdjustmentList) < 3):
    rotorManualAdjustmentNum = input()
    try:
      rotorManualAdjustmentInt = int(rotorManualAdjustmentNum)
      rotorManualAdjustmentList.append(rotorManualAdjustmentInt)
    except:
      continue
  print (rotorManualAdjustmentList)
  #------Finished inputting user's manual rotor values------


  #list of lists, where first list represents order of rotors, second represents position of each rotor from 0 to 25, third is rotor manual rotations
  rotorValues=[rotorList,rotorPositionList,rotorManualAdjustmentList]
  print (rotorValues)
        
  outputManualRotorvalues(rotorValues) #Outputing rotor values
    
  encryptedText=enigmaEncrypt(rotorValues,text)

  return encryptedText
  
  
  
#Method added for completion. The user is adviced to use default values (encryptWithDefaultValues)
#This method is used to encrypt a message when there exist pre-existing values
#for plugboard, reflector and rotor values, as well as rotor variables.
#Files randomConnections.txt and rotorValues.txt need to exist in the directory
#in order for this method to run. These files are produced by the encryptWithUserInput() method
def encryptWithPreExistingValues(text):
  
  plugboard,reflector,rotors = readPreExistingConnections()
  
  #Set the values that were just read, to be global
  global Plugboard
  global Rotors
  global Reflector
  
  Plugboard = plugboard
  Reflector = reflector
  Rotors = rotors
  
#  print ("Plugboard: ", Plugboard)
    
  rotorValues = readPreExistingRotorValues()
  print ('Rotor values: ', rotorValues)
  
  print ('Encrypting text with pre-existing values: ')
  encryptedText=enigmaEncrypt(rotorValues,text)
  
  return encryptedText
  
  

#User is adviced to use this function
#Method that encrypts text in inputText.txt file using default values. The values were produced randomly using method enigmaGenerateRandomVals()
def encryptWithDefaultValues(text):

  #rotorValues are a list of lists where the first list is the order of the rotors (5 total, 0-4) and the second list is the position of each rotor (26 positions 0-25, one for each letter). The third list shows the manual rotations that could be done to the rotors,
  #These where the secret values passed by the German army on a sheet of paper every month. On the sheet of paper it had enough values for the whole month and they had to be changed daily.
  rotorValues=[[3,1,4],[2,16,21],[0,0,0]]
  encryptedText=enigmaEncrypt(rotorValues,text)#list of lists, where first list represents order of rotors, second list represents position of each rotor from 0 to 25
  return encryptedText

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------







def main():

  #Read text to encrypt from file
  text=readText()
  print ('Original text:\n', text)
    
    
  #There are three main encyption methods, 2 should be commented out here
  encryptedText = encryptWithDefaultValues(text)        #First method uses default values
  #encryptedText = encryptWithUserInput(text)           #Second method produces new random connections and lets user adjust rotor positions. Outputs values to 2 txt files
  #encryptedText = encryptWithPreExistingValues(text)   #Third method reads the 2 txt files of the second method and carries out the encryption with those values

  print ('Encrypted Text:\n', encryptedText)
    
  #Output encrypted text to file 'encryptedText.txt'
  outputEncyptedText(encryptedText)


if __name__ == '__main__':
  main()

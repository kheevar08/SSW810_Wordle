import csv
import string
from tabnanny import check
from tempfile import TemporaryDirectory
occurence = {
  'A': [0, 0, 0, 0, 0],
  'B': [0, 0, 0, 0, 0],
  'C': [0, 0, 0, 0, 0],
  'D': [0, 0, 0, 0, 0],
  'E': [0, 0, 0, 0, 0],
  'F': [0, 0, 0, 0, 0],
  'G': [0, 0, 0, 0, 0],
  'H': [0, 0, 0, 0, 0],
  'I': [0, 0, 0, 0, 0],
  'J': [0, 0, 0, 0, 0],
  'K': [0, 0, 0, 0, 0],
  'L': [0, 0, 0, 0, 0],
  'M': [0, 0, 0, 0, 0],
  'N': [0, 0, 0, 0, 0],
  'O': [0, 0, 0, 0, 0],
  'P': [0, 0, 0, 0, 0],
  'Q': [0, 0, 0, 0, 0],
  'R': [0, 0, 0, 0, 0],
  'S': [0, 0, 0, 0, 0],
  'T': [0, 0, 0, 0, 0],
  'U': [0, 0, 0, 0, 0],
  'V': [0, 0, 0, 0, 0],
  'W': [0, 0, 0, 0, 0],
  'X': [0, 0, 0, 0, 0],
  'Y': [0, 0, 0, 0, 0],
  'Z': [0, 0, 0, 0, 0],
}


def letterLikelyhood():
  """Function to calculate the likelyhood of the letters"""
  f = open("wordList.txt",'r')
  content = f.read()
  tempList = content.split('\n')
  f.close()
  for word in tempList:
    count = 0
    for letter in word:
      occurence[letter][count] += 1
      count += 1
  flag = 0
  for word in tempList:
    flag += 1
  for letter in string.ascii_uppercase:
    occurence[letter][0] = round((occurence[letter][0] / flag),3)
    occurence[letter][1] = round((occurence[letter][1] / flag),3)
    occurence[letter][2] = round((occurence[letter][2] / flag),3)
    occurence[letter][3] = round((occurence[letter][3] / flag),3)
    occurence[letter][4] = round((occurence[letter][4] / flag),3)
  f = open("letterFrequency.csv", 'w')
  f.write("letter,first_pos, second_pos, third_pos, fourth_pos, fifth_pos \n")
  for key in string.ascii_uppercase:
    f.write(f"{key}, {occurence[key][0]}, {occurence[key][1]}, {occurence[key][2]}, {occurence[key][3]}, {occurence[key][4]}\n")
  f.close()
    
def dictListToTuple(dict):
  """Function to convert a list to tuple present in a dictionary"""
  for key in dict.keys():
    dict[key] = tuple(dict[key])

def statToDict():
  """Function for reading data from a csv file and storing it into a dictionary"""
  f = open("letterFrequency.csv", 'r')
  content = f.read()
  tempList = content.split('\n')
  myDict = {}
  for line in range(1,len(tempList)):
    temp = tempList[line].split(", ")
    if checkTemp(temp):
      myDict[temp[0]] = (temp[1],temp[2],temp[3],temp[4],temp[5])
  return myDict

def wordRank():
  """Function for calculating the ranks of the word present in the dictionary"""
  f = open("wordList.txt",'r')
  content = f.read()
  tempList = content.split('\n')
  f.close()
  myDict = {}
  for word in tempList:
      likelyhood = float(occurence[word[0]][0]) * float(occurence[word[1]][1]) * float(occurence[word[2]][2]) * float(occurence[word[3]][3]) * float(occurence[word[4]][4])
      myDict[word] = likelyhood
  finalDict = sorted(myDict.items(), key=lambda x:x[1])
  finalDict.reverse()
  f = open("wordRank.csv", 'w')
  f.write("rank, word, likelyhood \n")
  flag = 1
  for word in finalDict:
    f.write(f"{flag}, {word[0]}, {word[1]}\n")
    flag += 1
  f.close()

def checkTemp(temp):
  if(len(temp[0]) != 0):
    return True
  else:
    return False
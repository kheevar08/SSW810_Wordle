ans = "SONAR" #Answer of the WORDLE Game
flag = []     
status = [0,0,0,0,0] #To store the status of each letter after an attempt
userInputList = []      #To store all the user inputs
temp = 0                #To quit the game after the it is solved
k = 1                   #initialization
while k < 7 :           #while loop
    flag = [0,0,0,0,0]  #initialization before each iteration of while loop
    temp = 0    
    print(f"Attempt #{k}:")
    print("Any 5 letter word")
    word = input()      #Taking user's input
    word = word.upper() 
    if len(word) != 5 or word in userInputList or not word.isalpha(): #checking whether the input is valid or not
        print("Input should be a unique 5 letter word")
        
    else:
        userInputList.append(word)
        for i in range(5):
            if word[i] == ans[0] or word[i] == ans[1] or word[i] == ans[2] or word[i] == ans[3] or word[i] == ans[4] :
                flag[i] = 1             #if the letter is present in the answer
            if word[i] == ans[i] :      
                flag[i] = 2             #if the letter is at it's correct place
        for j in range(5):
            if flag[j] == 0:
                status[j] = f"{word[j]} is not present"         #if the letter is not present
            elif flag[j] == 1:
                status[j] = f"{word[j]} is present but not in correct place"    #if the letter is present but not in correct place
            else:
                status[j] = f"{word[j]} is correct"             #if the letter is at it's correct place
        k = k + 1
        for y in range(5):
            print(status[y])    #to print the status after each attempt
            temp = temp + flag[y]
        if temp == 10:
            print("You have solved the Wordle. Thank You!")
            quit()



#Pseudocode





# SET ans TO "SONAR" 

# SET flag TO []     

# SET status TO [0,0,0,0,0]

# SET userInputList TO []      

# SET temp TO 0                

# SET k TO 1                  

# WHILE k < 7 :           

#     SET flag TO [0,0,0,0,0]  

#     SET temp TO 0    

#     OUTPUT("Attempt No:")

#     OUTPUT("Any 5 letter word")

#     SET word TO INPUT()     

#     SET word TO word.upper() 

#     IF len(word) != 5 or word IN userInputList or not word.isalpha(): 

#         OUTPUT("Input should be a unique 5 letter word")

        

#     ELSE:

#         userInputList.append(word)

#         FOR i IN range(5):

#             IF word[i] EQUALS ans[0] or word[i] EQUALS ans[1] or word[i] EQUALS ans[2] or word[i] EQUALS ans[3] or word[i] EQUALS ans[4] :

#                 SET flag[i] TO 1             

#             IF word[i] EQUALS ans[i] :      

#                 SET flag[i] TO 2             

#         FOR j IN range(5):

#             IF flag[j] EQUALS 0:

#                 SET status[j] TO letter is not present"         

#             ELSEIF flag[j] EQUALS 1:

#                 SET status[j] TO letter is present but not IN correct place"    

#             ELSE:

#                 SET status[j] TO letter is correct"             

#         SET k TO k + 1

#         FOR y IN range(5):

#             OUTPUT(status[y])    

#             SET temp TO temp + flag[y]

#         IF temp EQUALS 10:

#             OUTPUT("You have solved the Wordle. Thank You!")

#             quit()








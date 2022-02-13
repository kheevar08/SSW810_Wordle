userInputList = []
def userinput(k) :
    
    print(f"Attempt #{k}:")
    print("Any 5 letter word")
    word = input()      #Taking user's input
    word = word.upper() 
    if(len(word) == 0):         #checking whether the word is empty or not
        quit()                
    if len(word) != 5 or word in userInputList or not word.isalpha(): #checking whether the input is valid or not
        print("Input should be a unique 5 letter word")
    else:
        userInputList.append(word)
        k = k+1
        return word         #returning the user's input
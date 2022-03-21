
class Ui:
    userInputList = []
    def __init__(self):
        self.userInputList = []
    def quitfunction(self,a):
        if(len(a) == 0):
            return True
        else:
            return False

    def userinput(self,k) :
        
        print(f"Attempt #{k}:")
        print("Any 5 letter word")
        word = input()      #Taking user's input
        word = word.upper() 
        if(self.quitfunction(word)):         #checking whether the word is empty or not
            quit()               
        if len(word) != 5 or word in self.userInputList or not word.isalpha(): #checking whether the input is valid or not
            print("Input should be a unique 5 letter word")
            return "incorrect input"
        else:
            self.userInputList.append(word)
            k = k+1
            return word         #returning the user's input
import HW03_Kheevar_Choudhary_ui as ui          #importing the ui module
import HW03_Kheevar_Choudhary_dictionary as dictionary      #importing the dictionary module


def main():
    while(True):                        #used to run the program indefinitely until a user enters an empty word to exit the program
        answer = dictionary.randomWord()
        attempts = 1
        while(attempts<7):              # user has 6 attempts to guess the correct word
            word = ui.userinput(attempts)
            status = []
            while(dictionary.checkWord(word) != True):      #checking if the word is a valid dictionary word or not
                print("Not a valid dictionary word")
                word = ui.userinput(attempts)

            letter_counts: dict = {}                #making a dictionary to store the number of letters

            if(word == answer):                     
                print("Correct Word! \n")
                print("Now the word has been changed, to exit please press ENTER/RETURN")
                break
            else:
                for letter in answer:           #loop used to store the number of letters in the answer
                    if letter in letter_counts.keys():
                        letter_counts[letter] += 1
                    else:
                        letter_counts[letter] = 1
                for index in range(len(answer)):  #loop used to store the status
                    if word[index] == answer[index]:
                        status.append(' ')
                        letter_counts[answer[index]] -= 1
                    else:
                        status.append('"')
                            
                for index in range(len(answer)):
                    if word[index] != answer[index]:
                        if word[index] in letter_counts:
                            if letter_counts[word[index]] > 0:
                                letter_counts[word[index]] -= 1
                                status[index] = "`"  
                attempts = attempts + 1
                print(''.join(status))          #printing the status after an attempt
            if(attempts == 7):              #checking if this is the last attempt or not
                print(f"The correct answer is #{answer}")
                print("Now the word has been changed, to exit please press ENTER/RETURN")

if __name__ == "__main__":
    main()
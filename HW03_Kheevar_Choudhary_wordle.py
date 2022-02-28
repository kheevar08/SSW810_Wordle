import HW03_Kheevar_Choudhary_ui as ui          #importing the ui module
import HW03_Kheevar_Choudhary_dictionary as dictionary      #importing the dictionary module


def compareWord(a,b):
    if(a==b):
        return True
    else:
        return False

def main():
    gamesPlayed = 0
    gamesWon = 0
    guessDistribution = [0,0,0,0,0,0]
    while(True):
        f = open("gameplay.log", "a+")                        #used to run the program indefinitely until a user enters an empty word to exit the program
        gamesPlayed = gamesPlayed + 1
        answer = dictionary.randomWord()
        dictionary.removeWord(answer)
        f.write(f"Selected Word: {answer}\n")
        attempts = 1
        while(attempts<7):              # user has 6 attempts to guess the correct word
            word = ui.userinput(attempts)
            status = []
            while(dictionary.checkWord(word) != True):      #checking if the word is a valid dictionary word or not
                print("Not a valid dictionary word")
                word = ui.userinput(attempts)
            f.write(f"User Input:{word}\n")
            letter_counts: dict = {}                #making a dictionary to store the number of letters

            if(compareWord(word,answer)):                     
                print("Correct Word! \n")
                gamesWon = gamesWon + 1
                guessDistribution[attempts-1] += 1
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
        print("GAME STATISTICS")
        print(f"Total number of games played: {gamesPlayed}")
        print(f"Win percentage: {(gamesWon*100/gamesPlayed): .2f}%")
        print("Guess Distribution")
        print(f"Guessed in 1st attempt : {guessDistribution[0]}")
        print(f"Guessed in 2nd attempt : {guessDistribution[1]}")
        print(f"Guessed in 3rd attempt : {guessDistribution[2]}")
        print(f"Guessed in 4th attempt : {guessDistribution[3]}")
        print(f"Guessed in 5th attempt : {guessDistribution[4]}")
        print(f"Guessed in 6th attempt : {guessDistribution[5]}")
        f.write("User Report\n")
        f.write(f"Total number of games played: {gamesPlayed}\n")
        f.write(f"Win percentage: {(gamesWon*100/gamesPlayed): .2f}%\n")
        f.write(f"Guessed in 1st attempt : {guessDistribution[0]}\n")
        f.write(f"Guessed in 2nd attempt : {guessDistribution[1]}\n")
        f.write(f"Guessed in 3rd attempt : {guessDistribution[2]}\n")
        f.write(f"Guessed in 4th attempt : {guessDistribution[3]}\n")
        f.write(f"Guessed in 5th attempt : {guessDistribution[4]}\n")
        f.write(f"Guessed in 6th attempt : {guessDistribution[5]}\n")


if __name__ == "__main__":
    main()
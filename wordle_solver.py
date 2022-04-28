import HW03_Kheevar_Choudhary_wordle as w
import HW03_Kheevar_Choudhary_dictionary as d
import wordle_helper as wh
import logger as l

def wordle_solver(log):
    win = 0
    loss = 0
    wordle = w.Wordle()
    dictionary = d.Dictionary()
    attempts = 1
    word = "SALES"
    fl = ''
    sl = ''
    tl = ''
    fol = ''
    fil = ''
    goodLetters = []
    badLetters = []
    answer = dictionary.randomWord()
    log.writeGameData()
    flag = True
    while(attempts<7):              # user has 6 attempts to guess the correct word
        totalAttempts = attempts
        log.writeGameAttempts(attempts,word,answer)
        attempts = attempts + 1
        temp = wordle.play_wordle_solver(answer,attempts,word,log)
        if temp == 0:
            flag = True
            win +=1
            break
        if temp != 0:
            temp_list = ['','','','','']
            temp_list[0] = temp[0]
            temp_list[1] = temp[1]
            temp_list[2] = temp[2]
            temp_list[3] = temp[3]
            temp_list[4] = temp[4]
            if temp_list[0] == ' ':
                # fl = word.split()[0]
                if not goodLetters.__contains__(word[0]):
                    goodLetters.append(word[0])
            if temp_list[1] == ' ':
                # sl = word.split()[1]
                if not goodLetters.__contains__(word[1]):
                    goodLetters.append(word[1])
            if temp_list[2] == ' ':
                # tl = word.split()[2]
                if not goodLetters.__contains__(word[2]):
                    goodLetters.append(word[2])
            if temp_list[3] == ' ':
                # fol = word.split()[3]
                if not goodLetters.__contains__(word[3]):
                    goodLetters.append(word[3])
            if temp_list[4] == ' ':
                # fil = word.split()[4]
                if not goodLetters.__contains__(word[4]):
                    goodLetters.append(word[4])
            
            if temp_list[0] == '"' and not badLetters.__contains__(word[0]) and not goodLetters.__contains__(word[0]):
                badLetters.append(word[0])
            if temp_list[1] == '"' and not badLetters.__contains__(word[1]) and not goodLetters.__contains__(word[1]):
                badLetters.append(word[1])
            if temp_list[2] == '"' and not badLetters.__contains__(word[2]) and not goodLetters.__contains__(word[2]):
                badLetters.append(word[2])
            if temp_list[3] == '"' and not badLetters.__contains__(word[3]) and not goodLetters.__contains__(word[3]):
                badLetters.append(word[3])
            if temp_list[4] == '"' and not badLetters.__contains__(word[4]) and not goodLetters.__contains__(word[4]):
                badLetters.append(word[4])
            
            if temp_list[0] == '`' and not goodLetters.__contains__(word[0]):
                goodLetters.append(word[0])
            if temp_list[1] == '`' and not goodLetters.__contains__(word[1]):
                goodLetters.append(word[1])
            if temp_list[2] == '`' and not goodLetters.__contains__(word[2]):
                goodLetters.append(word[2])
            if temp_list[3] == '`' and not goodLetters.__contains__(word[3]):
                goodLetters.append(word[3])
            if temp_list[4] == '`' and not goodLetters.__contains__(word[4]):
                goodLetters.append(word[4])
            
            solver_list = wh.rankedWords(goodLetters,badLetters)
            if(len(solver_list) > 0):
                word = solver_list[0]
            else:
                print("Failed to solve the wordle")
                flag = False
                loss += 1
                break
    log.writeGameStatistics(flag,totalAttempts,(win/(win+loss+1)))

logg = l.logger()
#Sometimes the code will return "Failed to solve the wordle" and sometimes it will guess the correct word.
for i in range(0,100):
    print(i)
    wordle_solver(logg)

logg.generateReport('2022-04-24 00:00:00.000000','2022-05-05 00:00:00.000000')
logg.closeLog()
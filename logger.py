import sqlite3
from datetime import datetime
import socket
import os

class logger():
    def __init__(self) -> None:
        if os.path.exists("sqlLogger.db"):
            os.remove("sqlLogger.db")
        self.connect = sqlite3.connect('sqlLogger.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute('''CREATE TABLE gameData (id integer primary key autoincrement, date text, localIp text)''')
        self.cursor.execute('''CREATE TABLE gameAttempts (id integer primary key autoincrement, date text, attempt text,userWord text, gameWord text, gameDataID integer, FOREIGN KEY(gameDataID) REFERENCES game(id))''')
        self.cursor.execute('''CREATE TABLE gameStatistics (id integer primary key autoincrement, date text, winLoss text, numGames integer, winRate text, gameDataID integer, FOREIGN KEY(gameDataID) REFERENCES game(id))''')
        self.ip = self.getIp()
        self.currentGameId = None
    
    def getIp(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(0)
        try:
            # doesn't even have to be reachable
            sock.connect(('10.255.255.255', 1))
            ip = sock.getsockname()[0]
        except Exception:
            ip = '127.0.0.1'
        finally:
            sock.close()
        return ip

    def writeGameAttempts(self, attempt, userWord,gameWord):
        time = datetime.now()
        self.cursor.execute("insert into gameAttempts values (NULL, ?, ?, ?, ?, ?)", (time, attempt, userWord, gameWord, self.currentGameId))

    def writeGameData(self):
        time = datetime.now()
        self.cursor.execute("insert into gameData values (NULL, ?, ?)", (time, self.ip))
        self.currentGameId = self.cursor.lastrowid

    def writeGameStatistics(self, winLoss, totalAttempts, winPercent):
        time = datetime.now()
        self.cursor.execute("insert into gameStatistics values (NULL, ?, ?, ?, ?, ?)", (time, winLoss, totalAttempts, winPercent, self.currentGameId))

    def closeLog(self):
        self.connect.commit()
        self.connect.close()
    

    def generateReport(self, startDate, endDate):
        if os.path.exists("dbReport.txt"):
            os.remove("dbReport.txt")
        report = open('dbReport.txt', 'w')
        report.write("Game Statistics\n")
        report.write(f"start date: {startDate}")
        report.write(f"end date: {endDate}")
        self.cursor.execute("select * from gameData where date>= :startDate and date<=:endDate",{"startDate":self.startDate,"endDate":self.endDate})
        data = self.cursor.fetchall()
        self.cursor.execute("select * from gameStatistics order by rowid")
        gameStatData = self.cursor.fetchall()
        lastGameStat = gameStatData[-1]
        report.write(f'Total number of games played: {len(data)}\n')
        report.write(f'Total number of games won: {lastGameStat[4]}\n')
        report.write(f'Guess Distribution: \n')
        guess = lastGameStat[5][1:-1].replace(' ','').split(',')
        for i, dist in enumerate(guess):
            print(f'Attempt {i+1}: {dist}')
            report.write(f'Attempt {i+1}: {dist}\n')
        report.close()
        print("Report generated at dbReport.txt")

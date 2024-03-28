#  This script runs daily to retrieve Fantasy5 numbers

# from email.policy import default
from bs4 import BeautifulSoup

import requests, json

from datetime import datetime, timedelta

from dbs import create_server_connection

from functions import F5AddStats

connection =  create_server_connection()

# Web site
URL = "https://www.flalottery.com/fantasy5"
DATA_FILE = "/home/jgoolsby/ssr-lottery/scripts/Python/environments/apienv/scripts/US/Florida/data/Fantasy5Eve.py"

def writeNewFile(s):

        file1 = open(DATA_FILE, 'w')  
        
        # # Writing a string to file
        file1.write(s) 
        
        # # Closing file
        file1.close()

        return

def checkAgainstPrevNums():
        file1 = open(DATA_FILE, 'r')
        return file1.read()

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
        'Accept-Language' : 'en-US,en;q=0.5', 
        'Accept-Encoding' : 'gzip, deflate', 
        'DNT' : '1', # Do Not Track Request Header 
        'Connection' : 'close'}

def InsertIntoDB(object):
    
    mycursor = connection.cursor()

    sql = "INSERT INTO FLFantasy5 (date, sequence, n1, n2, n3, n4, n5, jackpot) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (object['result']['date'], object['result']['sequence'], object['result']['numbers'][0]['n1'], object['result']['numbers'][0]['n2'], object['result']['numbers'][0]['n3'], object['result']['numbers'][0]['n4'], object['result']['numbers'][0]['n5'], object['result']['jackpot']) 

    mycursor.execute(sql, val)

    connection.commit()

    return mycursor.lastrowid

def split(word):
    return [char for char in word]
        
def fixDate(date):
    
    def adjustMth(month):
        match month:
            case 'January':
                return '01'
            case 'February':
                return '02'
            case 'March':
                return '03'
            case 'April':
                return '04'
            case 'May':
                return '05'
            case 'June':
                return '06'
            case 'July':
                return '07'
            case 'August':
                return '08'
            case 'September':
                return '09'
            case 'October':
                return '10'
            case 'November':
                return '11'
            case 'December':
                return '12'

    def fixDay(day):
        match str(day):
            case '1':
                return '01'
            case '2':
                return '02'
            case '3':
                return '03'
            case '4':
                return '04'
            case '5':
                return '05'
            case '6':
                return '06'
            case '7':
                return '07'
            case '8':
                return '08'                        
            case '9':
                return '09'
            case _:
                return day


    dateSplit = date.split()    
    year = dateSplit[3]
    month =   adjustMth(dateSplit[1])
    day = fixDay(dateSplit[2].replace(',', '') )
    sqlDate = f'{year}-{month}-{fixDay(day)}' + ' 00:00:00'
    return sqlDate

if __name__ == '__main__':

    # get site
    page = requests.get(URL, headers = headers)

    # parse data
    soup = BeautifulSoup(page.content, "html.parser")  

    # Find all Divs
    gameNumb = soup.find_all('div', class_="gamePageNumbers")

    # Start here getting date from results
    # daySession = gameNumb[0].find_all('p')
    evening = gameNumb[1].find_all('p')

    # Rolldown
    if len(evening) == 4:
        # the winning Number date played
        thePlayDate = evening[1].text

        # Winning Numbers
        winningNumbersEve = evening[2].text  

        # Winning Numbers array
        splitEveGameSection = winningNumbersEve.split('-')

    else:
        # the winning Number date played
        thePlayDate = evening[3].text

        # Winning Numbers
        winningNumbersEve = evening[4].text  

        # Winning Numbers array
        splitEveGameSection = winningNumbersEve.split('-')
    
    # Date
    today = datetime.today()
    yesterday = str(today - timedelta(days=1))
    dates = yesterday.split(' ')
    date = dates[0] + " 00:00:00"
    
    pos1 = splitEveGameSection[0]
    pos2 = splitEveGameSection[1]
    pos3 = splitEveGameSection[2]
    pos4 = splitEveGameSection[3]
    pos5 = splitEveGameSection[4]

    obj = {
        "result": {
            "date": fixDate(thePlayDate),
            "numbers": [{
                "n1": pos1,
                "n2": pos2,
                "n3": pos3,
                "n4": pos4,
                "n5": pos5,
            }],
            "sequence": winningNumbersEve,
            "jackpot": 'null'
        }
    }
    
    
    # Check local file for previous results
    verify = checkAgainstPrevNums()

    gg = json.loads(verify)
    
    # # Compare previous results
    if obj["result"]["date"] != gg["date"]:

        # # Pass dictionary results to DB function
        InsertIntoDB(obj)
    
        # # Update Stats - Pass sequence to function for pattern, subpattern, doubles, triples DB update
        F5AddStats(winningNumbersEve)

        # # Parse into string
        lds = json.dumps(obj["result"])
                
        # # Write new results to file
        writeNewFile(lds)


from bs4 import BeautifulSoup

import requests, json

from datetime import datetime, timedelta

from dbs import create_server_connection

connection =  create_server_connection()

from functions import fixDate


URL = "https://www.flalottery.com/jackpotTriplePlay"
DATA_FILE = "/home/jgoolsby/ssr-lottery/scripts/Python/environments/apienv/scripts/US/Florida/data/jackpotTriplePlay.py"

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

    sql = "INSERT INTO FLJackpotTriplePlay (date, sequence, firstNum, secondNum, thirdNum, fourthNum, fifthNum, sixthNum) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (object['result']['date'], object['result']['sequence'], object['result']['numbers'][0]['n1'], object['result']['numbers'][0]['n2'], object['result']['numbers'][0]['n3'], object['result']['numbers'][0]['n4'], object['result']['numbers'][0]['n5'], object['result']['numbers'][0]['n6']) 
    
    mycursor.execute(sql, val)

    connection.commit()

    return mycursor.lastrowid

# get site
page = requests.get(URL, headers = headers)

# parse data
soup = BeautifulSoup(page.content, "html.parser")

gameNumb = soup.find_all('div', class_="gamePageNumbers")

results = soup.find_all("span", class_="balls")

pos1 = results[0].text
pos2 = results[1].text
pos3 = results[2].text
pos4 = results[3].text
pos5 = results[4].text
pos6 = results[5].text
arr = [results[0].text, results[1].text, results[2].text, results[3].text, results[4].text]
winningNumbers = pos1 + "-" + pos2 + "-" + pos3 + "-" + pos4 + "-" + pos5 + "-" + pos6

# start here getting date from results
daterr = gameNumb[0].find_all('p')

thePlayDate = daterr[4].text

obj = {
        "result": {
            "date": fixDate(thePlayDate),
            "numbers": [{
                "n1": pos1,
                "n2": pos2,
                "n3": pos3,
                "n4": pos4,
                "n5": pos5,
                "n6": pos6
            }],
            "sequence": winningNumbers
        }
}

# Check local file for previous results
verify = checkAgainstPrevNums()

gg = json.loads(verify)

# Compare previous results
if obj["result"]["date"] != gg["date"]:

        # Pass dictionary results to DB function
        InsertIntoDB(obj)

        # Parse into string
        lds = json.dumps(obj["result"])
                
        # Write new results to file
        writeNewFile(lds)
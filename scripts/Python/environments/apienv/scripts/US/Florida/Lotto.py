from collections.abc import Sequence
from bs4 import BeautifulSoup

import requests, json

from datetime import datetime, timedelta

from dbs import create_server_connection

from functions import fixDate

connection =  create_server_connection()

URL = "https://www.flalottery.com/lotto"
DATA_FILE = "/home/jgoolsby/ssr-lottery/scripts/Python/environments/apienv/scripts/US/Florida/data/lotto.py"

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

def InsertIntoDB(object, object2):
    
    mycursor = connection.cursor()

    sql = "INSERT INTO FLlotto (date, sequence, firstNum, secondNum, thirdNum, fourthNum, fifthNum, sixthNum, dp, dpn1, dpn2, dpn3, dpn4, dpn5, dpn6) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (object['result']['date'], object['result']['sequence'], object['result']['numbers'][0]['n1'], object['result']['numbers'][0]['n2'], object['result']['numbers'][0]['n3'], object['result']['numbers'][0]['n4'], object['result']['numbers'][0]['n5'], object['result']['numbers'][0]['n6'], object2['result']['sequence'], object2['result']['numbers'][0]['n1'], object2['result']['numbers'][0]['n2'], object2['result']['numbers'][0]['n3'], object2['result']['numbers'][0]['n4'], object2['result']['numbers'][0]['n5'], object2['result']['numbers'][0]['n6'] ) 
    
    mycursor.execute(sql, val)

    connection.commit()

    return mycursor.lastrowid

# get site
page = requests.get(URL, headers = headers)

# parse data
soup = BeautifulSoup(page.content, "html.parser")


gameNumb = soup.find_all('div', class_="gamePageNumbers")

# Get lotto numbers here
fff = gameNumb[0].find_all('span')
temp= gameNumb[0].find_all('p')
n1 = fff[0].text
n2 = fff[2].text
n3 = fff[4].text
n4 = fff[6].text
n5 = fff[8].text
n6 = fff[10].text
seq = n1 + "-" + n2 + "-" + n3 + "-" + n4 + "-" + n5 + "-" + n6
dates = temp[4].text

obj = {
        "result": {
            "date": fixDate(dates),
            "numbers": [{
                "n1": n1,
                "n2": n2,
                "n3": n3,
                "n4": n4,
                "n5": n5,
                "n6": n6
            }],
            "sequence": seq
        }
}

# Deal with DP  here
ffff = gameNumb[1].find_all("span")
temp= gameNumb[1].find_all('p')
DPn1 = ffff[0].text
DPn2 = ffff[2].text
DPn3 = ffff[4].text
DPn4 = ffff[6].text
DPn5 = ffff[8].text
DPn6 = ffff[10].text
DPseq = DPn1 + "-" + DPn2 + "-" + DPn3 + "-" + DPn4 + "-" + DPn5 + "-" + DPn6
datesDP = temp[0].text

DPobj = {
        "result": {
            "date": fixDate(datesDP),
            "numbers": [{
                "n1": DPn1,
                "n2": DPn2,
                "n3": DPn3,
                "n4": DPn4,
                "n5": DPn5,
                "n6": DPn6
            }],
            "sequence": DPseq
        }
}

#  check if lotto and DP dates are drawn same
if dates == datesDP:

        # Check local file for previous results
        verify = checkAgainstPrevNums()

        # Parse JSON 
        gg = json.loads(verify)

        # Compare previous results
        if obj["result"]["date"] != gg["date"]:

                # Pass dictionary results to DB function
                InsertIntoDB(obj, DPobj)

                # Parse into string
                lds = json.dumps(obj["result"])
                
                # Write new results to file
                writeNewFile(lds)


else:
        xxxxx=0
        exit

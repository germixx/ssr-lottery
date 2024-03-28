# This script gets run daily


from bs4 import BeautifulSoup
import requests, json

from datetime import datetime, timedelta

from functions import fixDate, InsertIntoDBFLPick5Eve

URL = "https://www.flalottery.com/pick5"
DATA_FILE = "/home/jgoolsby/ssr-lottery/scripts/Python/environments/apienv/scripts/US/Florida/data/pick5Eve.py"

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
if __name__ == '__main__':

        # get site
        page = requests.get(URL, headers = headers)

        # parse data
        soup = BeautifulSoup(page.content, "html.parser")

        gameNumb = soup.find_all('div', class_="gamePageNumbers")

        eveningResults = gameNumb[1].find_all('p')

        eveningDate = eveningResults[1].text

        tempsplitEve = [int(x) for x in str(eveningResults[2].text.replace('-', ''))]
        
        obj = {
                "result": {
                        "date": fixDate(eveningDate),
                        "n1": tempsplitEve[0],
                        "n2": tempsplitEve[1],
                        "n3": tempsplitEve[2],
                        "n4": tempsplitEve[3],
                        "n5": tempsplitEve[4],
                        "fireBall": tempsplitEve[5],
                        "sequence": str(tempsplitEve[0]) + "" + str(tempsplitEve[1]) + "" + str(tempsplitEve[2]) + "" + str(tempsplitEve[3])  + "" + str(tempsplitEve[4])
                }
        }
        
        # Check local file for previous results
        verify = checkAgainstPrevNums()

        # Parse previous results
        gg = json.loads(verify)
        
        # Compare previous results
        if obj["result"]["date"] != gg["date"]:

                # Pass dictionary results to DB function
                InsertIntoDBFLPick5Eve(obj)

                # Parse into string
                lds = json.dumps(obj["result"])
                
                # Write new results to file
                writeNewFile(lds)






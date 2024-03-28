# Script for double tables

from bs4 import BeautifulSoup

from datetime import datetime
from datetime import timedelta

import requests

from functions import insertIntoDB

URL = "https://jgoolsby.com/cash4life.html"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
        'Accept-Language' : 'en-US,en;q=0.5', 
        'Accept-Encoding' : 'gzip, deflate', 
        'DNT' : '1', # Do Not Track Request Header 
        'Connection' : 'close'
}

def fixDateDB(date):
    
    dateObj = datetime.strptime(date, '%m/%d/%y')

    dater = str(dateObj)

    return dater

page = requests.get(URL, headers = headers)
    
# # parse website data
soup = BeautifulSoup(page.content, "html.parser")

# # get all data tables
tablez = soup.find_all("table")

tab = tablez[0]

rows = tab.find_all('tr')

daat = []

for i in rows:
    table_data = i.find_all('td')
    
    data = [j.text for j in table_data]
    
    daat.append(data)

sliceObj = slice(12, 71)

slicedResults =  daat[sliceObj]

master = []
filteredResultsCol1 = []
filteredResultsCol2 = []

for d in slicedResults:
    # print(d)
    lengthh = len(d)

    # Skips the empty lines
    if d[3] != '':

        tmpNumsCol1 = [int(d[3]), int(d[7]), int(d[11]), int(d[15]), int(d[19])]
        tmpNumsCol1.sort()
        tmpNumsCol1.append(int(d[23]))

        colObj1 = {
            "date": fixDateDB(d[1]),
            "sequence": str(tmpNumsCol1[0]) + "-" + str(tmpNumsCol1[1]) + "-" + str(tmpNumsCol1[2]) + "-" + str(tmpNumsCol1[3]) + "-" + str(tmpNumsCol1[4]),
            "firstNum": str(tmpNumsCol1[0]),
            "secondNum": str(tmpNumsCol1[1]),
            "thirdNum": str(tmpNumsCol1[2]),
            "fourthNum" : str(tmpNumsCol1[3]),
            "fifthNum": str(tmpNumsCol1[4]),
            "cashBall": str(tmpNumsCol1[5])
        }
        filteredResultsCol1.append(colObj1)


        if 28 < len(d):

            tmpNumsCol2 = [int(d[29]), int(d[33]), int(d[37]), int(d[41]), int(d[45])]
            tmpNumsCol2.sort()
            tmpNumsCol2.append( int(d[49]))

            colObj2 = {
                    "date": fixDateDB(d[27]),
                    "sequence": str(tmpNumsCol2[0]) + "-" + str(tmpNumsCol2[1]) + "-" + str(tmpNumsCol2[2]) + "-" + str(tmpNumsCol2[3]) + "-" + str(tmpNumsCol2[4]),
                    "firstNum": str(tmpNumsCol2[0]),
                    "secondNum": str(tmpNumsCol2[1]),
                    "thirdNum": str(tmpNumsCol2[2]),
                    "fourthNum" : str(tmpNumsCol2[3]),
                    "fifthNum": str(tmpNumsCol2[4]),
                    "cashBall": str(tmpNumsCol2[5])
            }
            filteredResultsCol2.append(colObj2)

    else: 
        print('')

filteredResultsCol1.reverse()
filteredResultsCol2.reverse()

for x in filteredResultsCol2:
    master.append(x)

for x in filteredResultsCol1:
    master.append(x)


insertIntoDB(master)



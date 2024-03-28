# Run 1st and once


# Script for double tables

from bs4 import BeautifulSoup

from datetime import datetime
from datetime import timedelta

import requests

from functions import insertIntoDBPick2Day, insertIntoDBPick2Eve

URL = "https://jgoolsby.com/pick2.html"

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

# print(tablez[28], '  is tabe')

# target specific table
tab = tablez[28]

# find rows
rows = tab.find_all('tr')

daat = []

for l in rows:
    
    table_data = l.find_all('td')
    # print(table_data)
    data = [j.text for j in table_data]
    
    daat.append(data)

sliceObj = slice(14, 103)

slicedResults =  daat[sliceObj]

masterE = []
masterM = []

col2ArrE = []
col2ArrM = []

# middle column
for d in slicedResults:
    
    lengthh = len(d)

    if(len(d) > 22):
        spl = d[17].split()

        if(spl[0] == 'M'):
            col2ArrM.append({'date': d[15], 'num': d[19] + "" + d[23]})

        elif(spl[0] == 'E'):
            col2ArrE.append({'date': d[15], 'num': d[19] + "" + d[23]})


col2ArrM.reverse()
col2ArrE.reverse()

col1ArrE = []
col1ArrM = []

# # first column
for d in slicedResults:
  
    lengthh = len(d)

   
    if(d[3] != ''):

        spl = d[3].split()
        
        if(spl[0] == 'M'):
            col1ArrM.append({'date': d[1], 'num': d[5] + "" + d[9]})

        elif(spl[0] == 'E'):
                col1ArrE.append({'date': d[1], 'num': d[5] + "" + d[9]})

col1ArrM.reverse()
col1ArrE.reverse()

masterM = col2ArrM + col1ArrM
masterE = col2ArrE + col1ArrE

insertIntoDBPick2Day(masterM)
insertIntoDBPick2Eve(masterE)


# row1
# d[1] = date
# d[3] = timeframe
# d[5] = first number
# d[9] = second number

# row2
# d[15] = date2
# d[17] = timeframe
# d[19] = first number
# d[23] = second number











































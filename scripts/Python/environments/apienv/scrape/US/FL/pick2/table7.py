# only run on table 7

# Left Col
# d[1] = date
# d[3] = timeframe
# d[5] = first number
# d[9] = second number
# d[13] = fireBall

# Middle Col
# d[17] = date2
# d[19] = timeframe
# d[21] = first number
# d[25] = second number
# d[29] = fireBall

# Right Col
# d[33] = date3
# d[35] = timeframe
# d[37] = first number
# d[41] = second number
# d[45] = fireBall

# Right Col w/o FB
# d[33] = date3
# d[35] = timeframe
# d[37] = first number
# d[41] = second number

from bs4 import BeautifulSoup

from datetime import datetime, timedelta

import requests

from functions import insertIntoDBPick2DayFB, insertIntoDBPick2EveFB

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
tab = tablez[7]

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

col3ArrE = []
col3ArrM = []

# third column
for d in slicedResults:
    
    lengthh = len(d)
    
    # if array is not even minimal 25 length, return
    if( lengthh > 25):
        
        spl = d[35].split()

        if(lengthh == 49):

            if(spl[0] == 'M'):
                col3ArrM.append({'date': d[33], 'num': d[37] + "" + d[41], "fireBall": d[45]})

            elif(spl[0] == 'E'):
                col3ArrE.append({'date': d[33], 'num': d[37] + "" + d[41], "fireBall": d[45]})

        if(lengthh == 47):

             if(spl[0] == 'M'):
                col3ArrM.append({'date': d[33], 'num': d[37] + "" + d[41], "fireBall": '0'})

             elif(spl[0] == 'E'):
                col3ArrE.append({'date': d[33], 'num': d[37] + "" + d[41], "fireBall": '0'})

col3ArrM.reverse()
col3ArrE.reverse()

col2ArrE = []
col2ArrM = []

# middle column
for d in slicedResults:
    
    if( len(d) > 25):

        spl = d[19].split()

        if(spl[0] == 'M'):
            col2ArrM.append({'date': d[17], 'num': d[21] + "" + d[25], "fireBall": d[29]})

        elif(spl[0] == 'E'):
            col2ArrE.append({'date': d[17], 'num': d[21] + "" + d[25], "fireBall": d[29]})


col2ArrM.reverse()
col2ArrE.reverse()

col1ArrE = []
col1ArrM = []

# # first column
for d in slicedResults:
    
    if(len(d) > 25):

        spl = d[3].split()
        
        if(spl[0] == 'M'):
            col1ArrM.append({'date': d[1], 'num': d[5] + "" + d[9], "fireBall": d[13]})

        elif(spl[0] == 'E'):
            col1ArrE.append({'date': d[1], 'num': d[5] + "" + d[9], "fireBall": d[13]})

col1ArrM.reverse()
col1ArrE.reverse()

masterM = col3ArrM + col2ArrM + col1ArrM
masterE = col3ArrE + col2ArrE + col1ArrE

# insertIntoDBPick2DayFB(masterM)
# insertIntoDBPick2EveFB(masterE)

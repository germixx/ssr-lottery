# Script for double tables

from bs4 import BeautifulSoup

from datetime import datetime, timedelta

import requests

from functions import insertIntoDBPick4Day, insertIntoDBPick4Eve

URL = "https://jgoolsby.com/p4.htm"

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
    
# Parse website data
soup = BeautifulSoup(page.content, "html.parser")

# Get all data tables
tablez = soup.find_all("table")

masterE = []
masterM = []

for x in reversed(tablez):
    
    col3ArrE = []
    col1ArrE = []
    col2ArrE = []

    col1ArrM = []
    col2ArrM = []
    col3ArrM = []

    col1ArrMFB = []
    col2ArrMFB = []
    col3ArrMFB = []

    col1ArrEFB = []
    col2ArrEFB = []
    col3ArrEFB = []
    
    # find rows
    rows = x.find_all('tr')

    daat = []

    for l in rows:
    
        table_data = l.find_all('td')

        data = [j.text for j in table_data]
        
        daat.append(data) 

    sliceObj = slice(14, 103)

    slicedResults =  daat[sliceObj]

    for d in reversed(slicedResults):
        
        lengthh = len(d)

        if(d[1] != ''):
            
            if(lengthh  == 38):

                # COL 2 Nums date=d[19] timeframe=d[21] n1=d[23] n2=d[27] n3=d[31] n4=d[35]
                if(d[21] == 'M'):
                    col2ArrM.append({'date': d[19], 'num': d[23] + "" + d[27] + "" + d[31]})

                elif(d[21] == 'E'):
                    col2ArrE.append({'date': d[19], 'num': d[23] + "" + d[27] + "" + d[31]})

                # Col1 date=d[1] timeframe=d[3]  n1=d[5] n2=d[9] n3 d[13]
                if(d[3] == 'M'):
                    col1ArrM.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13]})

                elif(d[3] == 'E'):
                    col1ArrE.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13]}) 

            elif (lengthh == 55):

                # COL 3 Nums date=d[37] timeframe=d[39] n1=d[41] n2=d[45] n3=d[49] n4=d[53]
                if(d[39] == 'M'):
                    col3ArrM.append({'date': d[37], 'num': d[41] + "" + d[45] + "" + d[49]  + "" + d[53]})

                elif(d[39] == 'E'):
                    col3ArrE.append({'date': d[37], 'num': d[41] + "" + d[45] + "" + d[49] + "" + d[53]})     

                # COL 2 Nums date=d[19] timeframe=d[21] n1=d[23] n2=d[27] n3=d[31] n4=d[35]
                if(d[21] == 'M'):
                    col2ArrM.append({'date': d[19], 'num': d[23] + "" + d[27] + "" + d[31]  + "" + d[35]})

                elif(d[21] == 'E'):
                    col2ArrE.append({'date': d[19], 'num': d[23] + "" + d[27] + "" + d[31] + "" + d[35]})     

                # COL 1 Nums date=d[1] timeframe=d[3] n1=d[5] n2=d[9] n3=d[13] n4=d[17]
                if(d[3] == 'M'):
                    col1ArrM.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13]  + "" + d[17]})

                elif(d[3] == 'E'):
                    col1ArrE.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13] + "" + d[17]})          
             
            elif(lengthh == 67):

                # COL 3 Nums date=d[45] timeframe=d[47] n1=d[49] n2=d[53] n3=d[57] n4=d[61] FB = d[65]
                if(d[47] == 'M'):
                    col3ArrM.append({'date': d[45], 'num': d[49] + "" + d[53] + "" + d[57]  + "" + d[61], 'FB': d[65]})

                elif(d[47] == 'E'):
                    col3ArrE.append({'date': d[45], 'num': d[49] + "" + d[53] + "" + d[57] + "" + d[61], 'FB': d[65]})     

                # COL 2 Nums date=d[23] timeframe=d[25] n1=d[27] n2=d[31] n3=d[35] n4=d[39] FB=d[43] 
                if(d[25] == 'M'):
                    col2ArrM.append({'date': d[23], 'num': d[27] + "" + d[31] + "" + d[35]  + "" + d[39], 'FB': d[43]})

                elif(d[25] == 'E'):
                    col2ArrE.append({'date': d[23], 'num': d[27] + "" + d[31] + "" + d[35] + "" + d[39], 'FB': d[43]})     

                # COL 1 Nums date=d[1] timeframe=d[3] n1=d[5] n2=d[9] n3=d[13] n4=d[17] FB=d[21]
                if(d[3] == 'M'):
                    col1ArrM.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13]  + "" + d[17], 'FB': d[21]})

                elif(d[3] == 'E'):
                    col1ArrE.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13] + "" + d[17], 'FB': d[21]})          


    masterE = masterE + col3ArrE + col2ArrE + col1ArrE + col3ArrEFB + col2ArrEFB + col1ArrEFB
    masterM = masterM + col3ArrM + col2ArrM + col1ArrM + col3ArrMFB + col2ArrMFB + col1ArrMFB

# insertIntoDBPick4Day(masterM)
# insertIntoDBPick4Eve(masterE)





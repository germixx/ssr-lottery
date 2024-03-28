# Script for double tables

from bs4 import BeautifulSoup

from datetime import datetime, timedelta

import requests

from functions import insertIntoDBPick3Day, insertIntoDBPick3Eve

URL = "https://jgoolsby.com/p3.htm"

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

    singleTableCol1ArrM = []
    singleTableCol1ArrE = []

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

            # NUMs date=d[1] timeframe=d[3] n1=d[5] n2=d[9] n3=d[13]

            if (lengthh < 18):

                spl = d[3].split()

                if(spl[0] == 'M'):
                    singleTableCol1ArrM.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13]})

                elif(spl[0] == 'E'):
                    singleTableCol1ArrE.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13]})

            elif(lengthh == 49):

                # COL3 date=d[33] timeframe=d[35] n1=d[37] n2=d[41] n3=d[45]
                
                spl3 = d[35].split()
                if(spl3[0] == 'M'):
                    col3ArrM.append({'date': d[33], 'num': d[37] + "" + d[41] + "" + d[45]})

                elif(spl3[0] == 'E'):
                    col3ArrE.append({'date': d[33], 'num': d[37] + "" + d[41] + "" + d[45]})
                
                # COL2 date=d[17] timeframe=d[19] n1=d[21] n2=d[25] n3=d[29]
                
                spl2 = d[19].split()
                if(spl2[0] == 'M'):
                    col2ArrM.append({'date': d[17], 'num': d[21] + "" + d[25] + "" + d[29]})

                elif(spl2[0] == 'E'):
                    col2ArrE.append({'date': d[17], 'num': d[21] + "" + d[25] + "" + d[29]})

                # Col1 date=d[1] timeframe=d[3]  n1=d[5] n2=d[9] n3 d[13]
                
                spl1 = d[3].split()
                if(spl1[0] == 'M'):
                    col1ArrM.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13]})

                elif(spl1[0] == 'E'):
                    col1ArrE.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13]})          
            
            elif(lengthh == 53):
                
                # COL3 date=d[37] timeframe=d[39] n1=d[41] n2=d[45] n3=d[49]
                
                spl3n = d[39].split()
                if(spl3n[0] == 'M'):
                    col3ArrM.append({'date': d[37], 'num': d[41] + "" + d[45] + "" + d[49]})

                elif(spl3n[0] == 'E'):
                    col3ArrE.append({'date': d[37], 'num': d[41] + "" + d[45] + "" + d[49]})

                # COL2 date=d[19] timeframe=d[21] n1=d[23] n2=d[27] n3=d[31] FB=d[35]

                spl2n = d[21].split()
                if(spl2n[0] == 'M'):
                    col2ArrMFB.append({'date': d[19], 'num': d[23] + "" + d[27] + "" + d[31], 'FB': d[35]})

                elif(spl2n[0] == 'E'):
                    col2ArrEFB.append({'date': d[19], 'num': d[23] + "" + d[27] + "" + d[31], 'FB': d[35]})

                # COL1 date=d[1] timeframe=d[3] n1=d[5] n2=d[9] n3=d[13] FB=d[17]

                spl1n = d[3].split()
                if(spl1n[0] == 'M'):
                    col1ArrMFB.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13], 'FB': d[17]})

                elif(spl1n[0] == 'E'):
                    col1ArrEFB.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13], 'FB': d[17]})

            # FB below
            elif(lengthh == 55):
                
                # COL3 date=d[37] timeframe=d[39] n1=d[41]  n2=d[45] n3=d[49] FB=d[53]

                spl3fb = d[39].split()
                if(spl3fb[0] == 'M'):
                    col3ArrMFB.append({'date': d[37], 'num': d[41] + "" + d[45] + "" + d[49], 'FB': d[53]})

                elif(spl3fb[0] == 'E'):
                    col3ArrEFB.append({'date': d[37], 'num': d[41] + "" + d[45] + "" + d[49], 'FB': d[53]})

                
                # COL2 date=d[19] timeframe=d[21] n1=d[23] n2=d[27] n3=d[31] FB=d[35]
                
                spl2fb = d[21].split()
                if(spl2fb[0] == 'M'):
                    col2ArrMFB.append({'date': d[19], 'num': d[27] + "" + d[31] + "" + d[35], 'FB': d[35]})

                elif(spl2fb[0] == 'E'):
                    col2ArrEFB.append({'date': d[19], 'num': d[27] + "" + d[31] + "" + d[35], 'FB': d[35]})

                # COL1  date=d[1] timeframe=d[3] n1=d[5] n2=d[9] n3=d[13] FB=d[17]

                spl1fb = d[3].split()
                if(spl1fb[0] == 'M'):
                    col1ArrMFB.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13], 'FB': d[17]})

                elif(spl1fb[0] == 'E'):
                    col1ArrEFB.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13], 'FB': d[17]})
    
    masterE = masterE + singleTableCol1ArrE + col3ArrE + col2ArrE + col1ArrE + col3ArrEFB + col2ArrEFB + col1ArrEFB
    masterM = masterM + singleTableCol1ArrM + col3ArrM + col2ArrM + col1ArrM + col3ArrMFB + col2ArrMFB + col1ArrMFB
                
# insertIntoDBPick3Eve(masterE)
# insertIntoDBPick3Day(masterM)
# Script for double tables

from bs4 import BeautifulSoup

from datetime import datetime, timedelta

import requests

from functions import insertIntoDBPick5Day, insertIntoDBPick5Eve

URL = "https://jgoolsby.com/p5.htm"

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

# for x in tablez:
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

            if(lengthh == 25):
                
                spl = d[3].split()
                
                if(spl[0] == 'M'):
                    col1ArrM.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13] + "" + d[17]+ "" + d[21]})

                elif(spl[0] == 'E'):
                    col1ArrE.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13] + "" + d[17] + "" + d[21]}) 
            
            elif(lengthh == 49):
                
                spl2 = d[27].split()

                # Col2 date=d[]
                if(spl2[0] == 'M'):
                    col2ArrM.append({'date': d[25], 'num': d[29] + "" + d[33] + "" + d[37] + "" + d[41]+ "" + d[45]})

                elif(spl2[0] == 'E'):
                    col2ArrE.append({'date': d[25], 'num': d[29] + "" + d[33] + "" + d[37] + "" + d[41] + "" + d[45]}) 

                spl = d[3].split()
                # Col1 date=d[]
                if(spl[0] == 'M'):
                    col1ArrM.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13] + "" + d[17]+ "" + d[21]})

                elif(spl[0] == 'E'):
                    col1ArrE.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13] + "" + d[17] + "" + d[21]}) 

            elif(lengthh == 45):
                
                # Col2 date=d[23] timeframe=d[25] n1=d[27] n2=d[31] n3=d[35] n4=d[39] n5=d[44]
                spl2 = d[25].split()
                
                if(spl2[0] == 'M'):
                    col2ArrM.append({'date': d[23], 'num': d[27] + "" + d[31] + "" + d[35] + "" + d[39]+ "" + d[43]})

                elif(spl2[0] == 'E'):
                    
                    col2ArrE.append({'date': d[23], 'num': d[27] + "" + d[31] + "" + d[35] + "" + d[39] + "" + d[43]}) 

                spl = d[3].split()
                # Col1 date=d[1] timeframe=d[3] n1=d[5] n2=d[9] n3=d[13] n4=d[17] n5=d[21]
                if(spl[0] == 'M'):
                    col1ArrM.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13] + "" + d[17]+ "" + d[21]})

                elif(spl[0] == 'E'):
                    col1ArrE.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13] + "" + d[17] + "" + d[21]}) 

            elif(lengthh == 67):
                
                # Col3 date=d[45] timeframe=d[47] n1=d[49] n2=d[53] n3=d[57] n4=d[61] n5=d[65]
                spl3 = d[47].split()
                if(spl3[0] == 'M'):
                    # print(d[45], ' i s E', d[49])
                    col3ArrM.append({'date': d[45], 'num': d[49] + "" + d[53] + "" + d[57] + "" + d[61]+ "" + d[65]})

                elif(spl3[0] == 'E'):
                    col3ArrE.append({'date': d[45], 'num': d[49] + "" + d[53] + "" + d[57] + "" + d[61] + "" + d[65]}) 

                # Col2  date=d[23] timeframe=d[25] n1=d[27] n2=d[31] n3=d[35] n4=d[39] n5=d[43]
                spl2 = d[25].split()
                if(spl2[0] == 'M'):
                    col2ArrM.append({'date': d[23], 'num': d[27] + "" + d[31] + "" + d[35] + "" + d[39]+ "" + d[43]})

                elif(spl2[0] == 'E'):
                    col2ArrE.append({'date': d[23], 'num': d[27] + "" + d[31] + "" + d[35] + "" + d[39] + "" + d[43]}) 

                # Col1  date=d[1] timeframe=d[3] n1=d[5] n2=d[9] n3=d[13] n4=d[17] n5=d[21]
                spl = d[3].split()
                if(spl[0] == 'M'):
                    col1ArrM.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13] + "" + d[17]+ "" + d[21]})

                elif(spl[0] == 'E'):
                    col1ArrE.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13] + "" + d[17] + "" + d[21]}) 

            elif(lengthh == 73):
                
                # Col3 date=d[49] timeframe=d[51] n1=d[53] n2=d[57] n3=d[61] n4=d[65] n5=d[69]
                spl3 = d[51].split()
                if(spl3[0] == 'M'):
                    
                    col3ArrM.append({'date': d[49], 'num': d[53] + "" + d[57] + "" + d[61] + "" + d[65]+ "" + d[69]})

                elif(spl3[0] == 'E'):

                    col3ArrE.append({'date': d[49], 'num': d[53] + "" + d[57] + "" + d[61] + "" + d[65] + "" + d[69]}) 

                # Col2 date=d[25] timeframe=d[27] n1=d[29] n2=d[33] n3=d[37] n4=d[41] n5=d[45]
                spl2 = d[27].split()
                if(spl2[0] == 'M'):
                    
                    col2ArrM.append({'date': d[25], 'num': d[29] + "" + d[33] + "" + d[37] + "" + d[41]+ "" + d[45]})

                elif(spl2[0] == 'E'):
                    
                    col2ArrE.append({'date': d[25], 'num': d[29] + "" + d[33] + "" + d[37] + "" + d[41] + "" + d[45]}) 

                # Col1 date=d[1] timeframe=d[3] n1=d[5] n2=d[9] n3=d[13] n4=d[17] n5=d[21]
                spl = d[3].split()
                if(spl[0] == 'M'):
                    
                    col1ArrM.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13] + "" + d[17]+ "" + d[21]})

                elif(spl[0] == 'E'):

                    col1ArrE.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13] + "" + d[17] + "" + d[21]}) 

            elif(lengthh == 79):   

                # Col3 date=d[53] timeframe=d[55] n1=d[57] n2=d[61] n3=d[65] n4=d[69] n5=d[73] FB=d[77]
                spl3 = d[55].split()
                if(spl3[0] == 'M'):
                    
                    col3ArrM.append({'date': d[53], 'num': d[57] + "" + d[61] + "" + d[65] + "" + d[69]+ "" + d[73], 'FB': d[77]})

                elif(spl3[0] == 'E'):

                    col3ArrE.append({'date': d[53], 'num': d[57] + "" + d[61] + "" + d[65] + "" + d[69] + "" + d[73], 'FB': d[77]}) 

                # Col2 date=d[27] timeframe=d[29] n1=d[31] n2=d[35] n3=d[39] n4=d[43] n5=d[47] FB=[51]
                spl2 = d[3].split()
                if(spl2[0] == 'M'):
                    
                    col2ArrM.append({'date': d[27], 'num': d[31] + "" + d[35] + "" + d[39] + "" + d[43]+ "" + d[47], 'FB': d[51]})

                elif(spl2[0] == 'E'):

                    col2ArrE.append({'date': d[27], 'num': d[31] + "" + d[35] + "" + d[39] + "" + d[43] + "" + d[47], 'FB': d[51]}) 


                # Col1 date=d[1] timeframe=d[3] n1=d[5] n2=d[9] n3=d[13] n4=d[17] n5=d[21] FB=d[25]
                spl = d[3].split()
                if(spl[0] == 'M'):
                    
                    col1ArrM.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13] + "" + d[17]+ "" + d[21], 'FB': d[25]})

                elif(spl[0] == 'E'):

                    col1ArrE.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13] + "" + d[17] + "" + d[21], 'FB': d[25]}) 

    masterE = masterE + col3ArrE + col2ArrE + col1ArrE + col3ArrEFB + col2ArrEFB + col1ArrEFB     
    masterM = masterM + col3ArrM + col2ArrM + col1ArrM + col3ArrMFB + col2ArrMFB + col1ArrMFB

# insertIntoDBPick5Day(masterM)
# insertIntoDBPick5Eve(masterE)























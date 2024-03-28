from bs4 import BeautifulSoup

from datetime import datetime, timedelta

import requests

from functions import insertIntoDB

URL = "https://jgoolsby.com/pb.htm"

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
tablez = soup.find_all("table") # 32

master = []

for x in reversed(tablez):

    col1Arr = []
    col2Arr = []

    rows = x.find_all('tr')

    daat = []

    for l in rows:
    
        table_data = l.find_all('td')

        data = [j.text for j in table_data]
            
        daat.append(data) 

    sliceObj = slice(12, 103)

    slicedResults =  daat[sliceObj]

    for d in reversed(slicedResults):
        
        if(d[1] != ''):
            
            # Col1 date=d[1] n1=d[3] n2=d[7] n3=d[11] n4=d[15] n5=d[19] MB=d[23]
            if(len(d)  == 27):
                # print(d)
                cccc=0
                col1Arr.append( { 'date': d[1], 'num': str(d[3]) + "-" + str(d[7]) + "-" + str(d[11]) + "-" + str(d[15]) + "-" + str(d[19]) + " " + str(d[23]), 'n1': d[3], 'n2': d[7], 'n3': d[11], 'n4': d[15], 'n5': d[19], 'PB': d[23] })
                
            # Col2 date=d[27] n1=d=[29] n2=d[33] n3=d[37] n4=d[41] n5=d[45] MB=d[49]
            if(len(d) == 53):

                col2Arr.append( { 'date': d[27], 'num': str(d[29]) + "-" + str(d[33]) + "-" + str(d[37]) + "-" + str(d[41]) + "-" + str(d[45]) + " " + str(d[49]), 'n1': d[29], 'n2': d[33], 'n3': d[37], 'n4': d[41], 'n5': d[45], 'PB': d[49] })
                
                col1Arr.append( { 'date': d[1], 'num': str(d[3]) + "-" + str(d[7]) + "-" + str(d[11]) + "-" + str(d[15]) + "-" + str(d[19]) + " " + str(d[23]), 'n1': d[3], 'n2': d[7], 'n3': d[11], 'n4': d[15], 'n5': d[19], 'PB': d[23] })

    master = master + col2Arr + col1Arr

# insertIntoDB(master)
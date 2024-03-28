from bs4 import BeautifulSoup

from datetime import datetime, timedelta

import requests

from functions import insertIntoDB, filterResults

URL = "https://jgoolsby.com/lotto.htm"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
        'Accept-Language' : 'en-US,en;q=0.5', 
        'Accept-Encoding' : 'gzip, deflate', 
        'DNT' : '1', # Do Not Track Request Header 
        'Connection' : 'close'
}

def checkXtra(num):

    x = num.startswith('X')

    if x:
        return ''
    else:
        if (len(num) > 5):
            return 'DP'
        else: 
            return num


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

    singleTableArr = []
    
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
    
            lengthh = len(d)
            
            if(d[1] != ''):
                
                # Single Column
                if( lengthh == 27):
                
                    sorted = [int(d[3]), int(d[7]), int(d[11]), int(d[15]), int(d[19]), int(d[23])]
                
                    sorted.sort()
                    
                    singleTableArr.append({'date': d[1], 'num': str(sorted[0]) + "-" + str(sorted[1]) + "-" + str(sorted[2]) + "-" + str(sorted[3]) + "-" + str(sorted[4]) + "-" + str(sorted[5]), 'n1': sorted[0], 'n2': sorted[1], 'n3': sorted[2], 'n4': sorted[3], 'n5': sorted[4], 'n6': sorted[5], 'xtra': '' })

                # Double Column 
                # Col1 date=d[1] n1=d[3] n2=d[7] n3=d[11] n4=d[15] n5=d[19] n6=d[23] type=d[25]
                # Col2 date=d[27] n1=d[29] n2=d[33] n3=d[37] n4=d[41] n5=d[45] n6=d[49] type=d[51] 
                
                elif(lengthh == 53):

                    # COL 2
                    sorted = [int(d[29]), int(d[33]), int(d[37]), int(d[41]), int(d[45]), int(d[49])]
                    sorted.sort()
                    col2Arr.append({'date': d[27], 'num': str(sorted[0]) + "-" + str(sorted[1]) + "-" + str(sorted[2]) + "-" + str(sorted[3]) + "-" + str(sorted[4]) + "-" + str(sorted[5]), 'n1': sorted[0], 'n2': sorted[1], 'n3': sorted[2], 'n4': sorted[3], 'n5': sorted[4], 'n6': sorted[5], 'xtra': checkXtra(d[51])  })
                    
                    # COL 1
                    sorted2 = [int(d[3]), int(d[7]), int(d[11]), int(d[15]), int(d[19]), int(d[23])]
                    sorted2.sort()
                    col1Arr.append({'date': d[1], 'num': str(sorted2[0]) + "-" + str(sorted2[1]) + "-" + str(sorted2[2]) + "-" + str(sorted2[3]) + "-" + str(sorted2[4]) + "-" + str(sorted2[5]), 'n1': sorted2[0], 'n2': sorted2[1], 'n3': sorted2[2], 'n4': sorted2[3], 'n5': sorted2[4], 'n6': sorted2[5], 'xtra': checkXtra(d[25]) })

    master = master + singleTableArr + col2Arr + col1Arr    

filterResults(master)



















































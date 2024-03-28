from bs4 import BeautifulSoup

from datetime import datetime, timedelta

import requests

from functions import insertIntoDB

URL = "https://jgoolsby.com/jtp.htm"

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

master = []
singleTable = []

tab = tablez[0]

rows = tab.find_all('tr')

daat = []

for l in rows:
    
    table_data = l.find_all('td')
    # print(table_data)
    data = [j.text for j in table_data]
    
    daat.append(data)

sliceObj = slice(14, 101)

slicedResults =  daat[sliceObj]

# single table
# for d in reversed(slicedResults):
        
#         lengthh = len(d)
        
#         # print(len(d))
#         # Col1 date=d[1] n1=d[3] n2=d[7] n3=d[11] n4=d[15] n5=d[19] n6=d[23]
#         if(lengthh == 25):
                
#             singleTable.append({'date':d[1], 'num': d[3] + "-" + d[7] + "-" + d[11] + "-" + d[15] + "-" + d[19] + "-" + d[23], 'n1': d[3], 'n2': d[7], 'n3':d[11], 'n4': d[15], 'n5': d[19], 'n6': d[23] })

# insertIntoDB(singleTable)


col1arr = []
col2arr = []

for d in reversed(slicedResults):
        
        lengthh = len(d)

        
        col1arr.append({'date':d[1], 'num': d[3] + "-" + d[7] + "-" + d[11] + "-" + d[15] + "-" + d[19] + "-" + d[23], 'n1': d[3], 'n2': d[7], 'n3':d[11], 'n4': d[15], 'n5': d[19], 'n6': d[23] })

        # col2arr.append({'date':d[25], 'num': d[27] + "-" + d[31] + "-" + d[35] + "-" + d[39] + "-" + d[43] + "-" + d[47], 'n1': d[27], 'n2': d[31], 'n3':d[35], 'n4': d[39], 'n5': d[43], 'n6': d[47] })
        
        
        
        # Col1 date=d[1] n1=d[3] n2=d[7] n3=d[11] n4=d[15] n5=d[19] n6=d[23]
        # Col2 date=d[25] n1=d[27] n2=d[31] n3=d[35] n4=d[39] n5=d[43] n6=d[47]


# print(col1arr)
# insertIntoDB(col2arr)
insertIntoDB(col1arr)


































# for x in tablez:
# for x in reversed(tablez):
    

#     col1Arr = []
#     col2Arr = []

    
#     # find rows
#     rows = x.find_all('tr')

#     daat = []

#     for l in rows: 
    
#         table_data = l.find_all('td')

#         data = [j.text for j in table_data]
        
#         daat.append(data) 

#     sliceObj = slice(14, 103)

#     slicedResults =  daat[sliceObj]

#     for d in reversed(slicedResults):
#         print(d)
#         lengthh = len(d)
#         # print(singleTable)
#         if(d[1] != ''):
#             # print(len(d))
#             # Col1 date=d[1] n1=d[3] n2=d[7] n3=d[11] n4=d[15] n5=d[19] n6=d[23]
#             if(lengthh == 25):
                
#                 singleTable.append({'date':d[1], 'num': d[3] + "-" + d[7] + "-" + d[11] + "-" + d[15] + "-" + d[19] + "-" + d[23] })

#             # Col1 date=d[1] n1=d[3] n2=d[7] n3=d[11] n4=d[15] n5=d[19] n6=d[23]
#             # Col2 date=d[25] n1=d[27] n2=d[31] n3=d[35] n4=d[39] n5=d[43] n6=d[47]
#             elif(lengthh == 49):
#                 # print(d)
#                 col1Arr.append({'date':d[1], 'num': d[3] + "-" + d[7] + "-" + d[11] + "-" + d[15] + "-" + d[19] + "-" + d[23] })
#                 col1Arr.append({'date':d[25], 'num': d[27] + "-" + d[31] + "-" + d[35] + "-" + d[39] + "-" + d[43] + "-" + d[47] })

#     # master = singleTable + col2Arr + col1Arr


# print(singleTable)
# print(master)
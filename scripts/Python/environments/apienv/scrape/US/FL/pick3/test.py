
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
    
# # parse website data
soup = BeautifulSoup(page.content, "html.parser")

# # get all data tables
tablez = soup.find_all("table")
tab = tablez[8]
# print(tablez[112], ' is tables')
# print(tablez[28], '  is tabe')
masterE = []
masterM = []
col3ArrE = []
col3ArrM = []
col2ArrE = []
col2ArrM = []

col1ArrE = []
col1ArrM = []

# ---------------------TEST sections
tab = tablez[7]

# find rows
rows = tab.find_all('tr')

daat = []

for l in rows:
    
    table_data = l.find_all('td')
    # print(table_data)
    data = [j.text for j in table_data]
    
    daat.append(data)


sliceObj = slice(14, 104)

slicedResults =  daat[sliceObj]
masterE = []
masterM = []

col3ArrE = []
col3ArrM = []
col2ArrE = []
col2ArrM = []
col1ArrE = []
col1ArrM = []
# for one column, filled row 17
# for thrid col with FB empty row 28, filled row 55
# third column  empty row 25 , filled row 49   
# cycle through rows of TABLE
for d in reversed(slicedResults):
    # print(len(d), d)
    # row length
    lengthh = len(d)

    # # if row is not completely empty, continue
    if(d[1] != ''):
            print(lengthh, d)
    #     # Determine if one col or 3 by length
    #     if (lengthh < 18):

    #         # cycle through one time
  
    #         spl = d[3].split()

    #         if(spl[0] == 'M'):
    #             col1ArrM.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13]})

    #         elif(spl[0] == 'E'):
    #             col1ArrE.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13]})



    #     elif(lengthh == 49):
    #             #cycle through here 3 times:


    #             print(d)
            
    #         # FB below
    #     elif(lengthh == 55):
    #         print(d)
    #         #cycle through here 3 times



        

            
print(col1ArrE)        


# ------------------------------- end test section





# for x in reversed(tablez):
#     # print(x)
#     # find rows
#     rows = x.find_all('tr')

#     daat = []

#     for l in rows:
    
#         table_data = l.find_all('td')

#         # print(table_data)
#         data = [j.text for j in table_data]
        
#         daat.append(data) 

#     sliceObj = slice(14, 103)

#     slicedResults =  daat[sliceObj]

    # third column
    # for d in slicedResults:
        
    #     lengthh = len(d)
    #     try:
    #         if( lengthh > 25):

    #             spl = d[31].split()

    #             if(spl[0] == 'M'):
    #                 col3ArrM.append({'date': d[29], 'num': d[33] + "" + d[37] + "" + d[41]})

    #             elif(spl[0] == 'E'):
    #                 col3ArrE.append({'date': d[29], 'num': d[33] + "" + d[37] + "" + d[41]})
    #     except:
    #         continue
   
    # col3ArrM.reverse()
    # col3ArrE.reverse()


    # middle column
    # for d in slicedResults:
        
    #     lengthh = len(d)
    #     try: 
    #         if( len(d) > 25):
    #             spl = d[17].split()

    #             if(spl[0] == 'M'):
    #                 col2ArrM.append({'date': d[15], 'num': d[19] + "" + d[23] + "" + d[27]})

    #             elif(spl[0] == 'E'):
    #                 col2ArrE.append({'date': d[15], 'num': d[19] + "" + d[23] + "" + d[27]})
    #     except:
    #         continue

    #     col2ArrM.reverse()
    #     col2ArrE.reverse()


    # # # first column
    # for d in slicedResults:
            
    #     lengthh = len(d)
    #     try:
    #         if(len(d) > 25):
    #             spl = d[3].split()
                    
    #             if(spl[0] == 'M'):
    #                 col1ArrM.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13]})

    #             elif(spl[0] == 'E'):
    #                 col1ArrE.append({'date': d[1], 'num': d[5] + "" + d[9] + "" + d[13]})
    #     except:
    #         continue
    # col1ArrM.reverse()
    # col1ArrE.reverse()

# masterM = col3ArrM + col2ArrM + col1ArrM
# masterE = col3ArrE + col2ArrE + col1ArrE

# print(masterE)

    # insertIntoDBPick3Day(masterM)
# insertIntoDBPick3Eve(masterE)
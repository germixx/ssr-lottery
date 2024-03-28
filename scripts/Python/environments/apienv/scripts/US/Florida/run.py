# Script to pull results from FL Fantasy 5 database
# 
# 
# Steps
# query results from database
# 
# 
#  

from dbs import create_server_connection
from datetime import datetime
connection =  create_server_connection()
import requests
from bs4 import BeautifulSoup

URL = "https://lotto.jgoolsby.com/api/ff5/getAll"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
        'Accept-Language' : 'en-US,en;q=0.5', 
        'Accept-Encoding' : 'gzip, deflate', 
        'DNT' : '1', # Do Not Track Request Header 
        'Connection' : 'close'
    }

resp = requests.get(url=URL)

data = resp.json()

for x in data['rows']:

    print(x)

    mycursor = connection.cursor()

    sql = "INSERT INTO FLFantasy5 (date, sequence, n1, n2, n3, n4, n5, jackpot) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"

    dat = datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S.%fZ")

    val = (dat, x['sequence'], x['firstNum'], x['secondNum'], x['thirdNum'], x['fourthNum'], x['fifthNum'], 'null') 

    # print(val)

    mycursor.execute(sql, val)

    connection.commit()

    # return mycursor.lastrowid















# This script gets run daily

from bs4 import BeautifulSoup
import requests

from datetime import datetime, timedelta

from functions import fixDate, splits, InsertIntoDBCash4Life

URL = "https://www.flalottery.com/cash4Life"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
        'Accept-Language' : 'en-US,en;q=0.5', 
        'Accept-Encoding' : 'gzip, deflate', 
        'DNT' : '1', # Do Not Track Request Header 
        'Connection' : 'close'}


# get site
page = requests.get(URL, headers = headers)

# parse data
soup = BeautifulSoup(page.content, "html.parser")

gameNumb = soup.find_all('div', class_="gamePageNumbers")

# start here getting date from results
daterr = gameNumb[0].find_all('p')
thePlayDate = daterr[3].text

# get all the number balls
results = soup.find_all("span", class_="balls")

pos1 = results[0].text
pos2 = results[1].text
pos3 = results[2].text
pos4 = results[3].text
pos5 = results[4].text
cashBall = results[5].text

winningNumbers = pos1 + "-" + pos2 + "-" + pos3 + "-" + pos4 + "-" + pos5

obj = {
    "result": {
        "date": fixDate(thePlayDate),
        "numbers": [{
            "n1": pos1,
            "n2": pos2,
            "n3": pos3,
            "n4": pos4,
            "n5": pos5,
      "cashBall": cashBall
        }],
        "sequence": winningNumbers 
    }
}

InsertIntoDBCash4Life(obj)

# Opening a file
file1 = open('/home/jgoolsby/api/lottery-api/scripts/Python/environments/apienv/scripts/US/Florida/logs/cash4life.txt', 'a')
s = "Script successfully ran on " + thePlayDate + "\n"
  
# # Writing a string to file
file1.write(s) 
    
# # Closing file
file1.close()

# #!/usr/bin/python

from datetime import datetime

from dbs import create_server_connection

connection =  create_server_connection()

def fixDateforDB(dat):
    gg = datetime.strptime(dat, '%M/%d/%y').strftime("%M/%d/%Y")
    hh = gg.split('/')
    return hh[2] + "-" + hh[0] + "-" + hh[1] + " 00:00:00"

def insertIntoDB(result):

    mycursor = connection.cursor()

    for x in result:
       
        sql = "INSERT INTO FLJackpotTriplePlay (date, sequence, firstNum, secondNum, thirdNum, fourthNum, fifthNum, sixthNum) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"

        # val = (fixDateforDB(x["date"]), x["num"], x['n1'], x['n2'], x['n3'], x['n4'], x['n5'], x['n6']) 
        # print(val)
        # mycursor.execute(sql, val)

        # connection.commit()


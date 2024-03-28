from dbs import create_server_connection

from datetime import datetime

connection =  create_server_connection()

def fixDateforDB(dat):
    gg = datetime.strptime(dat, '%M/%d/%y').strftime("%M/%d/%Y")
    hh = gg.split('/')
    return hh[2] + "-" + hh[0] + "-" + hh[1] + " 00:00:00"

def insertIntoDBPick5Day(result):

    mycursor = connection.cursor()

    for x in result:
        
        my_list = [int(x) for x in str(x["num"])]

        if "FB" in x:
            FB = x["FB"]
        else:
            FB = 0

        sql = "INSERT INTO FLPick5Day (date, sequence, firstNum, secondNum, thirdNum, fourthNum, fifthNum, fireBall) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"

        val = (fixDateforDB(x["date"]), x["num"], my_list[0], my_list[1], my_list[2], my_list[3], my_list[4], FB) 

        mycursor.execute(sql, val)

        connection.commit()


def insertIntoDBPick5Eve(result):

    mycursor = connection.cursor()

    for x in result:
        
        my_list = [int(x) for x in str(x["num"])]

        if "FB" in x:
            FB = x["FB"]
        else:
            FB = 0
        
        sql = "INSERT INTO FLPick5Eve (date, sequence, firstNum, secondNum, thirdNum, fourthNum, fifthNum, fireBall) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"

        val = (fixDateforDB(x["date"]), x["num"], my_list[0], my_list[1], my_list[2], my_list[3], my_list[4], FB) 

        mycursor.execute(sql, val)

        connection.commit()


from dbs import create_server_connection

from datetime import datetime

connection =  create_server_connection()

def fixDateforDB(dat):
    gg = datetime.strptime(dat, '%M/%d/%y').strftime("%M/%d/%Y")
    hh = gg.split('/')
    return hh[2] + "-" + hh[0] + "-" + hh[1] + " 00:00:00"

def insertIntoDBPick3Day(result):

    mycursor = connection.cursor()

    for x in result:
        
        my_list = [int(x) for x in str(x["num"])]

        if "FB" in x:
            FB = x["FB"]
        else:
            FB = 0

        sql = "INSERT INTO FLPick3Day (date, sequence, firstNum, secondNum, thirdNum, fireBall) VALUES ( %s, %s, %s, %s, %s, %s)"

        val = (fixDateforDB(x["date"]), x["num"], my_list[0], my_list[1], my_list[2], FB) 

        mycursor.execute(sql, val)

        connection.commit()

def insertIntoDBPick3Eve(result):

    mycursor = connection.cursor()

    for x in result:
                
        my_list = [int(x) for x in str(x["num"])]

        if "FB" in x:
            FB = x["FB"]
        else:
            FB = 0

        sql = "INSERT INTO FLPick3Eve (date, sequence, firstNum, secondNum, thirdNum, fireBall) VALUES ( %s, %s, %s, %s, %s, %s )"

        val = (fixDateforDB(x["date"]), x["num"], my_list[0], my_list[1], my_list[2], FB) 

        mycursor.execute(sql, val)

        connection.commit()


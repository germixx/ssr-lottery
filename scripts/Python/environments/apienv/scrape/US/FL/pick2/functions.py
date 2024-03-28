from dbs import create_server_connection

from datetime import datetime

connection =  create_server_connection()

def fixDateforDB(dat):
    gg = datetime.strptime(dat, '%M/%d/%y').strftime("%M/%d/%Y")
    hh = gg.split('/')
    return hh[2] + "-" + hh[0] + "-" + hh[1] + " 00:00:00"

def insertIntoDBPick2Day(result):
    
    mycursor = connection.cursor()

    for x in result:
        
        my_list = [int(x) for x in str(x["num"])]

        sql = "INSERT INTO FLPick2Day (date, sequence, firstNum, secondNum, fireBall) VALUES ( %s, %s, %s, %s, %s)"

        val = (fixDateforDB(x["date"]), x["num"], my_list[0], my_list[1], '0') 

        mycursor.execute(sql, val)

        connection.commit()


def insertIntoDBPick2Eve(result):

    mycursor = connection.cursor()

    for x in result:
        
        my_list = [int(x) for x in str(x["num"])]
        
        sql = "INSERT INTO FLPick2Eve (date, sequence, firstNum, secondNum, fireBall) VALUES ( %s, %s, %s, %s, %s)"

        val = (fixDateforDB(x["date"]), x["num"], my_list[0], my_list[1], '0') 

        mycursor.execute(sql, val)

        connection.commit()


def insertIntoDBPick2DayFB(result):

    mycursor = connection.cursor()

    for x in result:

        my_list = [int(x) for x in str(x["num"])]

        sql = "INSERT INTO FLPick2Day (date, sequence, firstNum, secondNum, fireBall) VALUES ( %s, %s, %s, %s, %s)"

        val = (fixDateforDB(x["date"]), x["num"], my_list[0], my_list[1], x["fireBall"]) 

        mycursor.execute(sql, val)

        connection.commit()


def insertIntoDBPick2EveFB(result):
    # print(result)
    
    mycursor = connection.cursor()

    for x in result:

        my_list = [int(x) for x in str(x["num"])]

        sql = "INSERT INTO FLPick2Eve (date, sequence, firstNum, secondNum, fireBall) VALUES ( %s, %s, %s, %s, %s)"

        val = (fixDateforDB(x["date"]), x["num"], my_list[0], my_list[1], x["fireBall"]) 

        mycursor.execute(sql, val)

        connection.commit()

# #!/usr/bin/python
from dbs import create_server_connection

connection =  create_server_connection()

def insertIntoDB(result):

    mycursor = connection.cursor()

    for x in result:
        
        sql = "INSERT INTO FLcash4life (date, sequence, firstNum, secondNum, thirdNum, fourthNum, fifthNum, cashBall) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"

        val = (x["date"], x["sequence"], x["firstNum"], x["secondNum"], x["thirdNum"], x["fourthNum"], x["fifthNum"], x["cashBall"]) 

        mycursor.execute(sql, val)

        connection.commit()


# #!/usr/bin/python

from datetime import datetime

from dbs import create_server_connection

connection =  create_server_connection()

mycursor = connection.cursor()

def fixDateforDB(dat):

    gg = datetime.strptime(dat, '%M/%d/%y').strftime("%M/%d/%Y")
    
    hh = gg.split('/')
    
    return hh[2] + "-" + hh[0] + "-" + hh[1] + " 00:00:00"

def updateDBByDate(res):
    
    for y in res:
        
        sql = "UPDATE FLlotto SET dp=%s, dpn1=%s, dpn2=%s, dpn3=%s, dpn4=%s, dpn5=%s, dpn6=%s WHERE date = %s"

        val = (y["num"], y['n1'], y['n2'], y['n3'], y['n4'], y['n5'], y['n6'], fixDateforDB(y["date"]) )

        mycursor.execute(sql, val)
        
        connection.commit()

def insertIntoDB(result):

    for x in result:
        
        sql = "INSERT INTO FLlotto (date, sequence, firstNum, secondNum, thirdNum, fourthNum, fifthNum, sixthNum, dp, dpn1, dpn2, dpn3, dpn4, dpn5, dpn6) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        val = (fixDateforDB(x["date"]), x["num"], x['n1'], x['n2'], x['n3'], x['n4'], x['n5'], x['n6'], '0', '0', '0', '0', '0', '0', '0') 
        
        mycursor.execute(sql, val)

        connection.commit()

def filterResults(res):

    LOTTO = []
    
    DP = []

    for x in res:
        
        if(x["xtra"] == 'DP'):
            DP.append(x)
        else:
            LOTTO.append(x)
        
    # insertIntoDB(LOTTO)
    # updateDBByDate(DP)


# pass all results to function -
# filter results -
# insert LOTTO results into DB
# then cycle through the DP numbers and insert by date

# columns DP DPn1 DPn2 DPn3 DPn4 DPn5 DPn6
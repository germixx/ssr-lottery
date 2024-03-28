from dbs import create_server_connection, connection2

connection =  create_server_connection()

def splits(word):
    return [char for char in word]
        
def fixDate(date):
    
    def adjustMth(month):
        match month:
            case 'January':
                return '01'
            case 'February':
                return '02'
            case 'March':
                return '03'
            case 'April':
                return '04'
            case 'May':
                return '05'
            case 'June':
                return '06'
            case 'July':
                return '07'
            case 'August':
                return '08'
            case 'September':
                return '09'
            case 'October':
                return '10'
            case 'November':
                return '11'
            case 'December':
                return '12'

    def fixDay(day):
        match str(day):
            case '1':
                return '01'
            case '2':
                return '02'
            case '3':
                return '03'
            case '4':
                return '04'
            case '5':
                return '05'
            case '6':
                return '06'
            case '7':
                return '07'
            case '8':
                return '08'                        
            case '9':
                return '09'
            case _:
                return day


    dateSplit = date.split()    
    year = dateSplit[3]
    month =   adjustMth(dateSplit[1])
    day = fixDay(dateSplit[2].replace(',', '') )
    sqlDate = f'{year}-{month}-{fixDay(day)}' + ' 00:00:00'
    return sqlDate

def InsertIntoDBCash4Life(object):
    
    mycursor = connection.cursor()

    sql = "INSERT INTO FLcash4life (date, sequence, firstNum, secondNum, thirdNum, fourthNum, fifthNum, cashBall) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (object['result']['date'], object['result']['sequence'], object['result']['numbers'][0]['n1'], object['result']['numbers'][0]['n2'], object['result']['numbers'][0]['n3'], object['result']['numbers'][0]['n4'], object['result']['numbers'][0]['n5'], object['result']['numbers'][0]['cashBall']) 

    mycursor.execute(sql, val)

    connection.commit()

    return mycursor.lastrowid

########################### Fantasy 5 ############################## 
def InsertIntoDBFantasy5(object):
    
    mycursor = connection.cursor()

    sql = "INSERT INTO FLFantasy5 (date, sequence, n1, n2, n3, n4, n5, jackpot) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (object['result']['date'], object['result']['sequence'], object['result']['numbers'][0]['n1'], object['result']['numbers'][0]['n2'], object['result']['numbers'][0]['n3'], object['result']['numbers'][0]['n4'], object['result']['numbers'][0]['n5'], object['result']['jackpot']) 

    mycursor.execute(sql, val)

    connection.commit()

    return mycursor.lastrowid

def getPattern(seq):

    seqArr = seq.split('-')
    
    patternArr = []

    def identifyPattern(num):

        if(1 <= num <= 9):
            return 'A'
        
        if(10 <= num <= 19):
            return 'B'
        
        if(20 <= num <= 29):
            return 'C'
        
        if(30 <= num <= 36):
            return 'D'

    for y in seqArr:

            patternArr.append(identifyPattern(int(y)))
    return ''.join(patternArr)

def getSubPattern(seq):
    
    def identifyPattern(p):
        
        if(1 <= p <= 5):
            return 'A1'

        if(6 <= p <= 9):
            return 'A2'

        if(10 <= p <= 14):
            return 'B1'

        if(15 <= p <= 19):
            return 'B2'

        if(20 <= p <= 24):
            return 'C1'

        if(25 <= p <= 29):
            return 'C2'

        if(30 <= p <= 32):
            return 'D1'

        if(33 <= p <= 36):
            return 'D2'

    seqArr = seq.split('-')
    
    patternArr = []

    for y in seqArr:
        patternArr.append(identifyPattern(int(y)))

    return ''.join(patternArr)


def getDoubles(seq):

    arr = []

    def adjustPattern(num1, num2):
        
        kk = max(int(num1), int(num2))
        jj = min(int(num1), int(num2))

        return str(jj) + "-" + str(kk)

    seqArr = seq.split('-')

    nm = adjustPattern( seqArr[0], seqArr[1] )
    nm2 = adjustPattern( seqArr[0] , seqArr[2] )
    nm3 = adjustPattern(seqArr[0] , seqArr[3] )
    nm4 = adjustPattern( seqArr[0] , seqArr[4] )
    nm5 = adjustPattern( seqArr[1] , seqArr[2] )
    nm6 = adjustPattern( seqArr[1] , seqArr[3])
    nm7 = adjustPattern( seqArr[1] , seqArr[4] )
    nm8 = adjustPattern( seqArr[2] , seqArr[3] )
    nm9 = adjustPattern( seqArr[2] , seqArr[4] )
    nm10 = adjustPattern( seqArr[3] , seqArr[4] )

    arr.append(nm)
    arr.append(nm2)
    arr.append(nm3)
    arr.append(nm4)
    arr.append(nm5)
    arr.append(nm6) 
    arr.append(nm7)
    arr.append(nm8)
    arr.append(nm9) 
    arr.append(nm10) 

    return arr

def getTriples(seq):

        seqArr = seq.split('-')

        arr = []

        tr = seqArr[0] + "-" + seqArr[1] + "-" + seqArr[2]
        tr1 = seqArr[0] + "-" + seqArr[1] + "-" + seqArr[3] 
        tr2 = seqArr[0] + "-" + seqArr[1] + "-" + seqArr[4]
        tr3 = seqArr[0] + "-" + seqArr[2] + "-" + seqArr[3]
        tr4 = seqArr[0] + "-" + seqArr[2] + "-" + seqArr[4]
        tr5 = seqArr[0] + "-" + seqArr[3] + "-" + seqArr[4]
        tr6 = seqArr[1] + "-" + seqArr[2] + "-" + seqArr[3]
        tr7 = seqArr[1] + "-" + seqArr[2] + "-" + seqArr[4]
        tr8 = seqArr[1] + "-" + seqArr[3] + "-" + seqArr[4]
        tr9 = seqArr[2] + "-" + seqArr[3] + "-" + seqArr[4]
        
        arr.append(tr)
        arr.append(tr1)
        arr.append(tr2)
        arr.append(tr3)
        arr.append(tr4)
        arr.append(tr5)
        arr.append(tr6)
        arr.append(tr7)
        arr.append(tr8)
        arr.append(tr9)

        return arr
    
def updatePatternCount(pattern):

    connPat = connection2('patterns')
    
    mycursor = connPat.cursor()

    sql1 = "SELECT count FROM FLFantasy5 WHERE pattern = %s"

    val1 = (pattern, )

    mycursor.execute(sql1, val1)

    myresult = mycursor.fetchone()

    if myresult == None:

        mycursor.reset()

        sql = "INSERT INTO FLFantasy5 (pattern, count) VALUES (%s, %s)"
        
        val = (pattern, 1)
        
        mycursor.execute(sql, val)

        connPat.commit()
        
    else:
        mycursor.reset()

        newResult = myresult[0] + 1

        sqls = "UPDATE FLFantasy5 SET count = %s WHERE pattern = %s"

        val = (newResult, pattern)

        mycursor.execute(sqls, val)

        connPat.commit()

def updateSubPattern(sub, pattern):

    connSubPat = connection2('subPatterns')

    mycursor = connSubPat.cursor()

    s = "SELECT count FROM FLFantasy5 WHERE subPattern = %s"

    q = (sub, )

    mycursor.execute(s, q)

    myresult = mycursor.fetchone()

    if myresult == None:

        mycursor.reset()

        sql = "INSERT INTO FLFantasy5 (pattern, subPattern, count) VALUES (%s, %s, %s)"
        
        val = (pattern, sub, 1)
        
        mycursor.execute(sql, val)

        connSubPat.commit()
        
    else:

        mycursor.reset()

        newResult = myresult[0] + 1

        sqls = "UPDATE FLFantasy5 SET count = %s WHERE subPattern = %s"

        val = (newResult, sub)

        mycursor.execute(sqls, val)

        connSubPat.commit()

def updateDoubles(dbl):

    conndbl = connection2('doubles')

    mycursor = conndbl.cursor(buffered=True)

    for x in dbl:
              
        sql1 = "SELECT count FROM FLFantasy5 WHERE doubles = %s"

        val1 = (x, )

        mycursor.execute(sql1, val1)

        myresult = mycursor.fetchone()
        
        if myresult == None:

            mycursor.reset()

            spl = x.split('-')
            
            sql = "INSERT INTO FLFantasy5 (doubles, n1, n2, count) VALUES ( %s, %s, %s, %s )"
            
            val = ( x, spl[0], spl[1], 1 )
            
            mycursor.execute(sql, val)

            conndbl.commit()
        
        else:

            mycursor.reset()

            newResult = myresult[0] + 1

            sqls = "UPDATE FLFantasy5 SET count = %s WHERE doubles = %s"

            val = (newResult, x)

            mycursor.execute(sqls, val)

            conndbl.commit()

def updateTriples(trpl):

    connTrips = connection2('triples')
    
    mycursor = connTrips.cursor()

    for x in trpl:
                
        sql1 = "SELECT count FROM FLFantasy5 WHERE triples = %s"

        val1 = (x, )

        mycursor.execute(sql1, val1)

        myresult = mycursor.fetchone()

        if myresult == None:

            mycursor.reset()

            spl = x.split('-')

            sql = "INSERT INTO FLFantasy5 (triples, n1, n2, n3, count) VALUES ( %s, %s, %s, %s, %s )"
            
            val = ( x, spl[0], spl[1], spl[2], 1 )
            
            mycursor.execute(sql, val)

            connTrips.commit()
        
        else:

            mycursor.reset()

            newResult = myresult[0] + 1

            sqls = "UPDATE FLFantasy5 SET count = %s WHERE triples = %s"

            val = (newResult, x)

            mycursor.execute(sqls, val)

            connTrips.commit()

def F5AddStats(seq):

    pat = getPattern(seq)
    
    updatedPat = updatePatternCount(pat)
    
    subPat = getSubPattern(seq)
    updatedSubPat = updateSubPattern(subPat, pat)

    dbls = getDoubles(seq)
    updatedDbls = updateDoubles(dbls)

    trpls = getTriples(seq)
    updatedTrip = updateTriples(trpls)

    return True

# Pick 2
def InsertIntoDBFLPick2Eve(object):
    
    mycursor = connection.cursor()

    sql = "INSERT INTO FLPick2Eve (date, sequence, firstNum, secondNum, fireBall) VALUES ( %s, %s, %s, %s, %s )"

    val = (object['result']['date'], object['result']['sequence'], object['result']['n1'], object['result']['n2'], object['result']['fireBall']) 

    mycursor.execute(sql, val)

    connection.commit()

    return mycursor.lastrowid

def InsertIntoDBFLPick2Day(object):
    
    mycursor = connection.cursor()

    sql = "INSERT INTO FLPick2Day (date, sequence, firstNum, secondNum, fireBall) VALUES ( %s, %s, %s, %s, %s )"

    val = (object['result']['date'], object['result']['sequence'], object['result']['n1'], object['result']['n2'], object['result']['fireBall']) 

    mycursor.execute(sql, val)

    connection.commit()

    return mycursor.lastrowid

# Pick 3
def InsertIntoDBFLPick3Day(object):

    mycursor = connection.cursor()

    sql = "INSERT INTO FLPick3Day (date, sequence, firstNum, secondNum, thirdNum, fireBall) VALUES ( %s, %s, %s, %s, %s, %s)"

    val = (object['result']['date'], object['result']['sequence'], object['result']['n1'], object['result']['n2'], object['result']['n3'], object['result']['fireBall']) 

    mycursor.execute(sql, val)

    connection.commit()

    return mycursor.lastrowid


def InsertIntoDBFLPick3Eve(object):

    mycursor = connection.cursor()

    sql = "INSERT INTO FLPick3Eve (date, sequence, firstNum, secondNum, thirdNum, fireBall) VALUES ( %s, %s, %s, %s, %s, %s)"

    val = (object['result']['date'], object['result']['sequence'], object['result']['n1'], object['result']['n2'], object['result']['n3'], object['result']['fireBall']) 

    mycursor.execute(sql, val)

    connection.commit()

    return mycursor.lastrowid

# Pick 4
def InsertIntoDBFLPick4Day(object):
    
    mycursor = connection.cursor()

    sql = "INSERT INTO FLPick4Day (date, sequence, firstNum, secondNum, thirdNum, fourthNum, fireBall) VALUES ( %s, %s, %s, %s, %s, %s, %s)"

    val = (object['result']['date'], object['result']['sequence'], object['result']['n1'], object['result']['n2'], object['result']['n3'], object['result']['n4'], object['result']['fireBall'], ) 

    mycursor.execute(sql, val)

    connection.commit()

    return mycursor.lastrowid

def InsertIntoDBFLPick4Eve(object):
    
    mycursor = connection.cursor()

    sql = "INSERT INTO FLPick4Eve (date, sequence, firstNum, secondNum, thirdNum, fourthNum, fireBall) VALUES ( %s, %s, %s, %s, %s, %s, %s)"

    val = (object['result']['date'], object['result']['sequence'], object['result']['n1'], object['result']['n2'], object['result']['n3'], object['result']['n4'], object['result']['fireBall'], )  

    mycursor.execute(sql, val)

    connection.commit()

    return mycursor.lastrowid


# Pick 5
def InsertIntoDBFLPick5Day(object):
    
    mycursor = connection.cursor()

    sql = "INSERT INTO FLPick5Day (date, sequence, firstNum, secondNum, thirdNum, fourthNum, fifthNum, fireBall) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (object['result']['date'], object['result']['sequence'], object['result']['n1'], object['result']['n2'], object['result']['n3'], object['result']['n4'], object['result']['n5'], object['result']['fireBall']) 

    mycursor.execute(sql, val)

    connection.commit()

    return mycursor.lastrowid

def InsertIntoDBFLPick5Eve(object):
    
    mycursor = connection.cursor()

    sql = "INSERT INTO FLPick5Eve (date, sequence, firstNum, secondNum, thirdNum, fourthNum, fifthNum, fireBall) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (object['result']['date'], object['result']['sequence'], object['result']['n1'], object['result']['n2'], object['result']['n3'], object['result']['n4'], object['result']['n5'], object['result']['fireBall']) 

    mycursor.execute(sql, val)

    connection.commit()

    return mycursor.lastrowid
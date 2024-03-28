from dbs import connection2

connPattern =  connection2('patterns')
connSubPattern = connection2('subPatterns')
connDoubles = connection2('doubles')
connTriples = connection2('triples')

def updatePattern(patArr):

    # grab value from database
    # increment 1 and insert new value
    print(patArr,' pahj')

def updateSubPattern(subArr):
    print(subArr)

def updateDoubles(doubArr):
    print(doubArr)

def updateTriples(tripArr):
    print(tripArr)

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

def F5Stats():
    
    seq = "16-28-30-35-36"

    pat = getPattern(seq)
    updatePattern(pat)

    subPat = getSubPattern(seq)
    updateSubPattern(subPat)

    dbls = getDoubles(seq)
    updateDoubles(dbls)

    trpls = getTriples(seq)
    updateTriples(trpls)

F5Stats()
globalCountry = ''
globalDate = ''
globalTime = ''
globalLeagua = ''
globalLeaguaRound = ''
globalLeaguaKindOgFinal = ''

def parseTitle(content):
    global globalCountry
    global globalLeagua
    global globalLeaguaRound
    global globalLeaguaKindOgFinal

    keyWordCountry = '<span class="description__country">'
    positionOfKeyWordCountry = content.find(keyWordCountry)+len(keyWordCountry)
    endOfKeyWordCountry = content.find(':', positionOfKeyWordCountry)
    globalCountry = content[positionOfKeyWordCountry:endOfKeyWordCountry]

    keyWordLeague = ';">'
    keyWordLeagueEnd = '</a>'
    positionOfKeyWordLeague = content.find(keyWordLeague, positionOfKeyWordCountry) + len(keyWordLeague)
    positionOfKeyWordLeagueEnd = content.find(keyWordLeagueEnd, positionOfKeyWordLeague)
    subContent = content[positionOfKeyWordLeague:positionOfKeyWordLeagueEnd]
    listRound = subContent.split(' - ')

    if len(listRound) == 1 :
        globalLeagua = listRound[0]
    elif len(listRound) == 2:
        globalLeagua = listRound[0]
        globalLeaguaRound = listRound[1]
    elif len(listRound) == 3:
        globalLeagua = listRound[0]
        globalLeaguaRound = listRound[1]
        globalLeaguaKindOgFinal = listRound[2]

def parseDateTime(content):
    global globalDate
    global globalTime
    keyWordDateTime = '="description__time">'
    positionOfKeyWordDateTime = content.find(keyWordDateTime) + len(keyWordDateTime)
    date = content[positionOfKeyWordDateTime:positionOfKeyWordDateTime+10]
    time = content[positionOfKeyWordDateTime+11:positionOfKeyWordDateTime+16]
    globalDate = date
    globalTime = time

def parseMatchSummary():
    pass

def parseScore(content):
    pass

if __name__=='__main__':
    # path = 'Statistics\ADE 4-3 BRI _ Adelaide United - Brisbane Roar _ Match Summary.html'
    path = 'Statistics\HUN 1-2 SVK _ Hungary - Slovakia _ Match Summary.html'
    file = open(path)
    content = file.read()
    parseTitle(content)
    parseDateTime(content)
    print(globalDate)
    print(globalTime)
    print(globalCountry)
    print(globalLeagua)
    print(globalLeaguaRound)
    print(globalLeaguaKindOgFinal)


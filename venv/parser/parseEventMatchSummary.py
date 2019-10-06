globalCountry = ''
globalDate = ''
globalTime = ''
globalLeagua = ''
globalLeaguaRound = ''
globalLeaguaKindOfFinal = ''

def parseTitle(content):
    global globalCountry
    global globalLeagua
    global globalLeaguaRound
    global globalLeaguaKindOfFinal

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
        globalLeaguaKindOfFinal = listRound[2]

def parseDateTime(content):
    global globalDate
    global globalTime
    keyWordDateTime = '="description__time">'
    positionOfKeyWordDateTime = content.find(keyWordDateTime) + len(keyWordDateTime)
    date = content[positionOfKeyWordDateTime:positionOfKeyWordDateTime+10]
    time = content[positionOfKeyWordDateTime+11:positionOfKeyWordDateTime+16]
    globalDate = date
    globalTime = time

def parseTimeOfGoal(content, period):
    keyWordIncident = 'detailMS__incidentRow incidentRow--'
    keyWordGoal = 'icon soccer-ball'
    keyWordTimeOfGoal = '<div class="time-box">'
    keyWordTimeOfGoalEnd = "'</div>"
    keyWordGoleodor = 'participant-name'
    keyWordPlayerTech = '/player/'
    keyWordAssistant = 'assist note-name'

    print(period + ' ' + str(content.count(keyWordGoal)))

    countOfGoals = content.count(keyWordGoal)

    positionOfKeyWordGoal = content.find(keyWordGoal)

    if positionOfKeyWordGoal != -1:

        positionOfKeyWordHomeAway = content.rfind(keyWordIncident, 0, positionOfKeyWordGoal) + len(keyWordIncident)

        while countOfGoals !=0:
            team = content[positionOfKeyWordHomeAway:positionOfKeyWordHomeAway+4] # Team - home/away
            print(team)
            positionOfKeyWordTimeOfGoal = content.rfind(keyWordTimeOfGoal, 0, positionOfKeyWordGoal)+len(keyWordTimeOfGoal)
            timeOfGoal = content[positionOfKeyWordTimeOfGoal:content.find(keyWordTimeOfGoalEnd, positionOfKeyWordTimeOfGoal)] #Time of goal

            if team == 'home':
                # goleodor part
                positionOfGoleodor = content.find(keyWordGoleodor, positionOfKeyWordGoal)
                positionOfKeyWordGoleodorTech = content.find(keyWordPlayerTech, positionOfGoleodor) + len(keyWordPlayerTech)
                positionOfKeyWordPlayerTechEnd = content.find('/', positionOfKeyWordGoleodorTech)
                print('Goal - ' + str(content[positionOfKeyWordGoleodorTech:positionOfKeyWordPlayerTechEnd]))
                positionOfKeyWordGoal = content.find(keyWordGoal, positionOfKeyWordGoal+len(keyWordGoal))

                # assistant part
                positionOfAsist = content.find(keyWordAssistant,  positionOfKeyWordHomeAway, positionOfKeyWordGoal)
                if positionOfAsist != -1:
                    positionOfKeyWordAsistTech = content.find(keyWordPlayerTech, positionOfAsist) + len(keyWordPlayerTech)
                    positionOfKeyWordAsistTechEnd = content.find('/', positionOfKeyWordAsistTech)
                    print('Assist - ' + str(content[positionOfKeyWordAsistTech:positionOfKeyWordAsistTechEnd]))
                pass
            else:
                positionOfGoleodor = content.find(keyWordGoleodor, positionOfKeyWordGoal)
                positionOfKeyWordGoleodorTech = content.find(keyWordPlayerTech, positionOfGoleodor) + len(keyWordPlayerTech)
                positionOfKeyWordPlayerTechEnd = content.find('/', positionOfKeyWordGoleodorTech)
                print('Goal - ' + str(content[positionOfKeyWordGoleodorTech:positionOfKeyWordPlayerTechEnd]))
                positionOfKeyWordGoal = content.find(keyWordGoal, positionOfKeyWordGoal + len(keyWordGoal))

                positionOfAsist = content.find(keyWordAssistant, positionOfKeyWordHomeAway, positionOfGoleodor)

                if positionOfAsist != -1:
                    positionOfKeyWordAsistTech = content.find(keyWordPlayerTech, positionOfAsist) + len(keyWordPlayerTech)
                    positionOfKeyWordAsistTechEnd = content.find('/', positionOfKeyWordAsistTech)
                    print('Assist - ' + str(content[positionOfKeyWordAsistTech:positionOfKeyWordAsistTechEnd]))

            positionOfKeyWordHomeAway = content.rfind(keyWordIncident, 0, positionOfKeyWordGoal+len(keyWordIncident)) + len(keyWordIncident)

            # print(content[positionOfKeyWordTimeOfGoal:content.find(keyWordTimeOfGoalEnd, positionOfKeyWordTimeOfGoal)])
            print(timeOfGoal)

            countOfGoals -= 1

def parseIncidents(content):

    keyWordIncidentFirstHalf = 'detailMS__incidentsHeader stage-12'
    keyWordIncidentSecondHalf = 'detailMS__incidentsHeader stage-13'
    keyWordIncidentExtraTime = 'detailMS__incidentsHeader stage-6'
    keyWordIncidentPenalties = 'detailMS__incidentsHeader stage-7'

    if content.count(keyWordIncidentExtraTime) == 0 and content.count(keyWordIncidentPenalties) == 0: #Match without penalties and extratime
        positionOfKeyWordIncidentFirstHalf = content.find(keyWordIncidentFirstHalf)+len(keyWordIncidentFirstHalf)
        positionOfKeyWordIncidentFirstHalfEnd = content.find(keyWordIncidentSecondHalf)
        positionOfKeyWordIncidentSecondHalf = content.find(keyWordIncidentSecondHalf)+len(keyWordIncidentSecondHalf)
        subContentFirstHalf = content[positionOfKeyWordIncidentFirstHalf:positionOfKeyWordIncidentFirstHalfEnd]
        subContentSecondHalf = content[positionOfKeyWordIncidentSecondHalf:]
        parseTimeOfGoal(subContentFirstHalf, 'First half')
        parseTimeOfGoal(subContentSecondHalf, 'Second half')
    elif content.count(keyWordIncidentPenalties) == 0 and content.count(keyWordIncidentExtraTime) == 1: #Match without penalties, but with extratime
        positionOfKeyWordIncidentFirstHalf = content.find(keyWordIncidentFirstHalf) + len(keyWordIncidentFirstHalf)
        positionOfKeyWordIncidentFirstHalfEnd = content.find(keyWordIncidentSecondHalf)
        positionOfKeyWordIncidentSecondHalf = content.find(keyWordIncidentSecondHalf) + len(keyWordIncidentSecondHalf)
        positionOfKeyWordIncidentSecondHalfEnd = content.find(keyWordIncidentExtraTime)
        positionOfKeyWordIncidentExtraTime = content.find(keyWordIncidentExtraTime)+len(keyWordIncidentExtraTime)
        subContentFirstHalf = content[positionOfKeyWordIncidentFirstHalf:positionOfKeyWordIncidentFirstHalfEnd]
        subContentSecondHalf = content[positionOfKeyWordIncidentSecondHalf:positionOfKeyWordIncidentSecondHalfEnd]
        subContentExtraTime = content[positionOfKeyWordIncidentExtraTime:]
        parseTimeOfGoal(subContentFirstHalf, 'First half')
        parseTimeOfGoal(subContentSecondHalf, 'Second half')
        parseTimeOfGoal(subContentExtraTime, 'Extra time')
    elif content.count(keyWordIncidentExtraTime) == 0 and conent.count(keyWordIncidentPenalties) == 1: #Match without extratime, but with penalties
        positionOfkeyWordIncidentFirstHalf = content.find(keyWordIncidentFirstHalf) + len(keyWordIncidentFirstHalf)
        positionOfkeyWordIncidentFirstHalfEnd = content.find(keyWordIncidentSecondHalf)
        positionOfKeyWordIncidentSecondHalf = content.find(keyWordIncidentSecondHalf) + len(keyWordIncidentSecondHalf)
        positionOfKeyWordIncidentSecondHalfEnd = content.find(keyWordIncidentPenalties)
        positionOfKeyWordIncidentPenalties = content.find(keyWordIncidentPenalties) + len(keyWordIncidentPenalties)
        subContentFirstHalf = content[positionOfkeyWordIncidentFirstHalf:positionOfkeyWordIncidentFirstHalfEnd]
        subContentSecondHalf = content[positionOfKeyWordIncidentSecondHalf:positionOfKeyWordIncidentSecondHalfEnd]
        subContentPenalties = content[positionOfKeyWordIncidentPenalties:]
        parseTimeOfGoal(subContentFirstHalf, 'First half')
        parseTimeOfGoal(subContentSecondHalf, 'Second half')
        parseTimeOfGoal(subContentPenalties, 'Penalties')
    else: #match with penalties and with Extratime
        positionOfkeyWordIncidentFirstHalf = content.find(keyWordIncidentFirstHalf) + len(keyWordIncidentFirstHalf)
        positionOfkeyWordIncidentFirstHalfEnd = content.find(keyWordIncidentSecondHalf)
        positionOfKeyWordIncidentSecondHalf = content.find(keyWordIncidentSecondHalf) + len(keyWordIncidentSecondHalf)
        positionOfKeyWordIncidentSecondHalfEnd = content.find(keyWordIncidentExtraTime)
        positionOfKeyWordIncidentExtraTime = content.find(keyWordIncidentExtraTime) + len(keyWordIncidentExtraTime)
        positionOfKeyWordIncidentExtraTimeEnd = content.find(keyWordIncidentPenalties)
        positionOfKeyWordIncidentPenalties = content.find(keyWordIncidentPenalties) + len(keyWordIncidentPenalties)
        subContentFirstHalf = content[positionOfkeyWordIncidentFirstHalf:positionOfkeyWordIncidentFirstHalfEnd]
        subContentSecondHalf = content[positionOfKeyWordIncidentSecondHalf:positionOfKeyWordIncidentSecondHalfEnd]
        subContentExtraTime = content[positionOfKeyWordIncidentExtraTime:positionOfKeyWordIncidentExtraTimeEnd]
        subContentPenalties = content[positionOfKeyWordIncidentPenalties:]
        parseTimeOfGoal(subContentFirstHalf, 'First half')
        parseTimeOfGoal(subContentSecondHalf, 'Second half')
        parseTimeOfGoal(subContentExtraTime, 'Extra time')
        parseTimeOfGoal(subContentPenalties, 'Penalties')

def parseScore(content):
    matchStatus = '<div class="info-status mstat">'
    matchStatusEnd = '</div>'
    fullTime = '<span class="ft">' # checkForAdditionalTime

    if content.find(fullTime) == -1:
        positionOfHomeScore = content.find('<span class="scoreboard">') + len('<span class="scoreboard">')
        positionOfHomeScoreEnd = content.find('</span>', positionOfHomeScore)
        print('Home score full time - ' + str(content[positionOfHomeScore:positionOfHomeScoreEnd]))
        positionOfAwayScore = content.find('<span class="scoreboard">', positionOfHomeScore) + len('<span class="scoreboard">')
        positionOfAwayScoreEnd = content.find('</span>', positionOfAwayScore)
        print('Away score full time - ' + str(content[positionOfAwayScore:positionOfAwayScoreEnd]))

        positionOfMatchStatus = content.find(matchStatus) + len(matchStatus)
        positionOfMatchStatusEnd = content.find(matchStatusEnd)
        print(content[positionOfMatchStatus:positionOfMatchStatusEnd])

    else:
        positionOfHomeFinalScore = content.find('<span class="scoreboard">') + len('<span class="scoreboard">')
        positionOfHomeFinalScoreEnd = content.find('</span>', positionOfHomeFinalScore)
        print('Home score full time - ' + str(content[positionOfHomeFinalScore:positionOfHomeFinalScoreEnd]))
        positionOfAwayFinalScore = content.find('<span class="scoreboard">', positionOfHomeFinalScore) + len('<span class="scoreboard">')
        positionOfAwayFinalScoreEnd = content.find('</span>', positionOfAwayFinalScore)
        print('Away score full time - ' + str(content[positionOfAwayFinalScore:positionOfAwayFinalScoreEnd]))

        positionOfHomeScore = content.find('<span class="scoreboard">', content.find(fullTime)) + len('<span class="scoreboard">')
        positionOfHomeScoreEnd = content.find('</span>', positionOfHomeScore)
        print('Home final score - ' + str(content[positionOfHomeScore:positionOfHomeScoreEnd]))
        positionOfAwayScore = content.find('<span class="scoreboard">', positionOfHomeScore) + len('<span class="scoreboard">')
        positionOfAwayScoreEnd = content.find('</span>', positionOfAwayScore)
        print('Away final score - ' + str(content[positionOfAwayScore:positionOfAwayScoreEnd]))

        positionOfMatchStatus = content.find(matchStatus) + len(matchStatus)
        positionOfMatchStatusEnd = content.find(matchStatusEnd)
        print(content[positionOfMatchStatus:positionOfMatchStatusEnd])

if __name__=='__main__':
    path = 'Statistics\ADE 4-3 BRI _ Adelaide United - Brisbane Roar _ Match Summary.html'
    # path = 'Statistics\HUN 1-2 SVK _ Hungary - Slovakia _ Match Summary.html'
    # path = 'Statistics\POL 1-2 POR _ Poland - Portugal _ Match Summary.html'
    file = open(path)
    content = file.read()
    # parseTitle(content)
    # parseDateTime(content)
    parseIncidents(content)
    parseScore(content)



    # print(globalDate)
    # print(globalTime)
    # print(globalCountry)
    # print(globalLeagua)
    # print(globalLeaguaRound)
    # print(globalLeaguaKindOfFinal)


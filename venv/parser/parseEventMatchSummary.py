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

def parseMissedPenalties(content, period):
    keyWordIncident = 'detailMS__incidentRow incidentRow--'
    keyWordMissedPenalties = 'icon penalty-missed'
    keyWordTimeOfGoal = '<div class="time-box">'
    keyWordTimeOfGoalEnd = "'</div>"
    keyWordGoleodor = 'participant-name'
    keyWordPlayerTech = '/player/'

    print(period + ' ' + str(content.count(keyWordMissedPenalties)))

    countOfGoals = content.count(keyWordMissedPenalties)

    positionOfkeyWordMissedPenalties = content.find(keyWordMissedPenalties)

    if positionOfkeyWordMissedPenalties != -1: # if it is goal in period

        positionOfKeyWordHomeAway = content.rfind(keyWordIncident, 0, positionOfkeyWordMissedPenalties) + len(keyWordIncident)

        while countOfGoals !=0:
            team = content[positionOfKeyWordHomeAway:positionOfKeyWordHomeAway+4] # Team - home/away
            print(team)
            positionOfKeyWordTimeOfGoal = content.rfind(keyWordTimeOfGoal, 0, positionOfkeyWordMissedPenalties)+len(keyWordTimeOfGoal)
            timeOfGoal = content[positionOfKeyWordTimeOfGoal:content.find(keyWordTimeOfGoalEnd, positionOfKeyWordTimeOfGoal)] #Time of goal

            if team == 'home':
                # goleodor part
                positionOfGoleodor = content.find(keyWordGoleodor, positionOfkeyWordMissedPenalties)
                positionOfKeyWordGoleodorTech = content.find(keyWordPlayerTech, positionOfGoleodor) + len(keyWordPlayerTech)
                positionOfKeyWordPlayerTechEnd = content.find('/', positionOfKeyWordGoleodorTech)
                goleodor = content[positionOfKeyWordGoleodorTech:positionOfKeyWordPlayerTechEnd]
                positionOfGoleodorNormalName = content.find('return false;">', positionOfKeyWordPlayerTechEnd) + len('return false;">')
                positionOfGoleodorNormalNameEnd = content.find('</a></span>', positionOfGoleodorNormalName)
                goleodorNormalName = content[positionOfGoleodorNormalName:positionOfGoleodorNormalNameEnd]
                goleodorTechCode = content[content.find('return false;">', positionOfKeyWordPlayerTechEnd)-17:
                                           content.find('return false;">', positionOfKeyWordPlayerTechEnd)-9]

                print('Missed penalty - ' + goleodor + ' ' + goleodorNormalName + ' ' + goleodorTechCode)
                positionOfkeyWordMissedPenalties = content.find(keyWordMissedPenalties, positionOfkeyWordMissedPenalties+len(keyWordMissedPenalties)) # ++ for itteration
            else:
                positionOfGoleodor = content.find(keyWordGoleodor, positionOfkeyWordMissedPenalties)
                positionOfKeyWordGoleodorTech = content.find(keyWordPlayerTech, positionOfGoleodor) + len(keyWordPlayerTech)
                positionOfKeyWordPlayerTechEnd = content.find('/', positionOfKeyWordGoleodorTech)
                goleodor = content[positionOfKeyWordGoleodorTech:positionOfKeyWordPlayerTechEnd]
                positionOfGoleodorNormalName = content.find('return false;">', positionOfKeyWordPlayerTechEnd) + len('return false;">')
                positionOfGoleodorNormalNameEnd = content.find('</a></span>', positionOfGoleodorNormalName)
                goleodorNormalName = content[positionOfGoleodorNormalName:positionOfGoleodorNormalNameEnd]
                goleodorTechCode = content[content.find('return false;">', positionOfKeyWordPlayerTechEnd) - 17:
                                           content.find('return false;">', positionOfKeyWordPlayerTechEnd) - 9]

                print('Missed penalty - ' + goleodor + ' ' + goleodorNormalName + ' ' + goleodorTechCode)
                positionOfkeyWordMissedPenalties = content.find(keyWordMissedPenalties, positionOfkeyWordMissedPenalties + len(keyWordMissedPenalties)) # ++ for itteration

            positionOfKeyWordHomeAway = content.rfind(keyWordIncident, 0, positionOfkeyWordMissedPenalties+len(keyWordIncident)) + len(keyWordIncident)
            print(timeOfGoal)
            countOfGoals -= 1 # -- move iterrator for while

def parseCards(content, period, keyWordCard):
    keyWordIncident = 'detailMS__incidentRow incidentRow--'
    keyWordTimeOfCard = '<div class="time-box">'
    keyWordTimeOfCardEnd = "'</div>"
    keyWordCardHolder = 'participant-name'
    keyWordPlayerTech = '/player/'

    if keyWordCard == 'icon y-card':
        countOfCards = content.count(keyWordCard)
        positionOfKeyWordCard = content.find(keyWordCard)
        print(keyWordCard)
    elif keyWordCard == 'icon yr-card':
        countOfCards = content.count(keyWordCard)
        positionOfKeyWordCard = content.find(keyWordCard)
        print(keyWordCard)
    else:
        countOfCards = content.count(keyWordCard)
        positionOfKeyWordCard = content.find(keyWordCard)
        print(keyWordCard)

    if positionOfKeyWordCard != -1:  # if it is goal in period
        print(positionOfKeyWordCard)

        positionOfKeyWordHomeAway = content.rfind(keyWordIncident, 0, positionOfKeyWordCard) + len(keyWordIncident)

        while countOfCards != 0:
            team = content[positionOfKeyWordHomeAway:positionOfKeyWordHomeAway + 4]
            print(team)
            positionOfKeyWordTimeOfCard = content.rfind(keyWordTimeOfCard, 0, positionOfKeyWordCard) + len(keyWordTimeOfCard)
            timeOfCard = content[positionOfKeyWordTimeOfCard:content.find(keyWordTimeOfCardEnd, positionOfKeyWordTimeOfCard)]  # Time of goal

            if team == 'home':
                # goleodor part
                positionOfCardHolder = content.find(keyWordCardHolder, positionOfKeyWordCard)
                positionOfKeyWordCardHolderTech = content.find(keyWordPlayerTech, positionOfCardHolder) + len(keyWordPlayerTech)
                positionOfKeyWordPlayerTechEnd = content.find('/', positionOfKeyWordCardHolderTech)
                cardHolder = content[positionOfKeyWordCardHolderTech:positionOfKeyWordPlayerTechEnd]
                positionOfCardHolderNormalName = content.find('return false;">', positionOfKeyWordPlayerTechEnd) + len('return false;">')
                positionOfCardHolderNormalNameEnd = content.find('</a></span>', positionOfCardHolderNormalName)
                cardHolderNormalName = content[positionOfCardHolderNormalName:positionOfCardHolderNormalNameEnd]
                cardHolderTechCode = content[content.find('return false;">', positionOfKeyWordPlayerTechEnd)-17:
                                           content.find('return false;">', positionOfKeyWordPlayerTechEnd)-9]

                print(keyWordCard + ' ' + cardHolder + ' ' + cardHolderNormalName + ' ' + cardHolderTechCode)

                positionOfKeyWordCard = content.find(keyWordCard, positionOfKeyWordCard+len(keyWordCard)) # ++ for itteration

            else:
                positionOfCardHolder = content.find(keyWordCardHolder, positionOfKeyWordCard)
                positionOfKeyWordCardHolderTech = content.find(keyWordPlayerTech, positionOfCardHolder) + len(keyWordPlayerTech)
                positionOfKeyWordPlayerTechEnd = content.find('/', positionOfKeyWordCardHolderTech)
                cardHolder = content[positionOfKeyWordCardHolderTech:positionOfKeyWordPlayerTechEnd]
                positionOfCardHolderNormalName = content.find('return false;">', positionOfKeyWordPlayerTechEnd) + len('return false;">')
                positionOfCardHolderNormalNameEnd = content.find('</a></span>', positionOfCardHolderNormalName)
                cardHolderNormalName = content[positionOfCardHolderNormalName:positionOfCardHolderNormalNameEnd]
                cardHolderTechCode = content[content.find('return false;">', positionOfKeyWordPlayerTechEnd) - 17:
                                           content.find('return false;">', positionOfKeyWordPlayerTechEnd) - 9]

                print(keyWordCard + ' ' + cardHolder + ' ' + cardHolderNormalName + ' ' + cardHolderTechCode)
                positionOfKeyWordCard = content.find(keyWordCard, positionOfKeyWordCard + len(keyWordCard)) # ++ for itteration

            positionOfKeyWordHomeAway = content.rfind(keyWordIncident, 0, positionOfKeyWordCard+len(keyWordIncident)) + len(keyWordIncident)
            print(timeOfCard)
            countOfCards -= 1  # -- move iterrator for while


def parseGoals(content, period):
    keyWordIncident = 'detailMS__incidentRow incidentRow--'
    keyWordGoal = 'icon soccer-ball'
    keyWordGoalPenalty = 'Penalty'
    keyWordTimeOfGoal = '<div class="time-box">'
    keyWordTimeOfGoalEnd = "'</div>"
    keyWordGoleodor = 'participant-name'
    keyWordPlayerTech = '/player/'
    keyWordAssistant = 'assist note-name'

    print(period + ' ' + str(content.count(keyWordGoal)))

    countOfGoals = content.count(keyWordGoal)

    positionOfKeyWordGoal = content.find(keyWordGoal)

    if positionOfKeyWordGoal != -1: # if it is goal in period

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
                goleodor = content[positionOfKeyWordGoleodorTech:positionOfKeyWordPlayerTechEnd]
                positionOfGoleodorNormalName = content.find('return false;">', positionOfKeyWordPlayerTechEnd) + len('return false;">')
                positionOfGoleodorNormalNameEnd = content.find('</a></span>', positionOfGoleodorNormalName)
                goleodorNormalName = content[positionOfGoleodorNormalName:positionOfGoleodorNormalNameEnd]
                goleodorTechCode = content[content.find('return false;">', positionOfKeyWordPlayerTechEnd)-17:
                                           content.find('return false;">', positionOfKeyWordPlayerTechEnd)-9]

                ownGoal = content[positionOfKeyWordGoal + len(keyWordGoal):positionOfKeyWordGoal + len(keyWordGoal) + 4]

                kindOfGoal = 'Goal - '
                if ownGoal == '-own':
                    kindOfGoal = 'Own goal - '

                print(kindOfGoal + goleodor + ' ' + goleodorNormalName + ' ' + goleodorTechCode)

                positionOfKeyWordGoal = content.find(keyWordGoal, positionOfKeyWordGoal+len(keyWordGoal)) # ++ for itteration

                # assistant part
                positionOfAsist = content.find(keyWordAssistant,  positionOfKeyWordHomeAway, positionOfKeyWordGoal)

                if positionOfAsist != -1:
                    positionOfKeyWordAssistTech = content.find(keyWordPlayerTech, positionOfAsist) + len(keyWordPlayerTech)
                    positionOfKeyWordAssistTechEnd = content.find('/', positionOfKeyWordAssistTech)
                    assistant = content[positionOfKeyWordAssistTech:positionOfKeyWordAssistTechEnd]

                    positionOfAssistantNormalName = content.find('return false;">', positionOfKeyWordAssistTechEnd) + len('return false;">')
                    positionOfAssistantNormalNameEnd = content.find('</a>)</span>', positionOfAssistantNormalName)
                    assistantNormalName = content[positionOfAssistantNormalName:positionOfAssistantNormalNameEnd]
                    assistantTechCode = content[content.find('return false;">', positionOfKeyWordAssistTechEnd) - 17:
                                                content.find('return false;">', positionOfKeyWordAssistTechEnd) - 9]
                    print('Assist - ' + assistant + ' ' + assistantNormalName + ' ' + assistantTechCode)

                # penaltie part
                positionOfPenalty = content.find(keyWordGoalPenalty,  positionOfKeyWordHomeAway, positionOfKeyWordGoal)

                if positionOfPenalty != -1:
                    penalty = content[positionOfPenalty:positionOfPenalty+7]
                    print(penalty)

            else:
                positionOfGoleodor = content.find(keyWordGoleodor, positionOfKeyWordGoal)
                positionOfKeyWordGoleodorTech = content.find(keyWordPlayerTech, positionOfGoleodor) + len(keyWordPlayerTech)
                positionOfKeyWordPlayerTechEnd = content.find('/', positionOfKeyWordGoleodorTech)
                goleodor = content[positionOfKeyWordGoleodorTech:positionOfKeyWordPlayerTechEnd]
                positionOfGoleodorNormalName = content.find('return false;">', positionOfKeyWordPlayerTechEnd) + len('return false;">')
                positionOfGoleodorNormalNameEnd = content.find('</a></span>', positionOfGoleodorNormalName)
                goleodorNormalName = content[positionOfGoleodorNormalName:positionOfGoleodorNormalNameEnd]
                goleodorTechCode = content[content.find('return false;">', positionOfKeyWordPlayerTechEnd) - 17:
                                           content.find('return false;">', positionOfKeyWordPlayerTechEnd) - 9]

                ownGoal = content[positionOfKeyWordGoal + len(keyWordGoal):positionOfKeyWordGoal + len(keyWordGoal) + 4]

                kindOfGoal = 'Goal - '
                if ownGoal == '-own':
                    kindOfGoal = 'Own goal - '

                print(kindOfGoal + goleodor + ' ' + goleodorNormalName + ' ' + goleodorTechCode)

                positionOfKeyWordGoal = content.find(keyWordGoal, positionOfKeyWordGoal + len(keyWordGoal)) # ++ for itteration

                positionOfAsist = content.find(keyWordAssistant, positionOfKeyWordHomeAway, positionOfGoleodor)
                if positionOfAsist != -1:
                    positionOfKeyWordAssistTech = content.find(keyWordPlayerTech, positionOfAsist) + len(keyWordPlayerTech)
                    positionOfKeyWordAssistTechEnd = content.find('/', positionOfKeyWordAssistTech)
                    assistant = content[positionOfKeyWordAssistTech:positionOfKeyWordAssistTechEnd]

                    positionOfAssistantNormalName = content.find('return false;">', positionOfKeyWordAssistTechEnd) + len('return false;">')
                    positionOfAssistantNormalNameEnd = content.find('</a>)</span>', positionOfAssistantNormalName)
                    assistantNormalName = content[positionOfAssistantNormalName:positionOfAssistantNormalNameEnd]
                    assistantTechCode = content[content.find('return false;">', positionOfKeyWordAssistTechEnd) - 17:
                                                content.find('return false;">', positionOfKeyWordAssistTechEnd) - 9]
                    print('Assist - ' + assistant + ' ' + assistantNormalName + ' ' + assistantTechCode)

                # penaltie part
                positionOfPenalty = content.find(keyWordGoalPenalty, positionOfKeyWordHomeAway, positionOfKeyWordGoal)

                if positionOfPenalty != -1:
                    penalty = content[positionOfPenalty:positionOfPenalty + 7]
                    print(penalty)



            positionOfKeyWordHomeAway = content.rfind(keyWordIncident, 0, positionOfKeyWordGoal+len(keyWordIncident)) + len(keyWordIncident)
            print(timeOfGoal)
            countOfGoals -= 1 # -- move iterrator for while

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
        # parseGoals(subContentFirstHalf, 'First half')
        # parseGoals(subContentSecondHalf, 'Second half')
        # parseMissedPenalties(subContentFirstHalf, 'First half')
        # parseMissedPenalties(subContentSecondHalf, 'Second half')

        parseCards(subContentFirstHalf, 'First half', 'icon y-card')
        parseCards(subContentFirstHalf, 'First half', 'icon yr-card')
        parseCards(subContentFirstHalf, 'First half', 'icon r-card')

        parseCards(subContentSecondHalf, 'Second half', 'icon y-card')
        parseCards(subContentSecondHalf, 'Second half', 'icon yr-card')
        parseCards(subContentSecondHalf, 'Second half', 'icon r-card')

    elif content.count(keyWordIncidentPenalties) == 0 and content.count(keyWordIncidentExtraTime) == 1: #Match without penalties, but with extratime
        positionOfKeyWordIncidentFirstHalf = content.find(keyWordIncidentFirstHalf) + len(keyWordIncidentFirstHalf)
        positionOfKeyWordIncidentFirstHalfEnd = content.find(keyWordIncidentSecondHalf)
        positionOfKeyWordIncidentSecondHalf = content.find(keyWordIncidentSecondHalf) + len(keyWordIncidentSecondHalf)
        positionOfKeyWordIncidentSecondHalfEnd = content.find(keyWordIncidentExtraTime)
        positionOfKeyWordIncidentExtraTime = content.find(keyWordIncidentExtraTime)+len(keyWordIncidentExtraTime)
        subContentFirstHalf = content[positionOfKeyWordIncidentFirstHalf:positionOfKeyWordIncidentFirstHalfEnd]
        subContentSecondHalf = content[positionOfKeyWordIncidentSecondHalf:positionOfKeyWordIncidentSecondHalfEnd]
        subContentExtraTime = content[positionOfKeyWordIncidentExtraTime:]
        # parseGoals(subContentFirstHalf, 'First half')
        # parseGoals(subContentSecondHalf, 'Second half')
        # parseGoals(subContentExtraTime, 'Extra time')
        # parseMissedPenalties(subContentFirstHalf, 'First half')
        # parseMissedPenalties(subContentSecondHalf, 'Second half')
        # parseMissedPenalties(subContentExtraTime, 'Extra time')
        parseCards(subContentFirstHalf, 'First half')
    elif content.count(keyWordIncidentExtraTime) == 0 and conent.count(keyWordIncidentPenalties) == 1: #Match without extratime, but with penalties
        positionOfkeyWordIncidentFirstHalf = content.find(keyWordIncidentFirstHalf) + len(keyWordIncidentFirstHalf)
        positionOfkeyWordIncidentFirstHalfEnd = content.find(keyWordIncidentSecondHalf)
        positionOfKeyWordIncidentSecondHalf = content.find(keyWordIncidentSecondHalf) + len(keyWordIncidentSecondHalf)
        positionOfKeyWordIncidentSecondHalfEnd = content.find(keyWordIncidentPenalties)
        positionOfKeyWordIncidentPenalties = content.find(keyWordIncidentPenalties) + len(keyWordIncidentPenalties)
        subContentFirstHalf = content[positionOfkeyWordIncidentFirstHalf:positionOfkeyWordIncidentFirstHalfEnd]
        subContentSecondHalf = content[positionOfKeyWordIncidentSecondHalf:positionOfKeyWordIncidentSecondHalfEnd]
        subContentPenalties = content[positionOfKeyWordIncidentPenalties:]
        # parseGoals(subContentFirstHalf, 'First half')
        # parseGoals(subContentSecondHalf, 'Second half')
        # parseGoals(subContentPenalties, 'Penalties')
        # parseMissedPenalties(subContentFirstHalf, 'First half')
        # parseMissedPenalties(subContentSecondHalf, 'Second half')
        # parseMissedPenalties(subContentPenalties, 'Penalties')
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
        # parseGoals(subContentFirstHalf, 'First half')
        # parseGoals(subContentSecondHalf, 'Second half')
        # parseGoals(subContentExtraTime, 'Extra time')
        # parseGoals(subContentPenalties, 'Penalties')
        # parseMissedPenalties(subContentFirstHalf, 'First half')
        # parseMissedPenalties(subContentSecondHalf, 'Second half')
        # parseMissedPenalties(subContentExtraTime, 'Extra time')
        # parseMissedPenalties(subContentPenalties, 'Penalties')

def parseTeams(content):
    keyWordTeam = 'class="participant-imglink" onclick="window.open(&#39;/team/'
    keyWordTeamEnd = '/'
    startPosition = 0
    for i in range(4):
        startPosition = content.find(keyWordTeam, startPosition)
        if i == 1:
            endPosition = content.find(keyWordTeamEnd, startPosition + len(keyWordTeam))
            homeTeamTechCode = content[startPosition + len(keyWordTeam) : endPosition]
            homeTaemHashCode = content[endPosition+1:endPosition+9]
            homeTeam = content[endPosition+32:content.find('</a>', endPosition+24)]
            print('Home - ' + homeTeamTechCode + ', ' + homeTaemHashCode + ', ' + homeTeam)

        if i == 3:
            endPosition = content.find(keyWordTeamEnd, startPosition + len(keyWordTeam))
            awayTeamTechCode = content[startPosition + len(keyWordTeam) : endPosition]
            awayTeamHashCode = content[endPosition+1:endPosition+9]
            awayTeam = content[endPosition+32:content.find('</a>', endPosition+24)]
            print('Home - ' + awayTeamTechCode + ', ' + awayTeamHashCode + ', ' + awayTeam)

        startPosition = content.find(keyWordTeam, startPosition + len(keyWordTeam))

        i+=1

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
    # path = 'Statistics\ADE 4-3 BRI _ Adelaide United - Brisbane Roar _ Match Summary.html'
    # path = 'Statistics\HUN 1-2 SVK _ Hungary - Slovakia _ Match Summary.html'
    # path = 'Statistics\POL 1-2 POR _ Poland - Portugal _ Match Summary.html'
    path = 'Statistics\KOL 0-4 FC _ Kolos Kovalivka - Dyn. Kyiv _ Match Summary.html'
    # path = 'Statistics\FK 1-3 SHA _ Oleksandriya - Shakhtar Donetsk _ Match Summary.html'
    # path = 'Statistics\IRN 14-0 CAM _ Іран - Камбоджа _ Огляд матчу.html'
    file = open(path)
    content = file.read()

    parseTitle(content)
    parseDateTime(content)
    parseIncidents(content)
    parseScore(content)
    parseTeams(content)

    # print(globalDate)
    # print(globalTime)
    # print(globalCountry)
    # print(globalLeagua)
    # print(globalLeaguaRound)
    # print(globalLeaguaKindOfFinal)


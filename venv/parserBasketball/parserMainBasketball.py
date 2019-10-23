import time as t

globalCountry = ''
globalLeagua = ''
globalSeason = ''
globalAOTCount = 0
globalMatchCount = 0

def parseSeasonBasketball(content):
    if len(content) != 0:
        global globalCountry
        global globalLeagua
        global globalSeason
        keyWordSeason = '<div class="seoTop__content">'
        positionOfKeyWordSeason = content.find(keyWordSeason) + len(keyWordSeason) + 18
        positionOfKeyWordSeasonEnd = content.find(': ', positionOfKeyWordSeason)
        globalCountry = content[positionOfKeyWordSeason:positionOfKeyWordSeasonEnd]
        positionOfKeyWordLeaguaEnd = content.find(' ', positionOfKeyWordSeasonEnd + 2)
        globalLeagua = content[positionOfKeyWordSeasonEnd + 2 : positionOfKeyWordLeaguaEnd]
        globalSeason = content[positionOfKeyWordLeaguaEnd + 1:content.find('</h1>', positionOfKeyWordLeaguaEnd)-1]
        print(globalCountry)
        print(globalLeagua)
        print(globalSeason)

def parseTitleBasketball(content):
    keyWordTitle = '</span><span class="event__title--name" title="'
    countKeyWordTitle = content.count(keyWordTitle)
    # print(countKeyWordTitle)
    beginToSearch = 0

    positionOfCountry = content.find(keyWordTitle, beginToSearch)
    positionOfCountryEnd = content.find(keyWordTitle, positionOfCountry + len(keyWordTitle))
    i = 1
    while i <= countKeyWordTitle:
        positionOfCountryBegin = content.rfind('>', 0, positionOfCountry)
        country = content[positionOfCountryBegin + 1 : positionOfCountry]

        positionOfLeaguaBegin = content.find('>', positionOfCountry + len(keyWordTitle))
        positionOfLeaguaEnd = content.find('<', positionOfLeaguaBegin)
        leaguaContent = content[positionOfLeaguaBegin + 1 : positionOfLeaguaEnd]
        listOfLeaguas = leaguaContent.split(' - ')
        if len(listOfLeaguas) == 1:
            leagua = listOfLeaguas[0]
            leaguaPart = 'Regular'
        elif len(listOfLeaguas) == 2:
            leagua = listOfLeaguas[0]
            leaguaPart = listOfLeaguas[1]

        print(country + ' : ' + leagua + ' : ' + leaguaPart + '; start - ' + str(positionOfCountry) + ' - ' + str(positionOfCountryEnd))

        subContent = content[positionOfCountry:positionOfCountryEnd]
        # print(len(subContent))
        parsePreSubtitleBasketball(subContent)

        positionOfCountry = content.find(keyWordTitle, positionOfCountry + len(keyWordTitle))
        positionOfCountryEnd = content.find(keyWordTitle, positionOfCountry + len(keyWordTitle))
        i += 1 # move iterator

def parsePreSubtitleBasketball(content):

    subTitleKeyWord = '<div class="event__round event__round--static">'

    if content.count(subTitleKeyWord) == 0:
        parseSubTitleBasketballRounds(content)

    else:
        positionContentStart = content.find(subTitleKeyWord)
        positionContentEnd = content.find(subTitleKeyWord, positionContentStart + len(subTitleKeyWord))
        contentForIteration = content[positionContentStart : positionContentEnd]
        i = 1
        while i <= content.count(subTitleKeyWord):
            # print('Diapasone - ' + str(positionContentStart) + ' - ' + str(positionContentEnd))
            round = contentForIteration[len(subTitleKeyWord): contentForIteration.find('</div', len(subTitleKeyWord))]
            print(round)
            parseSubTitleBasketballRounds(contentForIteration) # work +- norm

            positionContentStart = content.find(subTitleKeyWord, positionContentStart + len(subTitleKeyWord))
            positionContentEnd = content.find(subTitleKeyWord, positionContentStart + len(subTitleKeyWord))
            contentForIteration = content[positionContentStart: positionContentEnd]
            i += 1

    # print('-----------------------------------------------')

def parseSubTitleBasketballRounds(content):
    global globalAOTCount
    global globalMatchCount

    eventKeyWord = '<div id="g_3_'
    eventKeyWordHomeTeam = '<div class="event__participant event__participant--home'
    eventKeyWordAwayTeam = '<div class="event__participant event__participant--away'

    eventKeyWordHomeScore_Total = '<div class="event__score event__score--home">'
    eventKeyWordAwayScore_Total = '<div class="event__score event__score--away">'

    eventKeyWordHomeScore_First_Quoter = '<div class="event__part event__part--home event__part--1">'
    eventKeyWordAwayScore_First_Quoter = '<div class="event__part event__part--away event__part--1">'

    eventKeyWordHomeScore_Second_Quoter = '<div class="event__part event__part--home event__part--2">'
    eventKeyWordAwayScore_Second_Quoter = '<div class="event__part event__part--away event__part--2">'

    eventKeyWordHomeScore_Third_Quoter = '<div class="event__part event__part--home event__part--3">'
    eventKeyWordAwayScore_Third_Quoter = '<div class="event__part event__part--away event__part--3">'

    eventKeyWordHomeScore_Fourth_Quoter = '<div class="event__part event__part--home event__part--4">'
    eventKeyWordAwayScore_Fourth_Quoter = '<div class="event__part event__part--away event__part--4">'

    keyWordAOT = '<div class="event__stage"><div class="event__stage--block">AOT</div></div></div>'
    eventKeyWordHomeScore_AOT = '<div class="event__part event__part--home event__part--5">'
    eventKeyWordAwayScore_AOT = '<div class="event__part event__part--away event__part--5">'

    eventKeyWordWinner = '<div class="event__icon icon--winner">'

    def scoreParser(keyWord, start):
        return content[content.find(keyWord, start) + len(keyWord) : content.find('</div', content.find(keyWord, start))]


    positionOfEventKeyWord = content.find(eventKeyWord)
    # print('count - ' + str(content.count(eventKeyWord)))
    i = 1
    while i <= content.count(eventKeyWord):
        globalMatchCount = globalMatchCount + 1
        timeOfMatch = content[content.find('<div class="event__time">', positionOfEventKeyWord) + len('<div class="event__time">') :
               content.find('<div class="event__time">', positionOfEventKeyWord) + len('<div class="event__time">') + 12]

        #check OT

        checkAOT = content[content.find('<div class="event__time">', positionOfEventKeyWord) + len('<div class="event__time">') + 12 :
                           content.find('<div class="event__time">', positionOfEventKeyWord) + len('<div class="event__time">') + 12 + 80]
        aot = 0
        if checkAOT == keyWordAOT:
            aot = 1

        codeEventString = content[positionOfEventKeyWord + len(eventKeyWord): positionOfEventKeyWord + len(eventKeyWord) + 8]

        homeTeamPass = ''
        awayTeamPass = ''


        # fontBold"Toronto Raptors<div class="event__icon icon - -winner">

        homeTeam = content[content.find(eventKeyWordHomeTeam, positionOfEventKeyWord) + len(eventKeyWordHomeTeam) :
                           content.find('</div>', content.find(eventKeyWordHomeTeam, positionOfEventKeyWord))]
        homeTeam = homeTeam.replace(' fontBold">', '')
        homeTeam = homeTeam.replace('">', '')

        #Begin recognise a team which pass a round
        homePass = content[content.find('</div>', content.find(eventKeyWordHomeTeam, positionOfEventKeyWord)) - 38 :
                           content.find('</div>', content.find(eventKeyWordHomeTeam, positionOfEventKeyWord))]
        awayPass = content[content.find('</div>', content.find(eventKeyWordAwayTeam, positionOfEventKeyWord)) - 38:
                           content.find('</div>', content.find(eventKeyWordAwayTeam, positionOfEventKeyWord))]

        if  homePass == '<div class="event__icon icon--winner">':
            homeTeamPass = 1
            awayTeamPass = 0

        if awayPass == '<div class="event__icon icon--winner">':
            homeTeamPass = 0
            awayTeamPass = 1

        #End recognise a team which pass a round

        homeTeam = homeTeam.replace('<div class="event__icon icon--winner', '')

        awayTeam = content[content.find(eventKeyWordAwayTeam, positionOfEventKeyWord) + len(eventKeyWordAwayTeam):
                           content.find('</div>', content.find(eventKeyWordAwayTeam, positionOfEventKeyWord))]
        awayTeam = awayTeam.replace(' fontBold">', '')
        awayTeam = awayTeam.replace('">', '')

        awayTeam = awayTeam.replace('<div class="event__icon icon--winner', '')


        print(timeOfMatch + ' ' + codeEventString)

        aotScoreHome = ''
        aotScoreAway = ''
        if aot == 1:
            aotScoreHome = ' AOT - ' + str(scoreParser(eventKeyWordHomeScore_AOT, positionOfEventKeyWord))
            aotScoreAway = ' AOT - ' + str(scoreParser(eventKeyWordAwayScore_AOT, positionOfEventKeyWord))
            globalAOTCount = globalAOTCount + 1

        print(str(homeTeam) + ' - ' + str(scoreParser(eventKeyWordHomeScore_Total, positionOfEventKeyWord) + ' - ' +
                                          str(scoreParser(eventKeyWordHomeScore_First_Quoter, positionOfEventKeyWord)) + ' - ' +
                                          str(scoreParser(eventKeyWordHomeScore_Second_Quoter, positionOfEventKeyWord)) + ' - ' +
                                          str(scoreParser(eventKeyWordHomeScore_Third_Quoter, positionOfEventKeyWord)) + ' - ' +
                                          str(scoreParser(eventKeyWordHomeScore_Fourth_Quoter, positionOfEventKeyWord)) +
                                          aotScoreHome + ' ' + str(homeTeamPass)
                                          ))

        print(str(awayTeam) + ' - ' + str(scoreParser(eventKeyWordAwayScore_Total, positionOfEventKeyWord) + ' - ' +
                                          str(scoreParser(eventKeyWordAwayScore_First_Quoter, positionOfEventKeyWord)) + ' - ' +
                                          str(scoreParser(eventKeyWordAwayScore_Second_Quoter, positionOfEventKeyWord)) + ' - ' +
                                          str(scoreParser(eventKeyWordAwayScore_Third_Quoter, positionOfEventKeyWord)) + ' - ' +
                                          str(scoreParser(eventKeyWordAwayScore_Fourth_Quoter, positionOfEventKeyWord)) +
                                          aotScoreAway + ' ' + str(awayTeamPass)
                                          ))

        positionOfEventKeyWord = content.find(eventKeyWord, positionOfEventKeyWord + len(eventKeyWord))
        i += 1


if __name__=='__main__':
    path = r'Archive/NBA 2018_2019 Results - Basketball_USA.html'
    # firstCriteria = '<div class="event__round event__round--static">'
    file = open(path)
    contentGlobal = file.read()
    parseSeasonBasketball(contentGlobal)
    parseTitleBasketball(contentGlobal)

    print(globalAOTCount)
    print(globalMatchCount)
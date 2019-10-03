# import os
# try to parse from file
#Get file from flashscore.com


def parseRound(incomeStringRound):
#define the round
    criteriaFirstRound = '<div class="event__round event__round--static">'
    criteriaSecondRound = '</div>'
    beginOftheStringRound = incomeStringRound.find(criteriaFirstRound)
    endOftheStringRound = incomeStringRound.find(criteriaSecondRound)
    round = incomeStringRound[beginOftheStringRound + len(criteriaFirstRound):endOftheStringRound]
    return round

def parseCodeEventString(incomeCodeEventString):
    # define the code event string
    criteriaFirstCodeEventString = 'g_1_'
    criteriaSecondCodeEventString = 'Click for match detail!'
    countIncomeEventString = incomeCodeEventString.count(criteriaFirstCodeEventString)
    j = 0
    i = 1
    while i <=countIncomeEventString:
        beginOfTheCodeEventString = incomeCodeEventString.find(criteriaFirstCodeEventString, j)
        j = beginOfTheCodeEventString + 1
        endOfTheCodeEventString = incomeCodeEventString.find(criteriaSecondCodeEventString, j)
        outcomeCodeEventString = incomeCodeEventString[beginOfTheCodeEventString+len(criteriaFirstCodeEventString):]
        codeEventString = incomeCodeEventString[beginOfTheCodeEventString + len(criteriaFirstCodeEventString): endOfTheCodeEventString-9]
        t = str(parseTimeEventString(outcomeCodeEventString))
        h = str(parseEventHomeTeamString(outcomeCodeEventString))
        hos = str(parseEventHomeScoreString(outcomeCodeEventString))
        aws = str(parseEventAwayScoreString(outcomeCodeEventString))
        aw = str(parseEventAwayTeamString(outcomeCodeEventString))

        print(codeEventString + ' ' + t + ' ' + h + ' ' + hos + ' - ' + aws + ' ' + aw)
        i+=1

def parseTimeEventString(incomeTimeEventString):
    # define the time
    criteriaFirstTime = 'event__time'
    beginOfTheTimeEventString = incomeTimeEventString.find(criteriaFirstTime)
    timeEventString = incomeTimeEventString[beginOfTheTimeEventString + 13:beginOfTheTimeEventString+25]
    return timeEventString

def parseEventHomeTeamString(incomeEventHomeTeamString):
    # define home team
    criteriaFirstEventHomeTeamString = 'event__participant event__participant--home'
    criteriaSecondEventHomeTeamString = '</div>'
    incomeEventHomeTeamString = incomeEventHomeTeamString.replace('<div class ="icon icon--redCard redCard--first">', '')
    incomeEventHomeTeamString = incomeEventHomeTeamString.replace('<div class="icon icon--redCard redCard--first redCard--last">', '')
    beginOfTheEventHomeTeamString = incomeEventHomeTeamString.find(criteriaFirstEventHomeTeamString)
    endOfTheEventHomeTeamString = incomeEventHomeTeamString.find(criteriaSecondEventHomeTeamString, beginOfTheEventHomeTeamString)
    eventHomeTeamStringPre = incomeEventHomeTeamString[beginOfTheEventHomeTeamString + 45:endOfTheEventHomeTeamString]
    eventHomeTeamString = eventHomeTeamStringPre.replace('ontBold">', '')
    return eventHomeTeamString


def parseEventAwayTeamString(incomeEventAwayTeamString):
    # define away team
    criteriaFirstEventAwayTeamString = 'event__participant event__participant--away'
    criteriaSecondEventAwayTeamString = '</div>'
    incomeEventAwayTeamString = incomeEventAwayTeamString.replace('<div class ="icon icon--redCard redCard--first">', '')
    incomeEventAwayTeamString = incomeEventAwayTeamString.replace('<div class="icon icon--redCard redCard--first redCard--last">', '')
    beginOfTheEventAwayTeamString = incomeEventAwayTeamString.find(criteriaFirstEventAwayTeamString)
    endOfTheEventAwayTeamString = incomeEventAwayTeamString.find(criteriaSecondEventAwayTeamString, beginOfTheEventAwayTeamString)
    eventAwayTeamStringPre = incomeEventAwayTeamString[beginOfTheEventAwayTeamString + 45:endOfTheEventAwayTeamString]
    eventAwayTeamString = eventAwayTeamStringPre.replace('ontBold">', '')
    # print(eventAwayTeamString)
    return eventAwayTeamString

def parseEventHomeScoreString(incomeEventHomeScoreString):
    #define
    criteriaFirstEventHomeScoreString = '<span>'
    criteriaSecondEventHomeScoreString = '</span>'
    beginOfTheEventHomeScoreString = incomeEventHomeScoreString.find(criteriaFirstEventHomeScoreString)
    endOfTheEventHomeTeamString = incomeEventHomeScoreString.find(criteriaSecondEventHomeScoreString, beginOfTheEventHomeScoreString)
    eventHomeScoreString = incomeEventHomeScoreString[beginOfTheEventHomeScoreString+len(criteriaFirstEventHomeScoreString):endOfTheEventHomeTeamString]
    return eventHomeScoreString

def parseEventAwayScoreString(incomeEventAwayScoreString):
    criteriaFirstEventAwayScoreString = 'nbsp;<span>'
    criteriaSecondEventAwayScoreString = '</span>'
    beginOfTheEventAwayScoreString = incomeEventAwayScoreString.find(criteriaFirstEventAwayScoreString)
    endOfTheEventAwayTeamString = incomeEventAwayScoreString.find(criteriaSecondEventAwayScoreString, beginOfTheEventAwayScoreString)
    eventAwayScoreString = incomeEventAwayScoreString[beginOfTheEventAwayScoreString + len(criteriaFirstEventAwayScoreString):endOfTheEventAwayTeamString]
    # print(eventAwayScoreString)
    return eventAwayScoreString

if __name__=='__main__':
    path = 'Archive\England\season_2018_2019\Premier League 2018_2019 Results - Football_England.html'
    firstCriteria = '<div class="event__round event__round--static">'
    file = open(path)
    content = file.read()
    countFirstCriteria = content.count(firstCriteria)

    print(countFirstCriteria)

    i = 1
    j = 0


    while i <= countFirstCriteria:
        beginOftheString = content.find(firstCriteria, j)
        j = beginOftheString + 1
        endOfTheString = content.find(firstCriteria, j)
        outcomeString = content[beginOftheString:endOfTheString]
        print(parseRound(outcomeString))
        parseCodeEventString(outcomeString)
        i += 1
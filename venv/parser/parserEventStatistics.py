def parseStatistics(content, coreString):
    print(coreString)
    countOfCoreString = content.count(coreString)
    startPosition = content.find(coreString, len(coreString))
    for i in range(countOfCoreString):
        period = ''
        if i == 0:
            period = "Match - "
        elif i == 1:
            period = 'First half - '
        elif i == 2:
            period = 'Second half - '
        elif i == 3:
            period = 'Extra time - '

        stringToParse = content[startPosition-94:startPosition+63+len(coreString)]
        beginIndexHomeValue = stringToParse.find('homeValue">')
        endIndexHomeValue = stringToParse.find('</div>',beginIndexHomeValue)
        homeValue = stringToParse[beginIndexHomeValue+len('homeValue">'):endIndexHomeValue]
        print(period + homeValue.replace('%', ''))
        beginIndexAwayValue = stringToParse.find('awayValue">')
        endIndexAwayValue = stringToParse.find('</div>',beginIndexAwayValue)
        awayValue = stringToParse[beginIndexAwayValue+len('awayValue">'):endIndexAwayValue]
        print(period + awayValue.replace('%', ''))
        startPosition = content.find(coreString, startPosition + len(coreString))
        print('----')
    print('---------------------')

if __name__=='__main__':
    # path = 'Statistics\ADE 4-3 BRI _ Adelaide United - Brisbane Roar _ Statistics.html'
    # path = 'Statistics\POL 1-2 POR _ Poland - Portugal _ Statistics.html'
    # path = 'Statistics\ENG 0-1 ITA _ England - Italy _ Statistics.html'
    path = 'Statistics\AIG 2-1 RUK _ Aigle Noir - Rukinzo _ Statistics.html'
    file = open(path)
    content = file.read()
    criteriaBallPossession = '>Ball Possession<'
    criteriaGoalAttempst = '>Goal Attempts<'
    criteriaShotsOnGoal = '>Shots on Goal<'
    criteriaShotsOffGoal = '>Shots off Goal<'
    criteriaBlockedShots = '>Blocked Shots<'
    criteriaFreeKicks = '>Free Kicks<'
    criteriaOffsides = '>Offsides<'
    criteriaThrowIn = '>Throw-in<'
    criteriaGoalkeeperSaves = '>Goalkeeper Saves<'
    criteriaFouls = '>Fouls<'
    criteriaTotalPasses = '>Total Passes<'
    criteriaCompletedPasses = '>Completed Passes<'
    criteriaCornerKicks = '>Corner Kicks<'
    criteriaRedCards = '>Red Cards<'
    criteriaYellowCards = '>Yellow Cards<'
    criteriaTackles = '>Tackles<'
    criteriaAttacks = '>Attacks<'
    criteriaDangerousAttacks = '>Dangerous Attacks<'


    parseStatistics(content, criteriaBallPossession)
    parseStatistics(content, criteriaGoalAttempst)
    parseStatistics(content, criteriaShotsOnGoal)
    parseStatistics(content, criteriaShotsOffGoal)
    parseStatistics(content, criteriaBlockedShots)
    parseStatistics(content, criteriaFreeKicks)
    parseStatistics(content, criteriaOffsides)
    parseStatistics(content, criteriaThrowIn)
    parseStatistics(content, criteriaGoalkeeperSaves)
    parseStatistics(content, criteriaFouls)
    parseStatistics(content, criteriaTotalPasses)
    parseStatistics(content, criteriaCompletedPasses)
    parseStatistics(content, criteriaCornerKicks)
    parseStatistics(content, criteriaRedCards)
    parseStatistics(content, criteriaYellowCards)
    parseStatistics(content, criteriaTackles)
    parseStatistics(content, criteriaAttacks)
    parseStatistics(content, criteriaDangerousAttacks)
    # print(content)

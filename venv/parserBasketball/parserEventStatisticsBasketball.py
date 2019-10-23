def parseStatistics(content, coreString):
    print(coreString)
    countOfCoreString = content.count(coreString)
    startPosition = content.find(coreString, len(coreString))
    for i in range(countOfCoreString):
        period = ''
        if i == 0:
            period = "Match - "
        elif i == 1:
            period = '1st Quarter - '
        elif i == 2:
            period = '2nd Quarter - '
        elif i == 3:
            period = '3rd Quarter - '
        elif i == 4:
            period = '4rd Quarter - '
        elif i == 5:
            period = 'Owertime - '

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
    # path = 'Archive\GSW 110-114 TOR _ Golden State Warriors - Toronto Raptors _ Statistics.html'
    path = 'Archive\TOR 118-112 MIL _ Toronto Raptors - Milwaukee Bucks _ Statistics.html'
    file = open(path)
    content = file.read()
    criteria_Field_Goals_Attempted = '>Field Goals Attempted<'
    criteria_Field_Goals_Made = '>Field Goals Made<'
    criteria_Field_Goals_percent = '>Field Goals %<'
    criteria_2_Point_Field_Goal_Attempted = '>2-Point Field G. Attempted<'
    criteria_2_Point_Field_Goals_Made = '>2-Point Field Goals Made<'
    criteria_2_Point_Field_Goals_percent = '>2-Point Field Goals %<'
    criteria_3_Point_Field_Goal_Attempted = '>3-Point Field G. Attempted<'
    criteria_3_Point_Field_Goals_Made = '>3-Point Field Goals Made<'
    criteria_3_Point_Field_Goals_percent = '>3-Point Field Goals %<'
    criteria_Free_Throws_Attempted = '>Free Throws Attempted<'
    criteria_Free_Throws_Made = '>Free Throws Made<'
    criteria_Free_Throws_percent = '>Free Throws %<'

    criteria_Offensive_Rebounds = '>Offensive Rebounds<'
    criteria_Defensive_Rebounds  = '>Defensive Rebounds<'
    criteria_Total_Rebounds = '>Total Rebounds<'

    criteria_Assists = '>Assists<'
    criteria_Blocks = '>Blocks<'
    criteria_Turnovers = '>Turnovers<'
    criteria_Steals = '>Steals<'
    criteria_Personal_Fouls = '>Personal Fouls<'
    criteria_Technical_Fouls = '>Technical Fouls<'

    parseStatistics(content, criteria_Field_Goals_Attempted)
    parseStatistics(content, criteria_Field_Goals_Made)
    parseStatistics(content, criteria_Field_Goals_percent)
    parseStatistics(content, criteria_2_Point_Field_Goal_Attempted)
    parseStatistics(content, criteria_2_Point_Field_Goals_Made)
    parseStatistics(content, criteria_2_Point_Field_Goals_percent)
    parseStatistics(content, criteria_3_Point_Field_Goal_Attempted)
    parseStatistics(content, criteria_3_Point_Field_Goals_Made)
    parseStatistics(content, criteria_3_Point_Field_Goals_percent)
    parseStatistics(content, criteria_Free_Throws_Attempted)
    parseStatistics(content, criteria_Free_Throws_Made)
    parseStatistics(content, criteria_Free_Throws_percent)
    parseStatistics(content, criteria_Offensive_Rebounds)
    parseStatistics(content, criteria_Defensive_Rebounds)
    parseStatistics(content, criteria_Total_Rebounds)
    parseStatistics(content, criteria_Assists)
    parseStatistics(content, criteria_Blocks)
    parseStatistics(content, criteria_Turnovers)
    parseStatistics(content, criteria_Steals)
    parseStatistics(content, criteria_Personal_Fouls)
    parseStatistics(content, criteria_Technical_Fouls)

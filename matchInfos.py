import requests, pandas as pd, os,time
os.chdir('C:\\Users\\jackl')
key = {'X-Riot-Token' : 'RGAPI-ab86aa81-8b70-45bd-88b7-4b9889ab6f7d'} #update daily
tiers = ['BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'EMERALD', 'DIAMOND']
divisions = ['I', 'II', 'III', 'IV']


def oneMatchData (matchid):
    matchinfo = f'https://americas.api.riotgames.com/lol/match/v5/matches/{matchid}'

    res = requests.get(matchinfo, headers = key)
    info = res.json()
    data = info['info']['participants']

    df = pd.DataFrame(data)
    df['gameID'] = matchid
    wantedColumns = df[['gameID', 
    'champLevel',
    'championName',
    'damageDealtToObjectives',
    'goldEarned',
    'individualPosition',
    'lane',
    'teamPosition',
    'puuid',
    'wardsKilled',
    'wardsPlaced',
    'win']]
    wantedChallenges = [
    'puuid',
    'alliedJungleMonsterKills',
    'baronTakedowns',
    'controlWardsPlaced',
    'dragonTakedowns',
    'earliestDragonTakedown',
    'enemyJungleMonsterKills',
    'gameLength',
    'goldPerMinute',
    'jungleCsBefore10Minutes',
    'kda',
    'killParticipation',
    'killsOnOtherLanesEarlyJungleAsLaner',
    'moreEnemyJungleThanOpponent',
    'pickKillWithAlly',
    'stealthWardsPlaced',
    'teamDamagePercentage',
    'visionScoreAdvantageLaneOpponent',
    'visionScorePerMinute'
    ]
    challengesTemp = []
    for playernum in range (len(data)):
        dfchallenges = data[playernum]['challenges']
        dfchallenges['puuid'] = data[playernum]['puuid']
        challengesTemp.append (dfchallenges)

    challenges = pd.DataFrame(challengesTemp)
    challenges = challenges[wantedChallenges].drop_duplicates()

    result = pd.merge(wantedColumns,challenges, on='puuid', how='left')
    return result

matches = open('Desktop\\matches.txt', 'r')
matches = matches.read().replace("'", "").split(", ")

finalDf = pd.DataFrame()
for match in matches:
    try:
        finalDf = pd.concat([finalDf, oneMatchData(match)], ignore_index=True)
        print(finalDf)
    except:
        print('sleeping')
        time.sleep(5)
    print (match)

finalDf.to_excel('Desktop\\ProjectFile.xlsx')

#print(oneMatchData('NA1_4897671573'))
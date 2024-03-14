import requests, pandas as pd, os, time
os.chdir('C:\\Users\\jackl')
api_key = 'RGAPI-980674a5-7171-4087-821d-0c3e7a2f57f8' #update daily
tiers = ['BRONZE', 'SILVER', 'GOLD', 'PLATINUM', 'EMERALD', 'DIAMOND']
divisions = ['I', 'II', 'III', 'IV']

def getSummonerID (rank):
    rank = rank.upper()
    list = []
    for division in divisions: #table of 2 pages of guys in this rank
        for i in range(1,3):
            res = requests.get(f'https://na1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/{rank}/{division}?page={str(i)}&api_key={api_key}')

            for player in res.json():
                list.append(player['summonerId'])
    return list

def get_match_ids_by_rank(summonerId):
    # Get summoner ID by summoner name
    summoner_url = f'https://na1.api.riotgames.com/lol/summoner/v4/summoners/{summonerId}?api_key={api_key}'
    summoner_response = requests.get(summoner_url)
    summoner_data = summoner_response.json()
    summoner_id = summoner_data['puuid']
    
    # Get match IDs by summoner ID and rank
    match_url = f'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{summoner_id}/ids?type=ranked&start=0&count=5&api_key={api_key}'
    match_response = requests.get(match_url)
    match_ids = match_response.json()
    return match_ids


for id in getSummonerID('gold'):
    print(get_match_ids_by_rank(id))



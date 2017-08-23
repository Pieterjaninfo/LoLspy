import json

champions = dict()
champions_by_id = dict()


def getChampion(championId):
    return champions_by_id[championId]

# fill static data upon import
with open('champions.txt', 'r') as file:
    data = file.read().replace('\n', '')
    champions = json.loads(data)

for champion_name in champions['data']:
    champ_info = champions['data'][champion_name]
    champions_by_id[champ_info['id']] = champion_name





if __name__ == '__main__':
    print(champions_by_id)
    print(getChampion(61))
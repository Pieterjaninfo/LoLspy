import json
from utils import *


def getChampion(championId):
    """ Returns the champion name corresponding to the given champion id. """
    return champions_by_id[championId]

def getMasterie(masterieId):
    return masteries['data'][masterieId]

def getRune(runeId):
    return runes['data'][runeId]


#####################################
#                                   #
#   fill static data upon import    #
#                                   #
#####################################

champions = json.loads(open_file('champions.txt'))
masteries = json.loads(open_file('masteries.txt'))
runes = json.loads(open_file('runes.txt'))

champions_by_id = dict()
for champion_name in champions['data']:
    champ_info = champions['data'][champion_name]
    champions_by_id[champ_info['id']] = champion_name






if __name__ == '__main__':

    # print(champions_by_id)
    # print(getChampion(61))

    print(masteries)
    print(runes)
    print(getRune('5009'))
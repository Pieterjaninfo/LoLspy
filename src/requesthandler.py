from requester import *
from time import time
# {'accountId': 23955146, 'profileIconId': 2097, 'summonerLevel': 30, 'revisionDate': 1503435617000, 'id': 20694012, 'name': 'Lukeydude'}
# 20694012

current_time = time() * 1000


def analyze_user(summoner_name):
    user = getSummonerByName(summoner_name)
    user_id = user['id']
    user_level = user['summonerLevel']
    user_accountId = user['accountId']
    # print('id: %d, lvl: %d, accountId: %d' % (user_id, user_level, user_accountId))

    elo = get_elo(user_id)
    champ_mastery = getAllMastery(user_id)

    process_elo(elo)
    process_champion_mastery(champ_mastery)


def process_champion_mastery(champion_masteries):
    for champion_mastery in champion_masteries:
        champion_id = champion_mastery['championId']
        mastery_level = champion_mastery['championLevel']
        mastery_points = champion_mastery['championPoints']
        time_last_played = champion_mastery['lastPlayTime']

        champ_info = '%s - lvl %d (%.2fk points) - last played %.0f days ago' % \
                     (getChampion(champion_id), mastery_level, mastery_points/1000,
                      days_ago(time_last_played))
        print(champ_info)

# {'championPointsUntilNextLevel': 0, 'chestGranted': True,
# 'championPointsSinceLastLevel': 120226,
# 'lastPlayTime': 1502721448000, 'playerId': 20694012, 'championLevel': 6, 'championId': 61,
# 'championPoints': 141826, 'tokensEarned': 3}
def process_elo(elos):
    for elo in elos:
        tier = elo['tier']
        rank = elo['rank']
        wins = elo['wins']
        losses = elo['losses']
        queuetype = elo['queueType']

        elo_info = '%s %s %s %d:%d (w:l)' % (queuetype, tier, rank, wins, losses)
        print(elo_info)
    pass


if __name__ == '__main__':
    analyze_user('peeri')


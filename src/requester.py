import requests
from secret import KEY
from staticdata import *

##############################################
#                                            #
#                  REQUESTS                  #
#                                            #
##############################################

REGIONS = ['ru', 'kr', 'br1', 'oc1', 'jp1', 'na1', 'eun1', 'euw1', 'tr1', 'la1', 'la2']
region = 'euw1'
key_url = '?api_key=' + KEY

def sendRequest(post_url):
    """ Builds an http GET request and returns the response. """
    return requests.get(''.join(['https://', region, '.api.riotgames.com', post_url, key_url]))

# Champion Mastery

def getAllMastery(summonerId):
    """ Get all champion mastery entries sorted by number of champion points descending. """
    url = '/lol/champion-mastery/v3/champion-masteries/by-summoner/'
    return sendRequest(''.join([url, str(summonerId)])).json()


def getMastery(summonerId, championId):
    """ Get a champion mastery by player ID and champion ID. """
    url_1 = '/lol/champion-mastery/v3/champion-masteries/by-summoner/'
    url_2 = '/by-champion/'
    return sendRequest(''.join([url_1, str(summonerId), url_2, str(championId)])).json()


def getTotalMasteryScore(summonerId):
    """ Get a player's total champion mastery score, which is the sum of individual champion mastery levels. """
    url = '/lol/champion-mastery/v3/scores/by-summoner/'
    return sendRequest(''.join([url, str(summonerId)])).json()


# # Champion
#
# def getAllChampions():
#     """ Retrieve all champions. """
#     url = '/lol/platform/v3/champions'
#     return sendRequest(url)
#
#
# def getChampion(championId):
#     """ Retrieve champion by ID. """
#     url = '/lol/platform/v3/champions/'
#     return sendRequest(''.join([url, str(championId)]))

# Lol Static Data
'''
def getAllChampions():
    """ Retrieves champion list. """
    url = '/lol/static-data/v3/champions'
    return sendRequest(url).json()

def getChampion(championId):
    """ Retrieves champion by ID. """
    url = '/lol/static-data/v3/champions/'
    return sendRequest(''.join([url, str(championId)])).json()

def getAllItems():
    """ Retrieves item list. """
    url = '/lol/static-data/v3/items'
    return sendRequest(url).json()

def getItem(itemId):
    """ Retrieves item by ID. """
    url = '/lol/static-data/v3/items/'
    return sendRequest(''.join([url, str(itemId)])).json()

def getMasteriesItem(masteryId):
    """ Retrieves mastery item by ID. """
    url = '/lol/static-data/v3/masteries/'
    return sendRequest(''.join([url, str(masteryId)])).json()

def getRuneItem(runeId):
    """ Retrieves rune by ID. """
    url = '/lol/static-data/v3/runes/'
    return sendRequest(''.join([url, str(runeId)])).json()

def getSummonerSpellItem(summonerSpellId):
    """ Retrieves summoner spell by ID. """
    url = '/lol/static-data/v3/summoner-spells/{id}'
    return sendRequest(''.join([url, str(summonerSpellId)])).json()
'''


# Masteries
def getUserMasteries(summonerId):
    """ Get mastery pages for a given summoner ID. """
    url = '/lol/platform/v3/masteries/by-summoner/'
    return sendRequest(''.join([url, summonerId])).json()


# Runes
def getUserRunes(summonerId):
    """ Get rune pages for a given summoner ID. """
    url = '/lol/platform/v3/runes/by-summoner/'
    return sendRequest(''.join([url, str(summonerId)])).json()


# Spectator
def getCurrentGame(summonerId):
    """ Get current game information for the given summoner ID. """
    url = '/lol/spectator/v3/active-games/by-summoner/'
    return sendRequest(''.join([url, str(summonerId)])).json()


def getFeaturedGame():
    """ Get list of featured games. """
    url = '/lol/spectator/v3/featured-games'
    return sendRequest(url).json()


# Summoner
def getSummonerByName(summonerName):
    """ Get a summoner by summoner name. """
    url = '/lol/summoner/v3/summoners/by-name/'
    return sendRequest(''.join([url, summonerName])).json()

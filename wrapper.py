import requests
import json
from alerts import Alert
from invasions import Invasion
import configparser

class Wrapper:

    def __init__(self, platform):
        self.data = self.fetch(platform)
        self.alerts = []
        self.invasions = []


    @staticmethod
    def fetch(platform="PC"):
        if platform == "PC":
            url = "http://content.warframe.com/dynamic/worldState.php"
        elif platform == "PS4":
            url = "http://content.ps4.warframe.com/dynamic/worldState.php"
        elif platform == "XB1":
            url = "http://content.xb1.warframe.com/dynamic/worldState.php"
        else:
            raise Exception("incorrect platform")

        r = requests.get(url)
        data = json.loads(r.content)
        return data

    @staticmethod
    def getItemName(link):
        parser = configparser.ConfigParser()
        parser.read("itemlist.ini")
        try:
            name = parser.get("Items", link)
        except configparser.NoOptionError:
            return link
        return name

    def listAlerts(self):
        alertlist = self.data["Alerts"]
        return alertlist

    def listInvasions(self):
        invasionlist = self.data["Invasions"]
        return invasionlist

    def getAlerts(self):
        for alertNum in range(len(self.listAlerts())):
            self.alerts.append(Alert(alertNum, c.data["Alerts"][1]["_id"]["$oid"],
                      c.data["Alerts"][alertNum]["Activation"]["$date"]["$numberLong"],
                      c.data["Alerts"][alertNum]["Expiry"]["$date"]["$numberLong"],
                      **c.data["Alerts"][alertNum]["MissionInfo"]))

    def getInvasions(self):
        for invasionNum in range(len(self.listInvasions())):
            self.invasions.append(Invasion(invasionNum, **c.data["Invasions"][invasionNum]))


if __name__ == "__main__":
    c = Wrapper("PC")
    c.getAlerts()
    c.getInvasions()
    for x in range(len(c.alerts)):
        print(c.alerts[x].getAlertLoot())
    print("\n")

    for y in range(len(c.invasions)):
        print(c.invasions[y].getInvasionLoot("atk"))
        print(c.invasions[y].getInvasionLoot("def"))

    print(c.alerts[1].getAlertLocation())
    print(c.alerts[1].getAlertLoot())
    #print(c.alerts[1].getRemainingDuration())

    a = int(c.alerts[1].activation)
    e = int(c.alerts[1].expiry)
    now = int(c.data["Time"])
    print((e-now)/1000)
    #print(Alert.getItemName("/Lotus/Types/Items/MiscItems/Alertium"))

# event : dict_keys(['_id', 'Messages', 'Prop', 'Date', 'Priority', 'MobileOnly'])
#for x in range(len(c.data["Events"])):
#    print(c.data["Events"][x]["Messages"])

# dict_keys(['WorldSeed', 'Version', 'MobileVersion',
#  'BuildLabel', 'Time', 'Date', 'Events', 'Goals',
#  'Alerts', 'Sorties', 'SyndicateMissions', 'ActiveMissions',
#  'GlobalUpgrades', 'FlashSales', 'Invasions', 'HubEvents',
#  'NodeOverrides', 'BadlandNodes', 'VoidTraders',
#  'PrimeAccessAvailability', 'PrimeVaultAvailabilities',
#  'DailyDeals', 'LibraryInfo', 'PVPChallengeInstances',
# 'PersistentEnemies', 'PVPAlternativeModes', 'PVPActiveTournaments',
# 'ProjectPct', 'ConstructionProjects', 'TwitchPromos', 'WeeklyChallenges', 'FeaturedGuilds'])


# dict_keys(['_id', 'Activation', 'Expiry', 'HealthPct',
#  'VictimNode', 'Regions', 'Success', 'Desc', 'ToolTip',
#  'Icon', 'Tag', 'JobAffiliationTag', 'Jobs'])

'''
{'_id': {'$oid': '5c5aa46ac99e10bef4fbff91'}, 'Activation': {'$date': {'$numberLong': '1549565026219'}}, 
'Expiry': {'$date': {'$numberLong': '1551379426219'}}, 'HealthPct': 0.1416776, 'VictimNode': 'SolNode228', 
'Regions': [2], 'Success': 0, 'Desc': '/Lotus/Language/GameModes/RecurringGhoulAlert', 'ToolTip': '/Lotus/Language/GameModes/RecurringGhoulAlertDesc', 
'Icon': '/Lotus/Interface/Icons/Categories/IconGhouls256.png', 
'Tag': 'GhoulEmergence', 'JobAffiliationTag': 'CetusSyndicate', 'Jobs': [{'jobType': '/Lotus/Types/Gameplay/Eidolon/Jobs/Events/GhoulAlertBountyAss',
 'rewards': '/Lotus/Types/Game/MissionDecks/EidolonJobMissionRewards/GhoulBountyTableARewards',
  'masteryReq': 0, 'minEnemyLevel': 15, 'maxEnemyLevel': 25, 'xpAmounts': [250, 250, 250, 370]}, 
  {'jobType': '/Lotus/Types/Gameplay/Eidolon/Jobs/Events/GhoulAlertBountyHunt',
   'rewards': '/Lotus/Types/Game/MissionDecks/EidolonJobMissionRewards/GhoulBountyTableBRewards', 
   'masteryReq': 0, 'minEnemyLevel': 40, 'maxEnemyLevel': 50, 'xpAmounts': [540, 540, 540, 790]}]}

'''
import requests
import json




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
        for invastionNum in range(len(self.listInvasions())):
            self.invasions.append(Invasion(invastionNum, **c.data["Invasions"][invastionNum]))


class Alert:

    def __init__(self, num, alertId=None, activation=None, expiry=None, missionType=None, maxWaveNum=None, faction=None,
                 location=None, levelOverride=None, enemySpec=None, extraEnemySpec=None, vipAgent=None,
                 customAdvancedSpawners=None, minEnemyLevel=None, maxEnemyLevel=None, difficulty=None, seed=None,
                 archwingRequired=None, isSharkwingMission=None, missionReward=None):

        self.num = num
        self.alertId = alertId
        self.activation = activation
        self.expiry = expiry
        self.missionType = missionType
        self.maxWaveNum = maxWaveNum
        self.faction = faction
        self.location = location
        self.levelOverride = levelOverride
        self.enemySpec = enemySpec
        self.extraEnemySpec = extraEnemySpec
        self.vipAgent = vipAgent
        self.customAdvancedSpawners = customAdvancedSpawners
        self.minEnemyLevel = minEnemyLevel
        self.maxEnenyLevel = maxEnemyLevel
        self.difficulty = difficulty
        self.seed = seed
        self.archwingRequired = archwingRequired
        self.isSharkwingMission = isSharkwingMission
        self.missionReward = missionReward

    '''
    def getAlertTime(self, alertid):

        alert = self.listAlerts()[alertid]
        tact = int(alert["Activation"]["$date"]["$numberLong"])
        texp = int(alert["Expiry"]["$date"]["$numberLong"])

        now = int(self.data["Time"])
        # warframe zeit ist in ms
        time_left = texp-tact

        #print(texp-tact) # total duration
        #print(texp-now) # time left ??? but no
    '''

    def getAlertLoot(self):
        cred, itemcount = 0, 0
        item = None
        loot = self.missionReward

        try:
            cred = loot["credits"]
        except KeyError:
            pass
        try:
            item = loot["countedItems"][0]["ItemType"]
            itemcount = loot["countedItems"][0]["ItemCount"]
        except KeyError:
            try:
                item = loot["items"][0]
                itemcount = 1
            except KeyError:
                pass

        if item == "/Lotus/Types/Items/MiscItems/Alertium":
            item = "Nitan Extract"
        elif item == "/Lotus/StoreItems/Upgrades/Mods/FusionBundles/AlertFusionBundleLarge":
            item = "150 Endo"
        elif item == "/Lotus/StoreItems/Upgrades/Mods/FusionBundles/AlertFusionBundleMedium":
            item = "100 Endo"
        elif item == "/Lotus/StoreItems/Types/Recipes/Weapons/PangolinSwordBlueprint":
            item = "Pangolin Sword Blueprint"
        elif item == "/Lotus/StoreItems/Types/Recipes/Helmets/NekrosShroudHelmetBlueprint":
            item = "Nekros Shroud Helmet Blueprint"
        elif item == "/Lotus/Types/Items/MiscItems/Tellurium":
            item = "Tellurium"
        elif item == "/Lotus/Types/Items/MiscItems/VoidTearDrop":
            item = "Void Traces"
        elif item == "/Lotus/Types/Items/MiscItems/Neurode":
            item = "Neurode"
        else:
            pass

        return {"credits": cred, "item": item, "amount": itemcount}


class Invasion:

    def __init__(self, num, _id=None, Faction=None, Node=None, Count=None, Goal=None, LocTag=None,
                 Completed=None, AttackerReward=None, AttackerMissionInfo=None, DefenderReward=None,
                 DefenderMissionInfo=None, Activation=None):

        self.num = num
        self.InvasionId = _id["$oid"]
        self.Faction = Faction
        self.Node = Node
        self.Count = Count
        self.Goal = Goal
        self.LocTag = LocTag
        self.Completed = Completed
        self.AttackerReward = AttackerReward
        self.AttackerMissionInfo = AttackerMissionInfo
        self.DefenderReward = DefenderReward
        self.DefenderMissionInfo = DefenderMissionInfo
        self.Activation = Activation["$date"]["$numberLong"]



c = Wrapper("PC")
c.getAlerts()
c.getInvasions()
print(c.invasions[0].Activation)
for x in range(len(c.alerts)):
    print(c.alerts[x].getAlertLoot())

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
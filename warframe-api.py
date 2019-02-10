import requests
import json




class Wrapper:

    def __init__(self, platform):
        self.data = self.fetch(platform)
        self.alerts = []


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

    def getAlerts(self):
        for alertNum in range(len(self.listAlerts())):
            self.alerts.append(Alert(alertNum, c.data["Alerts"][1]["_id"]["$oid"],
                      c.data["Alerts"][alertNum]["Activation"]["$date"]["$numberLong"],
                      c.data["Alerts"][alertNum]["Expiry"]["$date"]["$numberLong"],
                      **c.data["Alerts"][alertNum]["MissionInfo"]))


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

        loot = self.missionReward
        cred = loot["credits"]
        item = loot["countedItems"]["ItemType"]
        itemcount = loot["countedItems"]["ItemCount"]

        if item == "/Lotus/Types/Items/MiscItems/Alertium":
            item = "Nitan Extract"
        elif item == "/Lotus/StoreItems/Upgrades/Mods/FusionBundles/AlertFusionBundleLarge":
            item = "150 Endo"
        elif item == "/Lotus/StoreItems/Types/Recipes/Weapons/PangolinSwordBlueprint":
            item = "Pangolin Sword Blueprint"
        else:
            pass

        return {"credits": cred, "item": item, "amount": itemcount}





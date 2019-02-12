import configparser


class Alert:

    def __init__(self, num, alertId=None, activation=None, expiry=None, missionType=None, maxWaveNum=None, faction=None,
                 location=None, levelOverride=None, enemySpec=None, extraEnemySpec=None, vipAgent=None,
                 customAdvancedSpawners=None, minEnemyLevel=None, maxEnemyLevel=None, difficulty=None, seed=None,
                 archwingRequired=None, isSharkwingMission=None, missionReward=None, nightmare=None):

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
        self.nightmare = nightmare


    def getRemainingDuration(self, alertid):

        return self.activation-self.expiry

        #alert = self.listAlerts()[alertid]
        #tact = int(alert["Activation"]["$date"]["$numberLong"])
        #texp = int(alert["Expiry"]["$date"]["$numberLong"])

        #now = int(self.data["Time"])
        # warframe zeit ist in ms
        #time_left = texp-tact

        #print(texp-tact) # total duration
        #print(texp-now) # time left ??? but no

    def getAlertLoot(self):
        from wrapper import Wrapper
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

        if item is not None:
            item = Wrapper.getItemName(item)

        return {"credits": cred, "item": item, "amount": itemcount}


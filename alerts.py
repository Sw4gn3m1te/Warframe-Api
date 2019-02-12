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
        elif item == "/Lotus/StoreItems/Types/Recipes/WarframeRecipes/TrapperSystemsBlueprint":
            item = "Vauban System Blueprint"
        else:
            pass

        return {"credits": cred, "item": item, "amount": itemcount}
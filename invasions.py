class Invasion:

    def __init__(self, num, _id=None, Faction=None, Node=None, Count=None, Goal=None, LocTag=None,
                 Completed=None, AttackerReward=None, AttackerMissionInfo=None, DefenderReward=None,
                 DefenderMissionInfo=None, Activation=None):

        self.num = num
        self.invasionId = _id["$oid"]
        self.faction = Faction
        self.node = Node
        self.count = Count
        self.goal = Goal
        self.locTag = LocTag
        self.completed = Completed
        self.attackerReward = AttackerReward
        self.attackerMissionInfo = AttackerMissionInfo
        self.defenderReward = DefenderReward
        self.defenderMissionInfo = DefenderMissionInfo
        self.activation = Activation["$date"]["$numberLong"]

    def getPointsLeft(self):
        if not self.completed:
            return self.goal - self.count
        else:
            return 0

    def getInvasionLoot(self, posistion):
        from wrapper import Wrapper
        cred, itemcount = 0, 0
        item = None
        if posistion == "atk":
            loot = self.attackerReward
            if loot == []:
                return {"credits": 0, "item": None, "amount": 0}
        elif posistion == "def":
            loot = self.defenderReward
        else:
            raise Exception("position must be 'atk' or 'def' !")
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

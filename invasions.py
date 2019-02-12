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

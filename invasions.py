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

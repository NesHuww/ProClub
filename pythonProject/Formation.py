from Player import *
class Formation:
    def __init__(self, player:list, captain:Player, disposition:str):

        if type(disposition) != str:
            raise TypeError('disposition is not a string')
        #if len(disposition) == 3:
         #   if disposition[0] + disposition[1] +disposition[2] != 10:
          #      raise ValueError('there is not 10 players in your team (expected gk)')
        #else:
            #if disposition[0] + disposition[1] + disposition[2] + disposition[3] != 10:
             #   raise ValueError('there are not 10 players in your team (expected gk)')
        self._players = player
        self._captain = captain
        self._disposition = disposition
        self._team = {}


    def getDefense(self)->int:
        return self._disposition[0]

    def getMidfield(self)->int:
        return self._disposition[1]

    def getAttack(self)->int:
        return self._disposition[2]

    def getCaptain(self)->Player:
        return self._captain

    def getDisposition(self)->str:
        return self._disposition

    def getStriker(self)-> str:
        if len(self._disposition) == 4:
            return self._disposition[3]
        else:
            return f"Useless for {self._disposition}, try to get Attack Instead"


    def getDisposition(self)->str:
        content = ""
        if type(self.getStriker()) == str:
            content = f"{self.getDefense()}-{self.getMidfield()}-{self.getAttack()}"
        else:
            content = f"{self.getDefense()}-{self.getMidfield()}-{self.getAttack()}-{self.getStriker()}"
        return content



    def addPlayer(self, player):
        if not isinstance(player, Player):
            raise TypeError("addPlayer: player isn't a player")
        self._players.append(player)
        self.assignPost(player)

    def removePlayer(self, Player2)->None:
        self.players = [player for player in self.players if player.name != Player2.name]
        if Player in self._team[Player.getPosition()]:
            self._team[Player.getPosition()].remove(Player)

    def assignPost(self, player:Player)->bool:
        '''
        Assigns a player to a post. Return True if someone had been replaced
        :param player: Player you assign
        :return: True or false
        '''
        if player not in self._players:
            raise ValueError('Player is not in the team')
        result = False
        if player.getPosition() in self._team.keys():
            result = True
            if player.getPosition() in ["GK", "RB", "LB", "RW", "LW"]:
                self._team[player.getPosition()] = player.getName()
            else:
                self._team[player.getPosition()] = [self._team[player.getPosition()], player.getName()]
        else:
            self._team[player.getPosition()] = player.getName()
        return result




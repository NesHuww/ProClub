from Player import *

class Formation:
    def __init__(self, player:list, captain:Player, disposition:str):
        '''
        Constructor of Formation class
        :param player: array of players on the field
        :param captain: Formation's captain
        :param disposition: How the team plays : 433/4231/42222
        '''

        if type(disposition) != str:
            raise TypeError('disposition is not a string')
        if len(disposition) > 4:
            raise ValueError('disposition is too long (max: 4)')

        self._players = player
        self._captain = captain
        self._disposition = disposition
        self._team = {}


    def getDefense(self)->int:
        '''
        Return the number of player playing in defense
        :return: int
        '''
        return self._disposition[0]

    def getMidfield(self)->int:
        '''
        Return the number of player playing in midfield
        :return: int
        '''
        return self._disposition[1]

    def getAttack(self)->int:
        '''
        Return the number of player playing in Attack
        :return: int
        '''
        return self._disposition[2]

    def getCaptain(self)->Player:
        '''
        Return the player who is the captain of the team
        :return: Player
        '''
        return self._captain


    def getStriker(self)-> str:
        '''
        Return the number of striker, if there is two steps on midfield
        :return: int or string if useless
        '''
        if len(self._disposition) == 4:
            return self._disposition[3]
        else:
            return f"Useless for {self._disposition}, try to get Attack Instead"


    def getDisposition(self)->str:
        '''
        Return how the team plays on the fied
        :return: string
        '''
        content = ""
        if type(self.getStriker()) == str:
            content = f"{self.getDefense()}-{self.getMidfield()}-{self.getAttack()}"
        else:
            content = f"{self.getDefense()}-{self.getMidfield()}-{self.getAttack()}-{self.getStriker()}"
        return content


    def addPlayer(self, player)->None:
        '''
        Add a player on the player list and then add him at the good post
        :param player: Player you want to have
        :return: None
        '''
        if not isinstance(player, Player):
            raise TypeError("addPlayer: player isn't a player")
        self._players.append(player)
        self.assignPost(player)

    def removePlayer(self, Player2)->None:
        '''
        Remove a player from the player list and then from the team
        :param Player2:
        :return:
        '''
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

    def SortTactic(self)->None:
        '''
        Use to sort posts by their position in a field
        :return: None
        '''
        dic = {}
        for key in Player.posts:
            if key in self._team.keys():
                dic[key] = self._team[key]
        self._team.clear()
        for key in dic.keys():
            self._team[key] = dic[key]
        return None




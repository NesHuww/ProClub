from __future__ import annotations

from Player import *


class Formation:
    def __init__(self, player:list, captain:Player, disposition:str):
        '''
        Constructor of Formation class
        :param player: array of players on the field
        :param captain: Formation's captain
        :param disposition: How the team plays : 433/4231/42222
        Please, if you play with a 3 players defense or a 343, put 5 defenders
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
        return int(self._disposition[0])

    def getMidfield(self)->int:
        '''
        Return the number of player playing in midfield
        :return: int
        '''
        return int(self._disposition[1])

    def getAttack(self)->int:
        '''
        Return the number of player playing in Attack
        :return: int
        '''
        return int(self._disposition[2])

    def getCaptain(self)->Player:
        '''
        Return the player who is the captain of the team
        :return: Player
        '''
        return self._captain


    def getStriker(self)-> str|int:
        '''
        Return the number of striker, if there is two steps on midfield
        :return: int or string if useless
        '''
        if len(self._disposition) == 4:
            return int(self._disposition[3])
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


    def addPlayer(self, player:Player)->None:
        '''
        Add a player on the player list and then add him at the good post
        :param player: Player you want to have
        :return: None
        '''
        if not type(player) == Player:
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
                #cas de poste unique
                self._team[player.getPosition()] = [player.getName()]
            else:
                # cas de poste non unique où il y a quelqu'un
                lst = self._team[player.getPosition()]
                lst.append(player.getName())
                lst.sort()
                self._team[player.getPosition()] = lst
        else:
            #cas où c'est pas un poste unique et qu'il n'y a personne
            self._team[player.getPosition()] = [player.getName()]
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

    def _createBot(self, n:int)->Player:
        '''
        Function to create a bot number n in parameters (weight and height are automaticly 180, 60 (not the reals ones))
        :return: Player (the bot)
        '''
        if type(n) is not int:
            raise TypeError('n is not an integer')
        return Player(f"Bot{n}", 180, 60)

    def addBotsTeams(self)->None:
        '''
        Function to add bots to the team where there are no players
        :return: None
        '''
        nbBots = 1
        onePostField = ['GK', 'RB', 'LB', 'RW', 'LW']
        nbplayer = len(self._players)
        for post in onePostField:
            if post not in self._team.keys():
                Bot = self._createBot(nbBots)
                Bot.setPosition(post)
                self.addPlayer(Bot)
                nbBots +=1
        nbdef = 0
        if 'CB' not in self._team.keys():
            nbdef = self.getDefense()-2
        else:
            nbCb = len(self._team['CB'])
            nbdef = self.getDefense()-2-nbCb
        for iteration in range(nbdef):
            Bot = self._createBot(nbBots)
            nbBots += 1
            Bot.setPosition('CB')
            self.addPlayer(Bot)

        if self.getMidfield() == 3:
            nbmilnec = 3
            quatre = False

        else:
            nbmilnec = 4
            quatre = True
        posts = ['CM', 'CDM', 'CAM']
        for post in posts:
            if post in self._team.keys():
                nbmilnec = nbmilnec - len(self._team[post])
        if not quatre and nbmilnec != 0:
                for nb in range(nbmilnec):
                    Bot = self._createBot(nbBots)
                    nbBots += 1
                    Bot.setPosition('CM')
                    self.addPlayer(Bot)

            # else:
                # #4 étages
                # if self.getMidfield()==2:
                #     #milieu avec un MOC
                #     print(nbmilnec)
                #     if 'CM' in self._team.keys() and len(self._team['CM']) != 2:
                #         nbmilnec -=1
                #     for nb in range(nbmilnec):
                #         Bot = self._createBot(nbBots)
                #         nbBots+=1
                #         Bot.setPosition('CM')
                #         self.addPlayer(Bot)
                #     if 'CAM' not in self._team:
                #         Bot = self._createBot(nbBots)
                #         nbBots += 1
                #         Bot.setPosition('CAM')
                #         self.addPlayer(Bot)










        print(f"you added {nbBots} bot(s) to the team")
        return None



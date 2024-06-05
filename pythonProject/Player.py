from __future__ import annotations
import requests

import json



class Player:
    posts = ["GK", "LB", "CB", "RB", "CDM", "CM", "CAM", "LW", "RW", "ST"]
    def __init__(self, name: str, height: float|int, weight: float|int, mean: float|int = 6.0, position:str="" ):
        '''
        build a player
        :param name: The name has to be the one you play with (EA account)
        :param height:
        :param weight:
        :param mean optional:
        :param position optional:
        '''
        if type(name) != str:
            raise TypeError('name isn\'t a string')
        if type(height) != float and type(height) != int:
            raise TypeError('height is not a number')
        if type(weight) != float and type(weight) != int:
            raise TypeError('weight is not a number')
        if type(mean) != float and type(mean) != int:
            raise TypeError('mean isn\'t a number')
        if type(position) != str:
            raise TypeError('position isn\'t a list')
        self._name = name
        self._position = position
        self._height = height
        self._weight = weight
        self._mean = mean

    def setName(self, name: str) -> None:
        '''
        name setter
        :param name: string
        :return: none
        '''
        if type(name) != str:
            raise TypeError('name you gave isn\'t string')
        self._name = name

    def setPosition(self, position: str) -> None:
        '''
        position setter
        :param position: has to be in available posts (getAvailablePosts)
        :return: None
        '''
        if position not in Player.posts:
            raise ValueError('position isn\'t in available positions')
        self._position = position


    def setHeight(self, height:float|int) -> None:
        '''
        height setter
        :param height: has to be a float or a int
        :return: None
        '''
        if type(height) != float and type(height) != int:
            raise TypeError('height isn\'t a float or an integer')
        self._height = height

    def setWeight(self, weight) -> None:
        '''
        weight setter
        :param weight: has to be a float or a int
        :return: None
        '''
        if type(weight) != float and type(weight) != int:
            raise TypeError('weight isn\'t a float or an integer')
        self._weight = weight

    def setMean(self, mean: float)->None:
        '''
        mean setter
        :param mean: has to be a float
        :return: None
        '''
        if type(mean) != float:
            raise TypeError('height isn\'t a float or an integer')
        self._mean = mean

    def getName(self) -> str:
        '''
        Name getter
        :return: string
        '''
        return self._name

    def getPosition(self) -> str:
        '''
        Position getter
        :return: string
        '''
        return self._position

    def getHeight(self) -> float|int:
        '''
        Height getter
        :return: float|int
        '''
        return self._height

    def getWeight(self) -> float|int:
        '''
        Weight getter
        :return: float|int
        '''
        return self._weight

    def getMean(self)->float:
        '''
        Mean getter
        :return: float
        '''
        return self._mean

    def getAvailablePosts(self):
        '''
        Available posts getter
        :return: array of availables posts
        '''
        return Player.posts


    def hasBetterMean(self, player2: Player) -> bool:
        '''
        Return true if player passed in parameter has a worst mean than actual player.
        :return: bool
        '''
        if type(player2) != Player:
            raise TypeError('betterMean : Player in parameter is not a player')
        return self._mean > player2.getMean()





    def __str__(self)->str:
        '''
        print how the player is
        :return: string, magical function.
        '''
        return f'Player:{self.getName()}\nHeight:{self.getHeight()}\nWeight:{self.getWeight()}\nPositions:{self.getPosition()}\nMean:{self.getMean()}'



from __future__ import annotations


class Player:
    posts = ["GK", "LB", "RB", "CB", "CDM", "CM", "CAM", "LW", "RW", "ST"]

    def __init__(self, name: str, height: float|int, weight: float|int, mean: float|int = 6.0, position:str="" ):
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
        self._name = name

    def setPosition(self, position: str) -> None:
        if position not in Player.posts:
            raise ValueError('position isn\'t in available positions')
        self._position = position

    def setHeight(self, height) -> None:
        self._height = height

    def setWeight(self, weight) -> None:
        self._weight = weight

    def setMean(self, mean: float):
        self._mean = mean

    def getName(self) -> str:
        return self._name

    def getPosition(self) -> str:
        return self._position

    def getHeight(self) -> float:
        return self._height

    def getWeight(self) -> float:
        return self._weight

    def getMean(self):
        return self._mean

    def hasBetterMean(self, player2: Player) -> bool:
        '''
        Return true if player passed in parameter has a worst mean than actual player.
        '''
        if type(player2) != Player:
            raise TypeError('betterMean : Player in parameter is not a player')
        return self._mean > player2.getMean()

    def __str__(self):
        return f'Player:{self.getName()}\nHeight:{self.getHeight()}\nWeight:{self.getWeight()}\nPositions:{self.getPosition()}\nMean:{self.getMean()}'



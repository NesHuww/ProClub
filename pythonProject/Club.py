from Formation import *
import requests
import json
from PIL import Image, ImageDraw, ImageFilter




class Club:
    def __init__(self, name:str, formation:Formation, id:int):
        '''
        Club constructor
        :param name:name of club
        :param formation:how the club plays
        :param id:club id
        '''
        self._name = name
        self._id = id
        self._formation = formation
        self._formation.SortTactic()
        self._players = []
        self._record = self.setRecord()


    def getName(self)->str:
        '''
        Club name getter
        :return: s tring
        '''
        return self._name

    def getCaptain(self)->str:
        '''
        Club captain name getter
        :return: str
        '''
        return self._captain.name

    def getFormation(self)->Formation:
        '''
        Club Formation getter (with bots)
        :return: Formation
        '''
        self._formation.addBotsTeams()
        self._formation.SortTactic()
        return self._formation._team


    def getRecord(self)->dict:
        '''
        Club record getter
        :return: dict
        '''
        return self._record




    def setName(self, name:str)->None:
        '''
        Club name setter
        :param name: has to be a string
        :return: None
        '''
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        self._name = name


    def setFormation(self,formation:Formation)->None:
        '''
        Club formation setter
        :param formation: has to be a formation
        :return: None
        '''
        if not isinstance(formation,Formation):
            raise TypeError("Formation isn't a Formation.")
        self._formation = formation



    def _getPlayerName(self, data:dict)->list:
        lst_name = []
        for name in range(len(data)):
            lst_name.append(data[name]['name'])
        return lst_name


    def _getClubData(self)->str:
        '''
        Data of the club getter
        :return: Data of a club, which is not epurated
        '''
        id = str(self._id)
        url = f'https://proclubs.ea.com/api/fc/members/stats?platform=common-gen5&clubId={id}'
        headers = {
            "Host": "proclubs.ea.com",
            "Sec-Ch-Ua": '"Chromium";v="125", "Not.A/Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Upgrade-Insecure-Requests": "1",
            "Cookie": "",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
            "Priority": "u=0, i",
            "Connection": "keep-alive"
        }

        try:
            response = requests.get(url, timeout=10, headers=headers)
            response.raise_for_status()
            content = response.text
        except requests.exceptions.RequestException as e:
            content = f"getClubData: {e}"
        i = 0
        while content[i] != '[':
            content = content[1:]
        k = len(content)-1
        while content[k] != ']':
            content = content[:k-1]
            k = len(content) - 1
        return content


    def setRecord(self)->dict:
        '''
        Record setter, automaticly update when you create a club
        :return: dictionnary of wins, ties and losses
        '''
        id = str(self._id)
        url = f'https://proclubs.ea.com/api/fc/clubs/overallStats?platform=common-gen5&clubIds={id}'
        headers = {
            "Host": "proclubs.ea.com",
            "Sec-Ch-Ua": '"Chromium";v="125", "Not.A/Brand";v="24"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Upgrade-Insecure-Requests": "1",
            "Cookie": "",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
            "Priority": "u=0, i",
            "Connection": "keep-alive"
        }

        try:
            response = requests.get(url, timeout=10, headers=headers)
            response.raise_for_status()
            content = response.text
        except requests.exceptions.RequestException as e:
            content = f"getRecord: {e}"
        data = json.loads(content)[0]
        wins = int(data["wins"])
        losses = int(data["losses"])
        draws = int(data["ties"])
        dic = {}
        dic["W"] = (wins, round(wins/(wins+losses+draws),2))
        dic["D"] = (draws, round(draws/(wins+losses+draws),2))
        dic["L"] = (losses, round(losses/(wins+losses+draws),2))
        return dic


    def _getPlayerUpdate(self, player:Player)->dict:
        '''
        Player updater with last statistics (data with ea website)
        :return: None
        '''
        if not type(player) == Player:
            raise TypeError('club you gave is not a club')
        data = self._getClubData()
        data = json.loads(data)
        lst_name = self._getPlayerName(data)
        if player.getName() not in lst_name:
            raise ValueError('Player is not in the club you gave')
        else:
            indice = lst_name.index(player.getName())
        return data[indice]


    def getPlayerData(self,player:Player)->dict:
        '''
        Allow you to get the data you want from your player
        :param player: Player you want the data from
        :param lst_data: lst of data you want
        :return: Dict of data you want
        '''
        data = self._getPlayerUpdate(player)
        lst_available_data = ['gamesplayed', 'winrate', 'goals', 'assists', 'cleansheetsdef',
        'cleansheetsGK', 'shotSuccessRate', 'passesMade', 'passSuccessRate',
        'ratingAve', 'tacklesMade', 'tackleSuccessRate', 'proName', 'proPos',
        'proStyle', 'proHeight', 'proNationality', 'proOverall', 'proOverallStr',
        'manOfTheMatch', 'redCards', 'prevGoals', 'prevGoals1', 'prevGoals2',
        'prevGoals3', 'prevGoals4', 'prevGoals5', 'prevGoals6', 'prevGoals7',
        'prevGoals8', 'prevGoals9', 'prevGoals10', 'favoritePosition']

        for key in range(len(lst_available_data)):
            lst_available_data[key] = lst_available_data[key].lower()
        lst_wanted_data = ['name']
        print("here is all the data you can ask, if you want all the data, type all, else, type each data one by one.")
        print("when you don't want data anymore, type no")
        print(lst_available_data)
        quest = 'a'
        while quest.lower() != 'no' and quest.lower() != 'all':
            quest = input('What data do you want ? (no if you want to stop)').lower()
            if quest == 'no':
                break
            if quest == 'all':
                return self._getPlayerUpdate(player)
            else:
                if quest not in lst_available_data:
                    raise ValueError("The data you entered isn't available please restart")
                lst_wanted_data.append(quest)
        lst_result = {}
        if len(lst_wanted_data) == 0:
            raise ValueError("you asked for no data")
        for key in data.keys():
            if key.lower() in lst_wanted_data:
                lst_result[key] = data[key]
        return lst_result


    def generateTactics(self):
        '''
        This function generates the image of the tactic
        :return: an image
        '''
        im1 = Image.open('../images/field.png')
        print(im1)

    def __str__(self)->str:
        '''
        Function to have a good print of a club
        :return: string
        '''
        return f"Club: {self._name}\nCaptain: {self._formation.getCaptain().getName()}\nFormation: {self._formation.getDisposition()}\nEquipe: {self.getFormation()}\nHistorique: {self.getRecord()}"
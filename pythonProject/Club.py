from Formation import *
import requests
import json
import simplejson


class Club:
    def __init__(self, name:str, formation:Formation, id:int):
        self._name = name
        self._id = id

        self._formation = formation
        self._players = []
        self._record = {"W": 0, "L": 0, "D": 0}


    def getName(self):
        return self._name

    def getCaptain(self):
        return self._captain.name

    def getFormation(self):
        return self._formation


    def getRecord(self):
        return self._record


    def setName(self, name:str):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        self._name = name

    def setCaptain(self, captain:Player):
        if not isinstance(captain,Player):
            raise TypeError("Captain isn't a Player object.")
        self._captain = captain

    def setFormation(self,formation:Formation):
        if not isinstance(formation,Formation):
            raise TypeError("Formation isn't a Formation.")
        self._formation = formation

    def getFormation(self)->dict:
        print(self._formation._team)


    def getClubInfos(self):
        id = str(self._id)
        url = f'https://proclubs.ea.com/api/fc/members/career/stats?platform=common-gen5&clubId={id}'
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
            content = f"ça bug: {e}"
        i = 0
        while content[i] != '[':
            content = content[1:]
        k = len(content)-1
        while content[k] != ']':
            content = content[:k-1]
            k = len(content) - 1
        return content


    def __str__(self):
        return f"Club: {self._name}\nCaptain: {self._formation.getCaptain().getName()}\nFormation: {self._formation.getDisposition()}"
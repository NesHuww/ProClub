from Player import *
from Club import *
from Formation import *
import json
from PIL import Image, ImageDraw, ImageFilter


NesHuw = Player("NesHuw", 178, 70)

NesHuw.setPosition("CM")

Formation = Formation([NesHuw],NesHuw, "433")

AleZai = Player("AleZai", 178, 70)
AleZai.setPosition("ST")


Bloody = Player("BloodyHD_51", 175, 70)
Bloody.setPosition("CAM")

AleZai = Player("AleZai", 185, 80)
AleZai.setPosition("ST")

Linoa = Player("Linoa", 168, 59)
Linoa.setPosition("CM")


RaideNN = Player("RaideNN", 190, 100)
RaideNN.setPosition("CB")

Paussax = Player("Paussax", 180, 70)
Paussax.setPosition("RW")

Naiz = Player("Naiz", 194, 90)
Naiz.setPosition("ST")

Antho = Player("Antho", 177, 69)
Antho.setPosition("CM")

Simisola = Player("Simisola", 170, 65)
Simisola.setPosition("LW")


#Formation.assignPost(NesHuw)
Formation.addPlayer(AleZai)
Formation.addPlayer(RaideNN)
#Formation.addPlayer(Linoa)
Formation.addPlayer(Paussax)
#Formation.addPlayer(Antho)
Formation.addPlayer(Simisola)


club = Club('PSG ARMY', Formation, 10102285)


#club.getFormation()

#infos = club._getClubData()
#parsed_json = json.loads(infos)

# Afficher le résultat pour vérifier
#(parsed_json[0])
#print(club.getPlayerData(AleZai))


print(club)

club.generateTactics()



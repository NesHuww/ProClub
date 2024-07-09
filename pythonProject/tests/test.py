import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Player import *
from Club import *
from Formation import *


import json



NesHuw = Player("NesHuw", 178, 70)

NesHuw.setPosition("CM")

club = Club('Fc Chillwell FR',  19371303)

#club.getClubData()

Qarter = Player("ProjectL_QARTER", 160, 50)

print(club.getPlayerData(Qarter))
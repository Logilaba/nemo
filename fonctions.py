
from classes import *
from constantes import *

def personnages_au_meme_endroit (personnage1, personnage2):
    print(personnage2.case_y, personnage2.case_x)
    print(personnage2.y, personnage2.x)
    if personnage1.x != personnage2.x:
        return False
    if personnage1.y != personnage2.y:
        return False
    return True

def pouvoir_touche_monstre (action1, action2):
    if action1.x != action2.x:
        return False
    if action1.y != action2.y:
        return False

    return True

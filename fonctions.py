

def personnages_au_meme_endroit (personnage1, personnage2):
    print(personnage2.x, personnage2.y)
    if personnage1.x != personnage2.x:
        return False
    if personnage1.y != personnage2.y:
        return False
    return True

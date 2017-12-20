#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images
"""

import pygame
from pygame.locals import *

from classes import *
from constantes import *
from fonctions import *

pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
#Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(titre_fenetre)
fin = pygame.image.load(image_defin).convert()
info = pygame.image.load(image_dinfo).convert()
fond_demon = pygame.image.load(image_Fdemon).convert()
mur_demon = pygame.image.load(image_Mdemon).convert()
accueil = pygame.image.load(image_accueil).convert()
fond = pygame.image.load(image_fond).convert()
perso_choix = pygame.image.load(image_perso).convert()
point_vie = pygame.font.SysFont ("Arial", 12)
coeur = pygame.image.load(image_coeur).convert_alpha()

#BOUCLE PRINCIPALE

prochaine_etape = ACCUEIL

while prochaine_etape != FIN:
	fenetre.blit(accueil, (0,0))
	pygame.display.flip()

	#BOUCLE D'ACCUEIL - CHOIX NIVEAU
	while prochaine_etape == ACCUEIL:
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			#Si l'utilisateur quitte, on met les variables
			#de boucle à 0 pour n'en parcourir aucune et fermer
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				prochaine_etape = FIN
			elif event.type == KEYDOWN:
				if event.key == K_RETURN:
					choix = 'n1'
					prochaine_etape = "choix_perso"
				elif event.key == K_F2:
					choix = 'n2'
					prochaine_etape = "choix_perso"
				elif event.key == K_F3:
					choix = 'n3'
					prochaine_etape = "choix_perso"
				elif event.key == K_F4:
					choix = "n4"
					prochaine_etape = "choix_perso"

	if choix != 0:
		niveau = Niveau(choix)

	#BOUCLE DE CHOIX DE PERSO
	while prochaine_etape == CHOIX_PERSO:
		print("choix_perso")
		pygame.time.Clock().tick(30)
		pygame.display.flip()
		fenetre.blit(perso_choix,(0,0))


		for event in pygame.event.get():
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				prochaine_etape = FIN
			elif event.type == KEYDOWN:
				if event.key == K_F1:
					choix_perso = 'Tanguy'
					demon = True
					prochaine_etape  = INFO
				elif event.key == K_F2:
					choix_perso = 'Alex'
					demon = False
					prochaine_etape = INFO

	vie = 5
	if choix_perso != 0:
		ms = Monstre("images/monstre_gauche.png", "images/monstre_droite.png",
					 "images/monstre_dos.png", "images/monstre_face.png",
					 niveau)

		if choix_perso == "Alex":
			dk = Hero("images/droite.png", "images/gauche.png",
			"images/dos.png", "images/face.png", niveau, choix_perso, vie)
		else:
			dk = Hero("images/vampire_droit.png", "images/vampire_gauche.png",
			"images/vampire_dos.png", "images/vampire_face.png", niveau, choix_perso, vie)


		niveau.generer()
		niveau.afficher(fenetre)


	#BOUCLE DE info
		while prochaine_etape == INFO:
			print("info")
			fenetre.blit(info,(0,0))
			pygame.display.flip()
			pygame.time.Clock().tick(30)


			for event in pygame.event.get():
				if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
					prochaine_etape = FIN
				elif event.type == KEYDOWN:
					prochaine_etape = NIVEAU_1
					etape = NIVEAU_1





	#BOUCLE DE NIVEAU 1
	pygame.display.flip()
	fenetre.blit (coeur,(300,20))
	for numero_niveau in range(1, 5) :
		niveau = Niveau('n' + str(numero_niveau), demon)
		niveau.generer()
		niveau.afficher(fenetre)
		dk.teleporter(niveau)
		prochaine_etape = "niveau " + str(numero_niveau)
		while prochaine_etape == etape:
			pygame.time.Clock().tick(30)
			pv = point_vie.render (str(dk.vie),1,(255,255,255))

			for event in pygame.event.get():
				if event.type == QUIT:
					prochaine_etape = FIN

				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						prochaine_etape = ACCUEIL

					#Touches de déplacement de Donkey Kong
					elif event.key == K_RIGHT:
						dk.deplacer('droite')
					elif event.key == K_LEFT:
						dk.deplacer('gauche')
					elif event.key == K_UP:
						dk.deplacer('haut')
					elif event.key == K_DOWN:
						dk.deplacer('bas')

					elif event.key == K_z:
						ms.deplacer("haut")
					elif event.key == K_s:
						ms.deplacer("bas")
					elif event.key == K_q:
						ms.deplacer("gauche")
					elif event.key == K_d:
						ms.deplacer("droite")

			if demon == False:
				fenetre.blit(fond, (0,0))

			else:
				fenetre.blit(fond_demon, (0,0))
			niveau.afficher(fenetre)
			fenetre.blit(dk.direction, (dk.x, dk.y))
			fenetre.blit(ms.direction, (ms.x, ms.y))
			fenetre.blit (coeur,(415,4))
			fenetre.blit(pv, (425, 10))
			pygame.display.flip()




			if niveau.structure[dk.case_y][dk.case_x] == 'a':
				etape = "niveau " + str(numero_niveau + 1)
				prochaine_etape = VICTOIRE

			if personnages_au_meme_endroit(dk, ms):
				if dk.vie > 0:
					dk.vie = dk.vie - 1
				else:
					prochaine_etape = VICTOIRE


	#BOUCLE DE VICTOIRE
	while prochaine_etape == VICTOIRE:
		pygame.time.Clock().tick(30)
		fenetre.blit(fin, (0,0))
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == QUIT:
				prochaine_etape = FIN

			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					prochaine_etape = FIN

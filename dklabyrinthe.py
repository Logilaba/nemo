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
bl = pygame.image.load(image_pouvoir).convert_alpha()
fin = pygame.image.load(image_defin).convert()
info = pygame.image.load(image_dinfo).convert()
fond_demon = pygame.image.load(image_Fdemon).convert()
mur_demon = pygame.image.load(image_Mdemon).convert()
accueil = pygame.image.load(image_accueil).convert()
fond = pygame.image.load(image_fond).convert()
perso_choix = pygame.image.load(image_perso).convert()
point_vie_monstre = pygame.font.SysFont ("Arial", 12)
point_vie = pygame.font.SysFont ("Arial", 12)
coeur = pygame.image.load(image_coeur).convert_alpha()
defaite = pygame.image.load(image_defaite).convert()

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
				elif event.key == K_F5:
					choix = "n5"
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

	poid = 0.1
	ms = Monstre("images/monstre_gauche.png", "images/monstre_droite.png",
				 "images/monstre_dos.png", "images/monstre_face.png",
		 		niveau, "images/monstre_face.png")

	# ms.x = 420

	# ms.y = 420
	# ms.case_x = 14
	# ms.case_y = 14
	if choix_perso != 0:
		if choix_perso == "Alex":
			dk = Hero("images/droite.png", "images/gauche.png",
			"images/dos.png", "images/face.png", niveau, choix_perso,"images/vampire_face.png")
		else:
			dk = Hero("images/vampire_droit.png", "images/vampire_gauche.png",
			"images/vampire_dos.png", "images/vampire_face.png", niveau, choix_perso, "images/vampire_face.png")

		niveau.generer()
		niveau.afficher(fenetre)


	#BOUCLE DE info
		while prochaine_etape == INFO:
			fenetre.blit(info,(0,0))
			pygame.display.flip()
			pygame.time.Clock().tick(30)


			for event in pygame.event.get():
				if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
					prochaine_etape = FIN
				elif event.type == KEYDOWN:
					prochaine_etape = NIVEAU_4
					etape = NIVEAU_4





	#BOUCLE DE NIVEAU
	pygame.display.flip()
	fenetre.blit (coeur,(300,20))
	for numero_niveau in range(1, 5) :
		niveau = Niveau('n' + str(numero_niveau), demon)
		niveau.generer()
		niveau.afficher(fenetre)
		dk.teleporter(niveau)
		ms.teleporter(niveau, 420, 420, 14, 14)
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
			fenetre.blit (coeur,(90, 0))
			fenetre.blit(pv, (100, 6))
			pygame.display.flip()




			if niveau.structure[dk.case_y][dk.case_x] == 'a':
				etape = "niveau " + str(numero_niveau + 1)
				prochaine_etape = "niveau_5"

			if personnages_au_meme_endroit(dk, ms):
				if dk.vie > 0:
					dk.vie = dk.vie - 1
					dk.retour()


			if dk.vie == 0:
				etape = "niveau " + str(numero_niveau + 1)
				prochaine_etape = DEFAITE

	numero_niveau = 5
	niveau = Niveau('n' + str(numero_niveau), demon)
	niveau.generer()
	niveau.afficher(fenetre)
	dk.teleporter(niveau, 0, 300, 0, 10)
	ms.teleporter(niveau, 420, 300, 14, 10)
	prochaine_etape = "niveau_5"

	pouvoir = None
	perso_position = "droite"

	while prochaine_etape == "niveau_5":
		print('coucou', etape)
		pygame.time.Clock().tick(30)
		pvm = point_vie_monstre.render (str(ms.vie),1,(255,255,255))
		pv = point_vie.render (str(dk.vie),1,(255,255,255))

		if pouvoir and pouvoir.pas_fini():
			pouvoir.deplacer(perso_position)

		for event in pygame.event.get():
			if event.type == QUIT:
				prochaine_etape = FIN

			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					prochaine_etape = ACCUEIL

				#Touches de déplacement de Donkey Kong
				elif event.key == K_RIGHT:
					perso_position = "droite"
					dk.deplacer(perso_position)
				elif event.key == K_LEFT:
					perso_position = 'gauche'
					dk.deplacer(perso_position)
				elif event.key == K_UP:
					perso_position = 'haut'
					dk.deplacer(perso_position)
				elif event.key == K_DOWN:
					perso_position = 'bas'
					dk.deplacer(perso_position)
				elif event.key == K_p:
					pouvoir = dk.pouvoir()

				elif event.key == K_SPACE:
					ms.deplacer("ciel")
				elif event.key == K_a:
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
		fenetre.blit(pvm, (423, 10))
		fenetre.blit (coeur,(90, 0))
		fenetre.blit(pv, (100, 6))
		if pouvoir != None and pouvoir.pas_fini():
			fenetre.blit(bl, (pouvoir.x, pouvoir.y))

		if pouvoir and pouvoir.fini():
			pouvoir = None

		pygame.display.flip()


		if personnages_au_meme_endroit(dk, ms):
			if dk.vie > 0:
				dk.vie = dk.vie - 1
				dk.retour()

		if dk.vie == 0:
			prochaine_etape = DEFAITE

		if pouvoir is not None and pouvoir_touche_monstre(pouvoir, ms):
			if ms.vie > 0:
				ms.vie = ms.vie - 1






		if ms.vie == 0:
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
	#BOUCLE DEFAITTE
	while prochaine_etape == DEFAITE:
		pygame.time.Clock().tick(30)
		fenetre.blit(defaite, (0,0))
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == QUIT:
				prochaine_etape = FIN

			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					prochaine_etape = FIN

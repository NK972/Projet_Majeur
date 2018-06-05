# Projet_Majeure

=======================Cahier des charges====================================

Objectif : 
	null
Fonctionnalit�e:
	null
Choix: 
	null
Valid�e:
	null
En cours:
	null
Modules:
	A remplir

========================Les lignes de commande====================================

Pepper1 peut �tre remplac� par l'adrresse ip de la cible

->Aller rapidement dans un dossier:
	cd ~/Documents/Projet_Majeur
	ssh nao@Pepper1 "cd /home/.local/share/PackageManager/apps/Projet_Majeure"
	ssh nao@Pepper1 "cd /home/projet/Robotcpe"

->Envoyer un dossier du PC au robot: 
	->Pour l'index:
		scp -r -p ~/Documents/Projet_Majeure nao@Pepper1/home/.local/share/PackageManager/apps/Projet_MajeureXXX
	->Pour le Dialogue:
		scp -r -p ~/Documents/Projet_Majeure nao@Pepper1/home/projet/Robotcpe

->Faut peut surpprimer les fichiers:
	ssh nao@Pepper1 "rm -rf /home/.local/share/PackageManager/apps/Projet_Majeure"
	ssh nao@Pepper1 "rm -rf /home/projet/Robotcpe"



=========================Lien vers web service======================================
https://algorithmia.com/algorithms/mheimann/RecognizeFaces  #Reconnaissance faciale
https://algorithmia.com/algorithms/deeplearning/GenderClassification #Reconnaissance de genre
https://www.chucknorrisfacts.fr/api/api # Les blagues de chuck norris

========================Utilisation de Git=========================================

Please mettre que les dossiers suivants sur GitHub, afin de bien distingu� le bon du mauvais.

Avant toutes utillisation de git aller dans le dossier "giter" puis faire la commande :
git pull #Cela permet de mettre � jour le dossier sur le pc
git commit -m "USER" #permet de pr�parer l'envoie de fichier
git push #Effectue l'envoie

Attention : 
git add /Chemin #permet l'ajout de nouveau composant au d�p�t git (sur le site)

=======================Compte Rendu 1: 05/06/2018==================================

Fonctionnel : 
	-> Dialogue fonctionnel � compl�ter.
	-> Tablette fonctionnel � compl�ter.
	-> Interaction tablette fonctionnel � compl�ter et am�liorer.

En cours : 
	->Les blagues de chuck norris, � intergrer aux fichiers ALTextToSpeech
	->Echolocalisation, voir le module 

A faire : 
	->Voir si il est possible de lancer tous les fichiers py � partir du PC
	->Page de menu lorsque le robot fait la pr�sentation avec les diff�rentes fonctionalit�s.
	->Lien en deux fichiers .py les possibilit�s sont :
		-> Ecriture dans un fichier, le plus simple
		-> Socket (Serveur/Clients), le plus pousser mais risque de perte de temps
		-> Multiprocessing, bof assez bizare comment lancer diff�rents process ...
		-> Autres protocole de communiquation, A vos Id�es
	->Les Webs Service: 
		-Reconnaissance de face
		-Reconnaissance de genre
		-A vos id�es
	->Des mouvements Pr�definies. 
	->Selon les phrases des comportements 

Conclusion :
	Apr�s 8h, nous avons peu avancer alors que nous n'avons pas encore attaquer les modules les plus dur. Il faut que l'on fournisse un travail plus cons�quent.
	Il faudrait aussi penser � nous fixer un Cahier des charges afin que l'on sache o� l'on va. 
	
=================================Les liens utiles==============================================
************naoqi****************
http://doc.aldebaran.com/2-4/naoqi/audio/altexttospeech-api.html #Pemet au Pepper de communiquer
http://doc.aldebaran.com/2-4/naoqi/peopleperception/alfacedetection-api.html #Permet au Pepper de faire de la reconnaissance facial sans wed service.
http://doc.aldebaran.com/2-4/naoqi/audio/alsoundlocalization-api.html#ALSoundLocalizationProxy::setParameter__ssCR.AL::ALValueCR #D�tecte la position d'un bruit.
http://doc.aldebaran.com/2-5/naoqi/core/almemory-tuto.html #Gestionnaire d'interruption.

============================Quelques installations utiles=====================================
Tous ceci se passe dans le terminal
**********pip************
1 - install "pip" :
	https://gist.github.com/haircut/14705555d58432a5f01f9188006a04ed
*********algorithmia******** 
2 - install "algorithmia":
	python pip intall --user algorithmia
V�rifier votre installation:
	python
	import Algorithmia


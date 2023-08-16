# Projet sécurité incendie 

## Constitution du dossier :

- .venv : Environnement virtuel contenant les bibliothèques essentielle au projet. 
- final : regroupe le projet avec toutes les applications nescésaire au fonctionnement du projet. 

## Constitution du dossier final : 

- alarme : dossier de l'application contenant le jeux sur l'alarle incendie.
- common : dossier contenant la base de donnée.
- connect : dossier de l'application contenat le système de connexion / inscription.
- evacuation : dossier de l'application contenant le jeu sur le plan d'évacuation 
- Extincteur : dossier de l'application contenant le jeu sur les extincteurs ainsi que le jeu sur le système de désenfummage
- fin : dossier de l'application contenant les pages de fin, le système d'export des données de la base de donnée aisni que la page de triche (s'il y a). Cette application sert à validé le jeux complet. 
- final : dossier contenat les paramêtres du projet. 
- handi : dossier contenant le jeu sur l'espace d'attente sécurisé
- passage : dossier contenat l'application qui permet d'affcicher les enigmes entre chaque jeux
- PDR : dossier de l'application contenant le jeu sur le sur le point de rassemblement
- porte : dossier de l'application contenant le jeu sur la porte coupe feu
- triangle : dossier de l'application contenant le jeu sur le triangle de feu. 
- db.sqlite3 : 
- manage.py : fichier qui permet de lancer le projet et l'afficher en local sur l'ordinateur. 
- testmdp.py : fichier avec un test de code de hashage de mot de passe.


## Explication du projet : 

Le projet est basé sur le framework Django. Le site est structuré de la manière suivante : 
1) application connect 
2) application triangle
3) application passage avec l'affichage de l'enigme de base [page d'acceuil de l'application] (réponse : alarme)
4) applicatoin alarme
5) application passage avec l'affichage de l'enigme extinceteur (réponse : extincteur)
6) application extincteur (affichage de la vue extincteur)
7) application passage avec l'affichage de l'enigme porte (réponse : porte)
8) application porte 
9) application passage avec l'affichage de l'enigme fume (résponse : désen)
10) application extincteur avec l'affichage de la vue fume (vue du jeu du système de désenfumage)
11) application passage avec l'affichage de l'enigme sécurité (réponse : sécu)
12) application handi 
13) application passage avec l'affichage de l'enigme evac (réponse : évacuation)
14) application evacuation 
15) application PDR (réponse du code : rass)
16) application fin: (fin du projet t2)
- si la personne n'a pas triché, on affiche la page d'acceuil de l'application
- si la personne a triché, on affiche la page triche
- on utilise cette application pour la page export de donnée. 

## Exporter les données de la base de données : 

Pour exporter les données, nous avons un réalisé un système de téléchargement d'un fichier csv (common separated values). 
Chaque champ est séparé par des virgules. 

Pour avoir accès au fichier, il faut se rendre sur l'application connect. Un fois sur la partie connexion, vous rentrer l'email administrateur ainsi que le mot de passe associé. 

Le téléchargement du fichier se lancera automatiquement. 

## Lancer le serveur : 

Pour lancer le porjet sur un serveur local (sur son ordinateur), il faut: 
- Ouvrir dans un terminal le dossier principale
- Activer l'environnement virtuel avec la commande suivant : 

```
.venv\scripts\activate

```

Vous ouvrez le dossier final

```

cd final 

```

Lancer le serveur : 

```
python manage.py runserver

```

Le site sera disponible sur le localhost à l'adresse suivante : http://127.0.0.1:8000/


## L'administration :

Mot de passe admin actuel :

- Nom d'utilisateur : admin
- email : admin@gmail.com
- mdp : superuser

Pour créer un administrateur, vous devez utilisé la commande suivante 

```
python manage.py createsuperuser

```

Il restera à choisir les étapes :
- usernanme
- email
- mot de passe
- confirmation mot de passe 

Et voilà, un administrateur est créé. 
Vous pouvez accéder à la base de donnée via l'adresse suivante en local: 

http://127.0.0.1:8000/admin

Une fois sur le lien, vous vous connectez avec votre username ainsi que votre mot de passe. 

## Axe d'amélioration 

- Chiffrage de mot de passe
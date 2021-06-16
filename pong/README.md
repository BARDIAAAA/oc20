# Projet Pong

## But du jeu
*Le tennis de table, plus fréquemment appelé "Ping-Pong" est un jeu olympique créé pour la première fois en 1890 par David Foster. Ce jeu est a seulement rejoins les sports olympiques en 1988 lors des JO de Séoul ([L'histoire du tennis de table](https://fr.cornilleau.com/content/55-lhistoire-du-tennis-de-table)). Vous le connaissez très certainement tous car c'est un jeu qui est très souvent joué en été lors des après-midi passés à la piscine ou juste chez un de vos amis. Le jeu consiste à donner une raquette à deux personnes qui vont devoir s'affronter. Ces deux personnes vont devoir, via leur raquette, tapper sur une balle et tenter de ne pas laisser la chance à l'adversaire de répondre.*

## Comment jouer ?
*Pour jouer, c'est très simple. Il faut tout d'abord être deux pour profiter du jeu au maximum. Vous pouvez y jouer seul mais c'est toujours plus amusant d'avoir un partenaire avec qui rigoler. Sachant que les raquettes peuvent uniquement monter et descendre, vous devez les utiliser pour battre votre adversaire. La raquette bleue monte en appuyant sur la touche "W" et descend en appuyant sur la touche "S". Pour la raquette rouge, c'est les flèches qu'il faut utiliser. La flèche du haut la fait monter et la flèche du bas la fait descendre. La partie est terminée lorsqu'une des personnes arrive à 5 points. À partir de ce moment-là, vous aurez deux possibilités : soit de recommencer une partie en appuyant sur la touche "ENTER", soit de quitter le jeu en appuyant sur la touche "ESC".*

**Pour résumer :**

* **W =** Monte la raquette bleue
* **S =** Descend la raquette bleue

* **Flèche du haut =** Monte la raquette rouge
* **Flèche du bas =** Descend la raquette rouge

* **ENTER =** Recommence une partie (À la fin d'une partie)
* **ESC =** Quitte le jeu (À la fin d'une partie)
  
![](resources/images/apercu.png)

## Les classes (structure interne de notre jeu)
* ***Settings :** classe où se trouvent toutes les images nécessaires au bon fonctionnement du jeu (Fantômes / Pac-Man), mais également la police et la musique.*
* ***Color :** classe où se trouvent toutes les couleurs dont nous aurons besoin, classe très basique.*
* ***Paddle :** classe qui va nous permettre de dessiner les rectangles qui vont être les murs du jeu.*
* ***Ball :*** *classe qui va permettre d'implanter les fantômes à tel ou tel endroit.*
* ***Game :*** *classe la plus importante, c'est par exemple celle qui va dessiner les murs, celle qui permettra de bouger Pac-Man, la classe principale.*

![](resources/images/diag.png)

## Amélioration possible sur le Pac-Man
*Aucune amélioration n'est à prévoir si le jeu à l'état actuel vous convient. Mais vous pouvez par exemple ajouter 2 raquettes pour que les parties soient du 2v2. Vous pouvez également ajouter une balle supplémentaire qui permettrait de donner encore plus de challenge au jeu. Ce sont des améliorations que vous pouvez apportez pour rendre le jeu encore plus complet mais le jeu à l'état actuel est déjà amplement suffisant.

## Cheminement
**[1]** *Parlons du commencement, j'ai tout d'abord commencé par créer les classes les plus simples et les plus logiques qui sont les classes "Color" et "Path", ce qui m'a permis d'ajouter les entités que je voulais, en pensant aussi à mettre la bonne taille à mon écran, qui saura correspondre à la map.*

**[2]** *Pour continuer, ce que j'ai fait et qui me semblait important, c'était d'ajouter les murs. C'est une longue étape mais une étape importante car c'est ce qui va donner le challenge au Pac-Man. Il faut prendre le temps de réfléchir au design de la map pour qu'elle soit optimale. Après avoir fait plusieurs croquis sur une feuille, je me suis lancé dans les calculs qui m'ont au final permis de dessiner les murs en faisant en sorte que les entités puissent juste passer entre les murs, ni plus ni moins.* 

**[3]** *La troisième étape consistait à ajouter les lieux de spawn des différentes entitées (Fantômes & Pac-Man). Les fantômes spawn dans leur petite cage 2 par 2 et Pac-Man spawn beaucoup plus bas.*

**[4]** *Les prochains étapes arriveront très prochainement, dans les quelques jours à suivre, le jeu sera complètement terminé et vous verrez les étapes qui m'ont permis d'y arriver ici.*

## Sources 
*Pour les sources que j'ai utilisé, je vais les classer dans différentes catégories que je vais nommer très clairement ci-dessous car je n'ai pas utilisé un Tutoriel à part entière mais un ensemble de sources différentes qui m'ont permis d'arriver jusqu'ici.*

* **[Création de rectangles] :**

      https://stackoverflow.com/questions/19780411/pygame-drawing-a-rectangle *(création de rectangles)*
      
* **[Téléchargement des entités] :**

      https://www.geeksforgeeks.org/python-display-images-with-pygame/#:~:text=Create%20a%20Image%20surface%20object,the%20pygame%20window%20using%20display.
  
* **[Document PyGame] :**

      https://www.pygame.org/docs/

* **[Musique] :**

      https://www.youtube.com/watch?v=fk_Klxd3-0A&t=7s

* **[Images] :**

*Les entités utilisées par notre jeu nous ont été données à la suite de notre demande par un volontaire.*

## Collaboration
*Mon ami Léandro (Merci à lui), pour ce jeu, m'a aidé à coder les fonctions qui se situent entre le SetMoving et le SetY (dans la classe Hero), ce sont des fonctions qui ne sont actuellement pas utilisées mais elles le seront plus tard. Le reste du travail a été effectué par moi-même (Bardia).*

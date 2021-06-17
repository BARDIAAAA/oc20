# Projet Pong

## Table des matières
* **1.** [But du jeu](##Butdujeu)
* **2.** [Comment jouer ?](##Commentjouer?)
* **3.** [Les classes (structure interne de notre jeu)](##Lesclasses(structureinternedenotrejeu))
* **4.** [Améliorations possibles](##Améliorationspossibles)
* **5.** [Cheminement](##Cheminement)
* **6.** [Sources](##Sources)


## But du jeu
*Le tennis de table, plus fréquemment appelé "Ping-Pong" est un jeu olympique créé pour la première fois en 1890 par David Foster. Ce jeu est a seulement rejoins les sports olympiques en 1988 lors des JO de Séoul ([L'histoire du tennis de table](https://fr.cornilleau.com/content/55-lhistoire-du-tennis-de-table)). Vous le connaissez très certainement tous car c'est un jeu qui est très souvent joué en été lors des après-midi passés à la piscine ou juste chez un de vos amis. Le jeu consiste à donner une raquette à deux personnes qui vont devoir s'affronter. Ces deux personnes vont devoir, via leur raquette, tapper sur une balle et tenter de ne pas laisser la chance à l'adversaire de répondre.*

<p align="center">
  <img width="650" height="500" src=http://www.collectionscanada.gc.ca/obj/001064/f1/0511ng-pintea5-v6.jpg>
</p>

---

## Comment jouer ?
*Pour jouer, c'est très simple. Il faut tout d'abord être deux pour profiter du jeu au maximum. Vous pouvez y jouer seul mais c'est toujours plus amusant d'avoir un partenaire avec qui rigoler. Sachant que les raquettes peuvent uniquement monter et descendre, vous devez les utiliser pour battre votre adversaire. La raquette bleue monte en appuyant sur la touche "W" et descend en appuyant sur la touche "S". Pour la raquette rouge, c'est les flèches qu'il faut utiliser. La flèche du haut la fait monter et la flèche du bas la fait descendre. La partie est terminée lorsqu'une des personnes arrive à 5 points. À partir de ce moment-là, vous aurez deux possibilités : soit de recommencer une partie en appuyant sur la touche "ENTER", soit de quitter le jeu en appuyant sur la touche "ESC".*

**Pour résumer :**

* **W =** Monte la raquette bleue
* **S =** Descend la raquette bleue
* **Flèche du haut =** Monte la raquette rouge
* **Flèche du bas =** Descend la raquette rouge
* **ENTER =** Recommence une partie (À la fin d'une partie)
* **ESC =** Quitte le jeu (À la fin d'une partie)

*Ci-dessous se trouve un visuel de notre Pong lorsque vous y jouez :*

<p align="center">
  <img width="650" height="500" src=https://i.ibb.co/VQ0KsNs/visuel.png>
</p>

---

## Les classes (structure interne de notre jeu) 
* ***Settings :*** *classe où se trouvent toutes les valeurs par défaut (Longeur, hauteur, rayon de la balle, et d'autres).*
* ***Color :*** *classe où se trouvent toutes les couleurs dont nous aurons besoin, classe très basique.*
* ***Paddle :*** *classe qui va comprendre les caractéristiques par défaut des paddles (les touches pour monter et descendre, le score de base, et d'autres).*
* ***Ball :*** *petite classe qui va décrire le lieu de spawn de la balle, ou la vitesse de la balle à l'origine.*
* ***Game :*** *classe la plus importante (classe mère), c'est cette classe qui va, par exemple, faire en sorte que le mouvement de la balle soit aléatoire, dessiner les différents points esthétiques, bouger la balle, les paddles, et mettre en place les collisions.*

<p align="center">
  <img width="650" height="500" src=https://i.ibb.co/WBWZrCW/thumbnail-diagrame-pong.jpg>
</p>

---

## Améliorations possibles <a name="améliorations possibles"></a>
*Aucune amélioration n'est à prévoir si le jeu à l'état actuel vous convient. Mais vous pouvez par exemple ajouter 2 raquettes pour que les parties soient du 2v2. Vous pouvez également ajouter une balle supplémentaire qui permettrait de donner encore plus de challenge au jeu. Ce sont des améliorations que vous pouvez apportez pour rendre le jeu encore plus complet mais le jeu à l'état actuel est déjà amplement suffisant.*

---

## Cheminement
**[1]** *Pour commencer le pong, ce que nous avons fait, c'est d'instaurer les valeurs par défaut de nos variables : Rapidité / Taille de la fenêtre / Rayon de la balle / Dimensions des raquettes / Couleurs, et d'autres. C'est le commencement.*

**[2]** *Nous avons continué avec la partie esthétique. Dessiner les lignes, les cercles, la balle sont indispensables pour un beau visuel.* 

**[3]** *Pour cette troisième étape, ce que nous avons en gros fait c'est d'ajouter les mouvements randoms de la balle, les mouvements des paddles, les collisions sur les différents murs. Ce qui nous permet de jouer au jeu.*

**[4]** *Pour cette dernière partie, nous nous sommes attardés sur la fin du jeu : l'affichage des fonctionnalités de fin (Victoire / Recommencer / Quitter / Limite jusqu'à 5 points).*

*Ci-dessous se trouve un visuel de notre Pong lorsque la partie est terminée :*

<p align="center">
  <img width="650" height="500" src=https://i.ibb.co/WpFYFW3/victoire.png>
</p>

---

## Sources 
*Pour les sources que nous avons utilisé, nous allons les classer dans différentes catégories que nous allons clairement très clairement ci-dessous.*

* **[Recherche & Compréhension pour "Pong"] :**

      https://www.youtube.com/watch?v=C6jJg9Zan7w
      https://www.geeksforgeeks.org/create-pong-game-using-python-turtle/
      https://www.101computing.net/pong-tutorial-using-pygame-getting-started/
      
* **[Code "Aide" que nous avons utilisé pour combler notre problème de collisions] :**

      https://gist.github.com/vinothpandian/4337527 
  
* **[Document PyGame] :**

      https://www.pygame.org/docs/

* **[Musique ("Wet Hand" C418 / Minecraft] :**

      https://www.youtube.com/watch?v=MSepOYJxB64

* **[Icône Aide] :**

      https://openclassrooms.com/forum/sujet/pygame-changer-l-icon-dans-la-barre-des-taches
      
* **[Icône image] :**

      https://www.kissclipart.com/ping-pong-racquet-sport-logo-racket-clip-art-nktr81/

* **[Ping-Pong 1988] :**

      https://www.collectionscanada.gc.ca/base-de-donnees/olympiens/001064-119.01-f.php?&photo_id_nbr=5185&brws_s=1&&PHPSESSID=dlbghk3a8459b5l4vpsjt2nhv0

* **[Aligner des images sur un README] :**

      https://gist.github.com/DavidWells/7d2e0e1bc78f4ac59a123ddf8b74932d

---

## Collaboration
*L'ensemble du code a été fait par nous-même mais comme stipulé dans les sources ci-dessus, nous avons utilisé, pour la partie des collisions, un code pré-existant qui nous a servit de "tutoriel".*

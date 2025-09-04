# WALE TECHNOLOGIE

## Description du projet

### Nom du projet : Projet Python 1

### Auteur : El Hadji Seydou Badiane

### Version : V1

### Objectif du projet

Ce projet est une application Python utilisant Tkinter qui permet à l'utilisateur de placer **4 points en forme de rectangle sur une zone de dessin**. Pour chaque point A,B,C et D le programme affiche les coordonnées.

---

## Installation et prérequis

### 1. Prérequis

- Python 3.x installé sur votre machine.
- La librairie Tkinter (généralement incluse par défaut avec Python).

Pour vérifier si Python est installé, vous pouvez lancer dans un terminal Python :

- sur windows :

```python
python --version ou python -V
```

- sur linux :

```python
python3 --version ou python3 -V
```

Si Python est installé, vous devriez voir une version similaire à la suivante : `3.x.x`

Pour vérifier si Tkinter est installé, vous pouvez lancer dans un terminal Python :

```python
import tkinter
print(tkinter.TkVersion)
```

Si Tkinter est installé, vous devriez voir une version similaire à la suivante : `8.6`

### 2. Installation

Étape 1 - Ouvrez un terminal et accédez au dossier où vous souhaitez stocker votre projet.

Étape 2 - Clonez le dépôt GitHub de ce projet en exécutant la commande suivante :

```bash
git clone https://github.com/Mister-Bajaan/wale_tech-projet_python1.git
```

Étape 3 - Accédez au dossier du projet :

```bash
cd wale_tech-projet_python1
```

Étape 4 - Lancez le script `main.py` en exécutant la commande suivante :

- sur windows :

```bash
python main.py
```

- sur linux :

```bash
python3 main.py 
```

L’application devrait s’ouvrir dans une fenêtre graphique avec une grille et vous pourrez commencer à cliquer pour placer les points.

---

## Fonctionnement du programme

L'application se compose de plusieurs parties distinctes :

### 1. Fenêtre principale et Canvas

- Le programme crée une **fenêtre Tkinter** avec une zone de dessin (`Canvas`) de 500x500 pixels.
- La couleur de fond est `#f6f6f6`.
- Le `Canvas` sert à afficher :
  - La **grille** pour positionner les points.
  - Les **points cliqués** par l'utilisateur.
  - Les **segments du rectangle** tracés automatiquement.

---

### 2. Grille

- La fonction `dessiner_grille_px()` dessine une **grille sur le Canvas** pour faciliter le placement des points.
- Paramètres :
  - `canvas` : le Canvas Tkinter.
  - `espacement_ligne` : distance en pixels entre les lignes de la grille (défaut 20).
  - `COULEUR_LIGNE_GRILLE` : couleur des lignes.

---

### 3. Placement des points

- Lorsque l'utilisateur clique sur le Canvas, la fonction `selectionner_point(event)` est appelée.
- Cette fonction :
  1. Récupère le nom du point à placer (`A`, `B`, `C`, `D`).
  2. Récupère les coordonnées `(x, y)` du clic.
  3. Stocke ces coordonnées dans le dictionnaire global`COORDONEES_POINT` en l'affectant à la clé correspondant au nom du point.
  4. Appelle `placer_point()` pour afficher le point sur le Canvas.
  5. Appelle `dessiner_segment()` pour tracer les segments du rectangle si 4 points sont présents.

---

### 4. Dessin des points

- La fonction `placer_point(point)` :
  - Dessine un **cercle** représentant le point.
  - Affiche le **nom du point** au-dessus.
  - Paramètres :
    - `point` : nom du point (`A`, `B`, `C`, `D`).
    - `canvas` : le Canvas Tkinter.
    - `couleur_point` : couleur du point.
    - `rayon_point` : taille du point.

---

### 5. Dessin des segments / rectangle

- La fonction `dessiner_segment(dict_points)` :
  1. Vérifie qu’il y a bien 4 points.
  2. Appelle `ordonner_points(dict_points)` pour obtenir les points dans l’ordre :
     - `haut_gauche`, `haut_droite`, `bas_droite`, `bas_gauche`.
  3. Utilise `create_polygon()` pour tracer le rectangle en une seule commande.
- Paramètres :
  - `dict_points` : dictionnaire contenant les coordonnées des points.
  - `canvas` : le Canvas Tkinter.
  - `couleur_segment` : couleur des segments.
  - `epaiseur_segment` : épaisseur des lignes.

---

### 6. Ordonnancement des points

- La fonction `ordonner_points(dict_points)` :
  - Calcule les **coordonnées extrêmes** (`min_x`, `max_x`, `min_y`, `max_y`).
  - Détermine les coins du rectangle :
    - `haut_gauche` = `(min_x, min_y)`
    - `haut_droite` = `(max_x, min_y)`
    - `bas_droite` = `(max_x, max_y)`
    - `bas_gauche` = `(min_x, max_y)`
  - Retourne un dictionnaire avec ces points pour garantir que le rectangle est tracé correctement, quel que soit l’ordre de clics.
- Paramètres :
  - `dict_points` : dictionnaire contenant les coordonnées des points.

---

### 7. Lancement du programme

- La fonction `main()` :
  - Dessine la grille.
  - Lie l’événement `<Button-1>` à la fonction `selectionner_point()`.
- `fenetre.mainloop()` lance la **boucle principale Tkinter**, qui rend la fenêtre interactive.

---

## Exemple d’utilisation

1. Lancez le programme avec `python main.py`.
2. Cliquez sur 4 points dans la zone de dessin pour former un rectangle.
3. Le programme affichera les points A, B, C et D avec leurs coordonnées sur le terminal.
4. Les segments du rectangle se dessinent automatiquement.

<!-- ### Exemple de coordonnées pour un rectangle :

- A (50, 50)
- B (200, 50)
- C (200, 100)
- D (50, 100)

Le rectangle apparaîtra ainsi :

A ----- B
|       |
D ----- C -->

## Limitations et améliorations possibles

### 1. Limitations

1.1. **Nombre fixe de points** :  

- Si l’utilisateur clique plus de 4 fois, aucun message s’affiche sur l'interface pour indiquer qu’il a dépassé le nombre de points.

1.2. **Manque d'indications** :

- L'utilisateur ne peut pas savoir en amont quelle point il va placer.
- Pas d'information sur la taille du rectangle.

1.3. **Interface simple** :  

- Pas de boutons pour interagir avec le programme.
- Pas de choix de couleur ou d’épaisseur des segments par l’utilisateur.
- La grille n'est pas graduée.

---

### 2. Améliorations possibles

2.1. **Interface plus interactive** :  

- Afficher les coordonnées des points sur la fenêtre principale.
- Ajouter un bouton "Réinitialiser" pour effacer les points et recommencer.
- Ajouter un bouton "Quitter" pour fermer la fenêtre.
- Afficher du texte sur la fenêtre pour indiquer quelle point va être placé.
- Afficher du texte sur la fenêtre pour indiquer la taille du rectangle.
- Graduer la grille pour faciliter le placement des points à des coordonnées précises.

2.2. **Options de personnalisation** :  

- Couleur et épaisseur des segments modifiable par l’utilisateur.
- Remplissage des rectangles possible.
from tkinter import Canvas, Tk, Frame, Label


# --------------------- Constantes --------------------- #

# Largeur et hauteur de la fenêtre
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700
BACKGROUND_COLOR = '#f6f6f6'

# Caractéristiques de la grille
COULEUR_LIGNE_GRILLE = '#e8e8ea'
ESPACEMENT_LIGNE = 20

# Caractéristiques des points
COORDONEES_POINT = {}
RAYON_POINT= 3
COULEUR_POINT = '#34495e'

# Caractéristiques des segments
EPAISEUR_SEGMENT = 2
COULEUR_SEGMENT = '#b7c2c8'


# Variables globales
NOMS_POINTS = ["A", "B", "C", "D"]




#--------------------- Configuration de l'interface : Fenêtre principale  ---------------------#

# Création de la fenêtre
fenetre = Tk()

# Titre de la fenêtre
fenetre.title("Coordonées des 4 points d'un rectangle")

# Récupération de la taille de l'écran
screen_width = fenetre.winfo_screenwidth()
screen_height = fenetre.winfo_screenheight()

# Calculer les coordonnées du centre de l'écran
center_x = int(screen_width/2 - WINDOW_WIDTH / 2)
center_y = int(screen_height/2 - WINDOW_HEIGHT / 2)

# Redimensionner la fenêtre
fenetre.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{center_x}+{center_y}')

# Ne pas pouvoir redimensionner la fenêtre
fenetre.resizable(False, False)

# Pour afficher une icône dans la fenêtre (Mettre le logo de l'entreprise dans le futur)
# fenetre.iconbitmap('path')

# Geometrie de la fenêtre pour avoir n colonnes et m lignes
## Pour avoir 3 colonnes
for i in range (3) :
    fenetre.columnconfigure(i, weight=1)

## Pour avoir 4 lignes
for i in range(4):
    fenetre.rowconfigure(i, weight=1)



#--------------------- Configuration de l'interface : Zone de dessin ---------------------#

"""
    --- Explication des attributs de la zone de dessin ---
    
    Canvas : Création d'une zone de dessin
    fenetre : Fenêtre principale (le parent de la zone de dessin, son conteneur)
    width : Largeur de la zone de dessin
    height : Hauteur de la zone de dessin
    background : Couleur de fond de la zone de dessin
"""

cadre_dessin = Canvas(fenetre, background=BACKGROUND_COLOR)
# configurer de la taille de la zone de dessin
cadre_dessin.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")


#--------------------- Configuration de l'interface : Zone pour les coordonnées de chaques points ---------------------#
frame_points = Frame(fenetre, bg="#e8e8ea")
frame_points.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=10, pady=5)



# Dictionnaire pour garder les labels existants
labels_points = {}

def afficher_coordonnees(nom_point, coord_x, coord_y):
    
    # Créer le label pour le point
    lbl = Label(frame_points, text=f"Les coordonnées de {nom_point} ( {coord_x}, {coord_y})", height= 1)
    
    # Positionner le label dans la frame (une colonne par point)
    col_index = len(labels_points)  # la colonne correspond au nombre de labels déjà existants
    lbl.grid(row=0,column=col_index, sticky="nsew", padx=8, pady=10) # étire le label dans toutes les directions
    
    #  Toutes les colonnes ont la même largeur
    frame_points.columnconfigure(col_index, weight=1) 
    
    # Toutes les lignes ont la même hauteur
    frame_points.rowconfigure(0, weight=1)
    
    # Ajouter le label à la liste des labels
    labels_points[nom_point] = lbl


#------------------------ Début du programme ------------------------#



# Cette fonction dessine une grille sur le canvas, pour faciliter le positionnement des points
def dessiner_grille_px(canvas= cadre_dessin, largeur_canvas=WINDOW_WIDTH, hauteur_canvas = WINDOW_HEIGHT, espacement_ligne=ESPACEMENT_LIGNE):
    """
    Dessine une grille sur le canvas avec un espacement donné en pixels.
    Par défaut, l'unité qu'utilise Tkinter est le pixel.
    
    Paramètres :
    - canvas : le Canvas Tkinter
    - largeur_canvas : largeur du Canvas en pixels
    - hauteur_canvas : hauteur du Canvas en pixels
    - espacement_px : distance entre deux lignes de la grille
    """
    # Lignes verticales 
    for x in range(0, largeur_canvas+1, espacement_ligne):
        canvas.create_line(x, 0, x, hauteur_canvas, fill=COULEUR_LIGNE_GRILLE)
    
    # Lignes horizontales
    for y in range(0, hauteur_canvas+1, espacement_ligne):
        canvas.create_line(0, y, largeur_canvas, y, fill=COULEUR_LIGNE_GRILLE)

# Cette fonction demande à l'utilisateur de saisir les coordonnées des points

i = 0


# Cette fonction permet de recupérer les coordonnées des points lorsque l'utilisateur clique sur la fenêtre
def selectionner_point(event):
        global i
        if i <= 3:
            # Recupération du nom du point
            nom_point = NOMS_POINTS[i]
            
            # Recupération des coordonnées du point
            x = event.x  # coordonnée x du clic
            y = event.y  # coordonnée y du clic
            
            # Ajout du point à la liste des coordonnées
            COORDONEES_POINT[nom_point] = (x, y)
        
            #Placer le point sur la fenêtre
            placer_point(nom_point)
            dessiner_segment(COORDONEES_POINT)
            afficher_coordonnees(nom_point, x, y)
            
            i += 1

        else:
            print("Tous les points sont déjà placés !")
            #TODO: Mettre une alerte pour indiquer que tous les points sont déjà placés

         
# Cette fonction dessine les points sur la fenêtre avec le nom du points
def placer_point(point, canvas= cadre_dessin,  couleur_point=COULEUR_POINT, rayon_point=RAYON_POINT):

    # Récupération des coordonnées du point
    x = COORDONEES_POINT[point][0] # coordonnée x du point A par exemple
    y = COORDONEES_POINT[point][1]
        
    print(f"les coordonnées de {point} sont : x = {x} et y = {y}")
    
    # Dessiner le point sous forme d'ellipse 
    canvas.create_oval(
        x - rayon_point, y - rayon_point,
        x + rayon_point, y + rayon_point,
        fill=couleur_point
    )
    
    # Afficher le nom du point juste à côté (au-dessus)
    canvas.create_text(
        x, y - 10,  # légèrement au-dessus du point
        text=point,
        fill="#1c1c1e",
    )
 
        
# Cette fonction dessine les segments reliant les points afin de former un rectangle
def dessiner_segment(dict_points, canvas=cadre_dessin, couleur_segment=COULEUR_SEGMENT, epaiseur_segment=EPAISEUR_SEGMENT):
    # Vérifier qu'on a bien 4 points
    if len(dict_points) != 4:
        print("Il faut 4 points pour dessiner le rectangle.")
        return
    
    # Réordonner les points qui sont dans notre dictionnaire
    points = ordonner_points(dict_points)
    
    # print(points)
    
    x1, y1 = points["haut_gauche"]
    x2, y2 = points["haut_droite"]
    x3, y3 = points["bas_droite"]
    x4, y4 = points["bas_gauche"]
    
    # Dessiner les 4 côtés
    canvas.create_polygon( 
        x1, y1, x2, y2, x3, y3, x4, y4,
        outline=couleur_segment,
        fill="",   # pas de remplissage
        width=epaiseur_segment
    )

    

# Fonction pour trier les points par ordre de X puis de Y
"""
    En principe : 
    Point haut à gauche (min_x, min_y) 
    Point haut à droite (max_x, min_y) 
    Point bas à droite  (max_x, max_y) 
    Point bas à gauche  (min_x, max_y) 
    
"""    
def ordonner_points(dict_points):
    # Recuperer les coordonnées des points sous forme de liste
    # Exemple : {"A": (120, 100), "B": (280, 200)} -> [(120, 100), (280, 200)]
    points = list(dict_points.values())
    

    # trouver les min et max en X et Y:
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)
    
    # Association des de chaque coin du rectangle aves ses coordonnées:
    point_haut_gauche = (min_x, min_y)   # haut-gauche
    point_haut_droite = (max_x, min_y)   # haut-droite
    point_bas_droite  = (max_x, max_y)   # bas-droite
    point_bas_gauche  = (min_x, max_y)   # bas-gauche

    # return {"A": point_haut_gauche, "B": point_haut_droite, "C": point_bas_droite, "D": point_bas_gauche}
    
    return {
        "haut_gauche": point_haut_gauche,
        "haut_droite": point_haut_droite,
        "bas_droite": point_bas_droite,
        "bas_gauche": point_bas_gauche
    }


# Fonction principale
def main(canvas= cadre_dessin):
    dessiner_grille_px()
    canvas.bind("<Button-1>", selectionner_point)

main()

"""
    --- Pour avoir un rectangle avec les points A, B, C et D ---
    
    A ----- B
    |       |
    D ----- C
    
    Xa = Xd
    Xb = Xc
    
    Xa = Xd < Xb = Xc
    
    Ya = Yb
    Yc = Yd
    
    Ya = Yb < Yc = Yd
    
    Exemple : Pour un rectangle de taille 150x50
    A(50,50) 
    B(200,50) 
    C(200,100) 
    D(50,100)
"""

# Lancer la fenêtre
fenetre.mainloop()
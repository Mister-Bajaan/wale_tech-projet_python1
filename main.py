from tkinter import Canvas, Tk



# --------------------- Constantes --------------------- #

# Largeur et hauteur de la fenêtre
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
BACKGROUND_COLOR = '#f6f6f6'

# Caractéristiques de la grille
COULEUR_LIGNE_GRILLE = '#e8e8ea'
EPACEMENT_LIGNE = 20

# Caractéristiques des points
COORDONEES_POINT = {}
RAYON_POINT= 3
COULEUR_POINT = '#34495e'

# Caractéristiques des segments
EPAISAUR_SEGMENT = 2
COULEUR_SEGMENT = '#b7c2c8'




#--------------------- Configuration de l'interface : Fenêtre principale  ---------------------#

# Création de la fenêtre
fenetre = Tk()

# Titre de la fenêtre
fenetre.title("Coordonées des 4 points d'un rectangle")



#--------------------- Configuration de l'interface : Zone de dessin ---------------------#

"""
    --- Explication des attributs de la zone de dessin ---
    
    Canvas : Création d'une zone de dessin
    fenetre : Fenêtre principale (le parent de la zone de dessin, son conteneur)
    width : Largeur de la zone de dessin
    height : Hauteur de la zone de dessin
    background : Couleur de fond de la zone de dessin
"""

cadre_dessin = Canvas(fenetre, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background=BACKGROUND_COLOR)

# Le gestioannaire du placement des widgets dans la fenêtre (On peut utiliser le pack() ou le grid())
cadre_dessin.pack()



#------------------------ Début du programme ------------------------#

# Cette fonction dessine une grille sur le canvas, pour faciliter le positionnement des points
def dessiner_grille_px(canvas= cadre_dessin, largeur_canvas=CANVAS_WIDTH, hauteur_canvas = CANVAS_HEIGHT, espacement_ligne=EPACEMENT_LIGNE):
    """
    Dessine une grille sur le canvas avec un espacement donné en pixels.
    Par défaut, l'unité qu'utilise Tkinter est le pixel.
    
    Paramètres :
    - cancvas : le Canvas Tkinter
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
def selectionner_point():
    for point in ["A", "B", "C", "D"]:
        x_point = int(input(f"Entrez la coordonnée x du point {point} : "))
        y_point = int(input(f"Entrez la coordonnée y du point {point} : "))
        COORDONEES_POINT[point] = (x_point, y_point)
         
# Cette fonction dessine les points sur la fenêtre
def placer_point(canvas= cadre_dessin, couleur_point=COULEUR_POINT, rayon_point=RAYON_POINT):
    
    for point in COORDONEES_POINT : 
    
        x = COORDONEES_POINT[point][0]
        y = COORDONEES_POINT[point][1]
        
        print(f"les coordonnées de {point} sont : x = {x} et y = {y}")
        
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
def dessiner_segment(canvas= cadre_dessin, couleur_segment=COULEUR_SEGMENT, epaiseur_segment=EPAISAUR_SEGMENT ) : 
    
    # Segment AB
    canvas.create_line(
        COORDONEES_POINT["A"][0], COORDONEES_POINT["A"][1],
        COORDONEES_POINT["B"][0], COORDONEES_POINT["B"][1],
        fill=couleur_segment,
        width=epaiseur_segment
    )
    
    # Segment BC
    canvas.create_line(
        COORDONEES_POINT["B"][0], COORDONEES_POINT["B"][1],
        COORDONEES_POINT["C"][0], COORDONEES_POINT["C"][1],
        fill=couleur_segment,
        width=epaiseur_segment
    )
    
    #Segment CD
    canvas.create_line(
        COORDONEES_POINT["C"][0], COORDONEES_POINT["C"][1],
        COORDONEES_POINT["D"][0], COORDONEES_POINT["D"][1],
        fill=couleur_segment,
        width=epaiseur_segment
     )
    
    #Segment DA
    canvas.create_line(
    COORDONEES_POINT["D"][0], COORDONEES_POINT["D"][1],
    COORDONEES_POINT["A"][0], COORDONEES_POINT["A"][1],
    fill=couleur_segment,
    width=epaiseur_segment
    )
    


# Fonction principale
def main():
    dessiner_grille_px()
    selectionner_point()
    placer_point()
    dessiner_segment()

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
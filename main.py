from tkinter import Canvas, Tk



# --------------------- Constantes --------------------- #

# Largeur et hauteur de la fenêtre
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
BACKGROUND_COLOR = '#f6f6f6'

# Coordonnées des points
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


# Cette fonction demande à l'utilisateur de saisir les coordonnées des points
def selectionner_point():
    for point in ["A", "B", "C", "D"]:
        x_point = int(input(f"Entrez la coordonnée x du point {point} : "))
        y_point = int(input(f"Entrez la coordonnée y du point {point} : "))
        COORDONEES_POINT[point] = (x_point, y_point)
       
        
# Cette fonction dessine les points sur la fenêtre
def dessiner_point(cadre_dessin, couleur_point=COULEUR_POINT, rayon_point=RAYON_POINT):
    
    for point in COORDONEES_POINT : 
    
        x = COORDONEES_POINT[point][0]
        y = COORDONEES_POINT[point][1]
        
        print(f"les coordonnées de {point} sont : x = {x} et y = {y}")
        
        cadre_dessin.create_oval(
            x - rayon_point, y - rayon_point,
            x + rayon_point, y + rayon_point,
            fill=couleur_point
        )
        
        # Afficher le nom du point juste à côté (au-dessus)
        cadre_dessin.create_text(
            x, y - 10,  # légèrement au-dessus du point
            text=point,
            fill="#1c1c1e",
        )
        
        
def dessiner_segment(cadre_dessin, couleur_segment=COULEUR_SEGMENT,epaiseur_segment=EPAISAUR_SEGMENT ) : 
    
    # Segment AB
    cadre_dessin.create_line(
        COORDONEES_POINT["A"][0], COORDONEES_POINT["A"][1],
        COORDONEES_POINT["B"][0], COORDONEES_POINT["B"][1],
        fill=couleur_segment,
        width=epaiseur_segment
    )
    
    # Segment BC
    cadre_dessin.create_line(
        COORDONEES_POINT["B"][0], COORDONEES_POINT["B"][1],
        COORDONEES_POINT["C"][0], COORDONEES_POINT["C"][1],
        fill=couleur_segment,
        width=epaiseur_segment
    )
    
    #Segment CD
    cadre_dessin.create_line(
        COORDONEES_POINT["C"][0], COORDONEES_POINT["C"][1],
        COORDONEES_POINT["D"][0], COORDONEES_POINT["D"][1],
        fill=couleur_segment,
        width=epaiseur_segment
     )
    
    #Segment DA
    cadre_dessin.create_line(
    COORDONEES_POINT["D"][0], COORDONEES_POINT["D"][1],
    COORDONEES_POINT["A"][0], COORDONEES_POINT["A"][1],
    fill=couleur_segment,
    width=epaiseur_segment
    )
    
    
def main():
    selectionner_point()
    dessiner_point(cadre_dessin)
    dessiner_segment(cadre_dessin)

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
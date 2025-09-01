from tkinter import Canvas, Tk



# --------------------- Constantes --------------------- #

# Largeur et hauteur de la fenêtre
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
BACKGROUND_COLOR = 'gray75'

# Coordonnées des points
COORDONEES_POINT = {}
RAYON_POINT= 3
COULEUR_POINT = 'blue'



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


"""
    --- Explication des fonctions ---
    selectionner_point() : Permet de choisir un point dans la fenêtre, pour le moment les coordonnées sont saisies manuellement par l'utilisateur
    dessiner_point() : Permet de dessiner un point dans la fenêtre
    
    --- Explication des variables ---
    point : Nom de la variable qui contient le nom du point sélectionné
    couleur_point : Nom de la variable qui contient la couleur du point sélectionné
    rayon_point : Nom de la variable qui contient le rayon du point sélectionné
    
    --- Explication des attributs ---
    x_point : Coordonnée x du point sélectionné
    y_point : Coordonnée y du point sélectionné
"""
def selectionner_point():
    numero_point = 1
    
    while numero_point <= 4:
        if numero_point == 1 :
            point = "A"
        elif numero_point == 2 : 
            point = "B"
        elif numero_point == 3 : 
            point = "C"
        elif numero_point == 4 : 
            point = "D"
        
        
        x_point = int(input(f"Entrez la coordonnée x du point {point} : "))
        y_point = int(input(f"Entrez la coordonnée y du point {point} : "))
        
        if numero_point == 1 : 
            COORDONEES_POINT["A"] = (x_point, y_point)
        elif numero_point == 2 : 
            COORDONEES_POINT["B"] = (x_point, y_point)
        elif numero_point == 3 : 
            COORDONEES_POINT["C"] = (x_point, y_point)
        elif numero_point == 4 : 
            COORDONEES_POINT["D"] = (x_point, y_point)
        
        numero_point += 1
        

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
    
    
def main():
    selectionner_point()
    dessiner_point()

main()

# Lancer la fenêtre
fenetre.mainloop()
from tkinter import Canvas, Tk



# --------------------- Constantes --------------------- #

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500
BACKGROUND_COLOR = 'gray75'



#--------------------- Configuration de l'interface : Fenêtre principale  ---------------------#

# Création de la fenêtre
fenetre = Tk()

# Titre de la fenêtre
fenetre.title("Rectangle avec 4 points") 



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

# Le gestioannaire du placement des widgets dans la fenêtre
cadre_dessin.pack()



# Lancer la fenêtre
fenetre.mainloop()
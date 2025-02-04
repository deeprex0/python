import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import random


#### PARITE 1 & 2
##### PARTIE 1 & 2 ###############
def lectureImage(chemin): 
    # Cette fonction lit une image à partir du chemin spécifié (chemin).
    # Elle utilise matplotlib pour charger l'image et retourne un tableau NumPy 
    # représentant les données de l'image.
    img = plt.imread(chemin)
    return img 

def AfficherImg(img):
    # Cette fonction affiche une image sans les axes (mode "off").
    # Les paramètres vmin=0 et vmax=255 sont utilisés pour garantir que l'image 
    # reste dans l'échelle appropriée des niveaux de gris (de 0 à 255).
    plt.axis("off")
    plt.imshow(img, cmap="gray", vmin=0, vmax=255)
    plt.show()

def saveImage(img):
    # Cette fonction sauvegarde une image dans un fichier intitulé "image1.png".
    # Elle utilise la méthode imsave de matplotlib pour enregistrer l'image telle quelle.
    plt.imsave("image1.png", img)

## NOTE SUR CES FONCTIONS :
## Ces trois fonctions permettent de lire, afficher et sauvegarder une image. 
## Cependant, dans leur usage, certaines limitations doivent être prises en compte :
## - Les paramètres vmin=0 et vmax=255 dans AfficherImg sont essentiels pour cree les images
##   en niveau de gris ou noir et blanc . mais au meme temps Leur omission peut causer 
##   des erreurs d'affichage si l'image dépasse cette intervalle.
## - La fonction lectureImage lit l'image en format RGB dans la plupart des cas,
##   ce qui peut poser problème si une manipulation en niveaux de gris est nécessaire. 
##   Pour cela, des fonctions spécifiques, comme Ouvrir (partie 3) ou grayscale (partie 5),
##   doivent être utilisées pour effectuer une conversion efficace en niveaux de gris.


##### PARTIE 3 : MANIPULATION D'IMAGES NOIR ET BLANC ########

def image_noire(h, l):
    # Question 3 : Créer une image noire.
    # Cette fonction génère une matrice de taille (h, l) contenant uniquement des 0, 
    # ce qui correspond à une image complètement noire.
    return np.zeros((h, l))  # Image noire.

def image_blanche(h, l):
    # Question 4 : Créer une image blanche.
    # Cette fonction génère une matrice de taille (h, l) contenant uniquement des 255, 
    # ce qui correspond à une image complètement blanche.
    return np.ones((h, l)) * 255  # Image blanche.

def ImageBlancNoir(h, l):
    # Quesiton 5 : Créer une image noire et blanche.
    # Cette fonction génère une matrice (h, l) où la valeur de chaque pixel (i, j) 
    # est calculée par (i + j) % 2, créant ainsi un motif en damier noir et blanc.
    return np.fromfunction(lambda i, j: (i + j) % 2, (h, l), dtype=int) * 255

def negatif(Img):
    # Question 6 : Créer le négatif d'une image.
    # Cette fonction génère une nouvelle image où chaque pixel est inversé :
    # - Les pixels noirs (0) deviennent blancs (1).
    # - Les pixels blancs (1) deviennent noirs (0).
    return 1 - Img  # Image négative.

# Fonction 7 : Tester les Fonctions (voir la documentation)  
# Remarque : Pour tester ces fonctions de manière interactive,  
# lancez le programme, puis choisissez de créer une image blanche, noire, ou en noir et blanc selon votre préférence.






##### PARTIE 3 : Manipulation des Images en Niveaux de Gris #####
# Note : Ces fonctions permettent d'analyser et de manipuler les images en niveaux de gris
# pour des opérations comme la luminance, le contraste, la profondeur et la conversion.

# Remarque : Dans l'exercice 11 de la partie "grayscale", il était demandé de retourner une matrice 
# représentant l'image en niveaux de gris. Cependant, la plupart des images sont au format RGB, même si elles 
# apparaissent comme des images en noir et blanc. Cela nécessite une conversion en niveaux de gris 
# pour effectuer des manipulations spécifiques. 
# Bien que la fonction classique "grayscale" effectue ce travail, elle peut être plus lente. 
# La méthode alternative proposée ici est plus rapide et adaptée aux besoins.

## Question 8 : Calcul de la Luminance
def luminance(img):
    # Cette fonction retourne la luminance moyenne de l'image en utilisant NumPy.
    return np.mean(img)

def luminance_Version0(img): 
    # Méthode classique pour calculer la luminance moyenne avec des boucles for.
    size = len(img[0]) * len(img)  # Nombre total de pixels.
    S = 0  # Somme des intensités des pixels.
    for rows in range(len(img)):
        for columns in range(len(img[0])):
            S += img[rows][columns]
    return S / size  # Retourne la moyenne des intensités.

## Question 9 : Calcul du Contraste
def contrast(img):
    # Cette fonction calcule le contraste de l'image (variance des niveaux de gris).
    mean = luminance(img)
    return np.mean((img - mean) ** 2)

def contrast_Version0(img):
    # Version classique pour calculer le contraste avec des boucles for.
    moy = luminance(img)
    N = img.size  # Nombre total de pixels.
    contrast = 0
    for rows in range(len(img)):
        for columns in range(len(img[0])):
            contrast += (img[rows][columns] - moy) ** 2
    return contrast / N  # Retourne la variance.

## Question 10 : Détermination de la Profondeur Maximale
def profondeur(img):
    # Cette fonction retourne la valeur maximale des intensités des pixels de l'image.
    return np.max(img)

def profondeur_Version0(img):
    # Méthode classique pour trouver la valeur maximale avec des boucles for.
    max_value = 0
    for rows in range(len(img)):
        for columns in range(len(img[0])):
            if img[rows][columns] > max_value:
                max_value = img[rows][columns]
    return max_value

## Question 11 : Ouvrir et Convertir une Image en Niveaux de Gris
def Ouvrir(chemin):  
    # Fonction pour ouvrir une image et la convertir en niveaux de gris si elle est en couleur.
    img = plt.imread(chemin)
    if img.ndim == 3:  # Si l'image est en couleur (3 dimensions : RGB).
        img = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])  # Conversion en niveaux de gris.
    return img

def Ouvrir_Version0(image):
    # Méthode classique pour convertir une image RGB en niveaux de gris.
    result = [[0 for _ in range(image.shape[1])] for _ in range(image.shape[0])]
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            r, g, b = image[i, j][:3]  # Extraction des canaux R, G, B.
            result[i][j] = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return np.array(result)  # Retourne une matrice de niveaux de gris.

##################################################################
##################################################################


##### PARTIE 4 ##############

## Quesion 12
def inverser(img):
    # Cette fonction renvoie l'inverse de l'image d'origine.
    # Le ton de chaque pixel dans la nouvelle image est calculé par 255 - v,
    # où v est la valeur d'origine du pixel.
    # Par exemple, un pixel avec une intensité de 200 deviendrait 55.
    return 255 - img

## Question 13
def flipH(img):
    # Cette fonction renvoie l'image transformée par symétrie horizontale
    # (axe vertical passant par le milieu de l'image). Utile pour inverser
    # l'image de gauche à droite.
    return np.fliplr(img)

## Question 14
def poserV(img1, img2):
    # Cette fonction prend en entrée deux images (img1 et img2)
    # de même largeur et profondeur.
    # Elle renvoie une nouvelle image obtenue en mettant img1 sur img2,
    # c'est-à-dire une concaténation verticale.
    if img1.shape[1] == img2.shape[1] and img1.shape[2] == img2.shape[2]:
        return np.vstack((img1, img2))  # Concaténation verticale.
    else:
        # Si les images n'ont pas les mêmes dimensions, lève une erreur.
        raise ValueError("Les images doivent avoir la même largeur et profondeur")

## Question 15
def poserH(img1, img2):
    # Cette fonction prend en entrée deux images (img1 et img2)
    # de même hauteur et profondeur.
    # Elle renvoie une nouvelle image obtenue en mettant img2 à droite de img1,
    # c'est-à-dire une concaténation horizontale.
    if img1.shape[0] == img2.shape[0] and img1.shape[2] == img2.shape[2]: 
        return np.hstack((img1, img2))  # Concaténation horizontale.
    else:
        # Si les images n'ont pas les mêmes dimensions, lève une erreur.
        raise ValueError("Les images doivent avoir la même hauteur et profondeur")


#############################


##### PARIE 5 ################
#Question 16 : 
    
'''
M=[[[210, 100, 255],[100, 50, 255],[90, 90, 255],[90, 90, 255],[90, 90, 255],[90, 80, 255]],
[[190, 255,89],[ 201, 255,29],[200, 255,100],[100, 255,90],[20, 255,200], [100, 255,80]],
[[255,0, 0],[ 255,0, 0],[255,0, 0],[255,0, 0],[255,0, 0], [255,0, 0]]]

'''
#print(M[0][1][1]) --> 50

#print(M[1][0][1]) --> 255

#print(M[2][1][0]) --> 255

#Guestion 17 :

'''
la quantité de mémoire nécessaire en octets (8 bits) pour stocker le tableau
représentant une image RGB est : 3 x N = 3 x H x L 
avec : 
    N : nombre de pixels égale à : N = H x L 
    ou :
        H est la hauteur de l'image RGB
        L est la largeur de l'image RGB 
Justification :    
Pour une image RGB, chaque pixel est représenté par 3 canaux de couleur : Rouge (R),
Vert (G), et Bleu (B). Chaque canal est généralement codé sur 1 octet (8 bits). 
La mémoire totale nécessaire dépend du nombre total de pixels de l'image.
'''
## Question 18
def initImageRGB(width, height):
    image = np.empty((height, width, 3), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            image[i, j] = [random.randrange(0, 256) for _ in range(3)]  # [R, G, B]
    return image

## Question 19
def symetrie_horizontale(img):
    return np.flipud(img)
def symetrie_verticale(img):
    return np.fliplr(img)

## Question 20
def grayscale(imageRGB):
    """
    Convertit une image RGB en une image en niveaux de gris en suivant l'algorithme spécifié.
    
    Arguments :
    - imageRGB : tableau NumPy représentant l'image en couleur (hauteur, largeur, 3).
    
    Retourne :
    - Un tableau NumPy de taille (hauteur, largeur) représentant l'image en niveaux de gris.
    """
    # Créer un tableau vide pour l'image en niveaux de gris avec la même hauteur et largeur que l'image originale
    hauteur, largeur, _ = imageRGB.shape
    gris_image = np.zeros((hauteur, largeur), dtype=np.uint8)
    
    # Parcourir chaque pixel de l'image
    for i in range(hauteur):
        for j in range(largeur):
            # Extraire les valeurs RGB du pixel
            r, g, b = imageRGB[i, j]
            
            # Calculer le maximum et le minimum des trois valeurs
            max_val = max(r, g, b)
            min_val = min(r, g, b)
            
            # Calculer la moyenne entière de ces valeurs maximales et minimales
            gris_val = (max_val + min_val) // 2
            
            # Assigner cette valeur au pixel dans l'image en niveaux de gris
            gris_image[i, j] = gris_val
    
    return gris_image
## le probleme avec cette grayscale fonction c'est que il prend une tres long duree pour transformer
#  l'image rgb a grayscale, et pour cela dans le programe on a travaile avec une version plue 
# efficace c'est transformImg(img)
###############################





##Partie Facultative : Comparaison et Avantages de Python
##Cette partie est facultative mais importante,
#  car elle illustre la puissance de Python par rapport à d'autres langages comme C. 
#  notre projet précédent écrit en C, nous avions développé un programme de gestion de stock de plus de 500 lignes,
# fonctionnant uniquement via le terminal. Cela limitait l'interactivité et la flexibilité.

##En revanche, avec Python, il est possible de développer une interface graphique interactive avec environ le même nombre de lignes,
#  grâce à des bibliothèques comme Tkinter. 
#  interfaces offrent des fonctionnalités conviviales et n'exigent aucune modification manuelle du code pour interagir avec le programme.



class ImageApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Mygip Application de traitement d'image")

        # Center align the entire frame
        self.main_frame = tk.Frame(master)
        self.main_frame.pack(fill="both", expand=True)

        # Configure a grid system for the main frame
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

        # Create two sub-frames for buttons
        self.left_frame = tk.Frame(self.main_frame)
        self.left_frame.grid(row=0, column=0, pady=10, padx=10)

        self.right_frame = tk.Frame(self.main_frame)
        self.right_frame.grid(row=0, column=1, pady=10, padx=10)

        # Left-side buttons
        self.upload_button = tk.Button(self.left_frame, text="Charger Image", command=self.upload_image, font=("Arial", 12))
        self.upload_button.pack(pady=5)

        self.height_label = tk.Label(self.left_frame, text="Longueur:", font=("Arial", 12))
        self.height_label.pack()
        self.height_entry = tk.Entry(self.left_frame, font=("Arial", 12))
        self.height_entry.pack()
        self.height_entry.insert(0, "256")

        self.width_label = tk.Label(self.left_frame, text="Largeur:", font=("Arial", 12))
        self.width_label.pack()
        self.width_entry = tk.Entry(self.left_frame, font=("Arial", 12))
        self.width_entry.pack()
        self.width_entry.insert(0, "256")

        self.create_black_button = tk.Button(self.left_frame, text="Creer Image Noir", command=self.create_black_image, font=("Arial", 12))
        self.create_black_button.pack(pady=5)

        self.create_white_button = tk.Button(self.left_frame, text="Creer Image Blanc", command=self.create_white_image, font=("Arial", 12))
        self.create_white_button.pack(pady=5)

        self.create_rgb_img_button = tk.Button(self.left_frame, text="Creer Image RGB", command=self.create_rgb_img, font=("Arial", 12))
        self.create_rgb_img_button.pack(pady=5)

        self.create_bnw_button = tk.Button(self.left_frame, text="Creer Imange Blanc et Noir", command=self.create_bnw_image, font=("Arial", 12))
        self.create_bnw_button.pack(pady=5)

        # Right-side buttons
        self.flip_horizontal_button = tk.Button(self.right_frame, text="Flip Horizontal", command=self.flip_horizontal, state="disabled", font=("Arial", 12))
        self.flip_horizontal_button.pack(pady=5)

        self.flip_vertical_button = tk.Button(self.right_frame, text="Flip Vertical", command=self.flip_vertical, state="disabled", font=("Arial", 12))
        self.flip_vertical_button.pack(pady=5)

        self.negate_button = tk.Button(self.right_frame, text="Image Negatif", command=self.negative_image, state="disabled", font=("Arial", 12))
        self.negate_button.pack(pady=5)

        self.calculate_luminance_button = tk.Button(self.right_frame, text="Claculer la  Luminance", command=self.calculate_luminance, state="disabled", font=("Arial", 12))
        self.calculate_luminance_button.pack(pady=5)

        self.calculate_contrast_button = tk.Button(self.right_frame, text="Calculer le Contrast", command=self.calculate_contrast, state="disabled", font=("Arial", 12))
        self.calculate_contrast_button.pack(pady=5)

        self.calculate_profondeur_button = tk.Button(self.right_frame, text="Calculer le Profondeur", command=self.calculate_profondeur, state="disabled", font=("Arial", 12))
        self.calculate_profondeur_button.pack(pady=5)

        self.cree_inverser_button = tk.Button(self.right_frame, text = " Inverser Image", command= self.cree_inverser, state = "disabled",  font=("Arial", 12))
        self.cree_inverser_button.pack(pady=5)


        self.trans_grayscale_button = tk.Button(self.right_frame, text="Transformer Grayscale", command=self.trans_grayscale, state="disabled", font=("Arial", 12))
        self.trans_grayscale_button.pack(pady=5)

        self.cree_poserH_button = tk.Button(self.right_frame, text="Pose Horizontal", command=self.cree_poserH, state="disabled", font=("Arial", 12))
        self.cree_poserH_button.pack(pady=5)

        self.cree_poserV_button = tk.Button(self.right_frame, text="Pose Vertical", command=self.cree_poserV, state="disabled", font=("Arial", 12))
        self.cree_poserV_button.pack(pady=5)

        self.afficher_image_button = tk.Button(self.right_frame, text="Afficher Image", command=self.afficher_image, state="disabled", font=("Arial", 12))
        self.afficher_image_button.pack(pady=5)

        self.save_image_button = tk.Button(self.right_frame, text=" Enregistrer L'Image", command=self.save_image, state="disabled", font=("Arial", 12))
        self.save_image_button.pack(pady=5)




        # Footer
        self.footer = tk.Label(self.main_frame, text="Realiser par: Daibbar, El Gueroua, Chigr, El Kouably, Bardoud", font=("Arial", 10), fg="gray")
        self.footer.grid(row=1, column=0, columnspan=2, pady=10)

        self.image = None

    def calculate_profondeur(self):
        if self.imagegray is not None:
            prof = profondeur(self.imagegray)
            messagebox.showinfo("Profondeur d'image", f"Profondeur: {prof:.2f}")
        else:
            messagebox.showerror("Error", "No image Charger!")

    def get_dimensions(self):
        try:
            height = int(self.height_entry.get())
            width = int(self.width_entry.get())
            return height, width
        except ValueError:
            messagebox.showerror("Error", " dimensions Invalid!")
            return None, None

    def upload_image(self):
        path = filedialog.askopenfilename(title="Selectionner Image File", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if path:
            self.image = lectureImage(path)
            self.imagegray = Ouvrir(path)
            messagebox.showinfo("Succée", "Image est bien Charger!")
            self.enable_buttons()
        else:
            messagebox.showwarning("Warning", "No image selectioner!")
    
    def save_image(self):
        if self.image is not None:
            saveImage(self.image)
            messagebox.showinfo("Succée", "Image est bien Enregistre: 'image1.png'!")
        else:
            messagebox.showerror("Error", "No image à Enregistrer!")



    def enable_buttons(self):
        self.flip_horizontal_button.config(state="normal")
        self.flip_vertical_button.config(state="normal")
        self.negate_button.config(state="normal")
        self.calculate_luminance_button.config(state="normal")
        self.calculate_contrast_button.config(state="normal")
        self.afficher_image_button.config(state="normal")
        self.calculate_profondeur_button.config(state="normal")
        self.trans_grayscale_button.config(state="normal")
        self.cree_poserH_button.config(state="normal")
        self.cree_poserV_button.config(state="normal")
        self.cree_inverser_button.config(state="normal")
        self.save_image_button.config(state="normal")


    def afficher_image(self):
        if self.image is not None:
            AfficherImg(self.image)
        else:
            messagebox.showerror("Error", "No image à afficher!")

    def flip_horizontal(self):
        if self.image is not None:
            self.image = symetrie_horizontale(self.image)
            messagebox.showinfo("Success", "Image est bien flipper horizontalement!")
        else:
            messagebox.showerror("Error", "No image Charger!")

    def flip_vertical(self):
        if self.image is not None:
            self.image = symetrie_verticale(self.image)
            messagebox.showinfo("Succée", "Image est bien flipper verticalement!")
        else:
            messagebox.showerror("Error", "No image Charger!")

    def negative_image(self):
        if self.image is not None:
            self.image = negatif(self.image)
            messagebox.showinfo("Succée", "Image est Bien Transformer!")
        else:
            messagebox.showerror("Error", "No image Charger!")

    def calculate_luminance(self):
        if self.imagegray is not None:
            lum = luminance(self.imagegray)
            messagebox.showinfo("Luminance", f"Luminance: {lum:.2f}")
        else:
            messagebox.showerror("Error", "No image Charger!")

    def calculate_contrast(self):
        if self.imagegray is not None:
            cont = contrast(self.imagegray)
            messagebox.showinfo("Contrast", f"Contrast: {cont:.2f}")
        else:
            messagebox.showerror("Error", "No image Charger!")

    def create_black_image(self):
        height, width = self.get_dimensions()
        if height and width:
            self.image = image_noire(height, width)
            messagebox.showinfo("Succée", " image Noir est bien Creer!")
            self.enable_buttons()

    def create_white_image(self):
        height, width = self.get_dimensions()
        if height and width:
            self.image = image_blanche(height, width)
            messagebox.showinfo("Succée", "Image blanc est bien Creer!")
            self.enable_buttons()

    def create_bnw_image(self):
        height, width = self.get_dimensions()
        if height and width:
            self.image =ImageBlancNoir(height, width)
            messagebox.showinfo("Succée", "Image Blan et Noir est Bien Creer!")
            self.enable_buttons()
    
    def create_rgb_img(self):
        height, width = self.get_dimensions()
        if height and width:
            self.image = initImageRGB(height, width)
            messagebox.showinfo("Succée", "Image est bien Creer!")
            self.enable_buttons()
    
    def trans_grayscale(self):
        if self.image is not None:
            self.image = self.imagegray
            messagebox.showinfo("Succée", "Image a bien transformeé vers le grayscale!")
        else:
            messagebox.showerror("Error", "No image Charger!")
     
    def cree_poserH(self):
        if self.image is not None:
            self.image = poserH(self.image, self.image)
            messagebox.showinfo("Succée", "Image poser horizontalement!")

        else:
            messagebox.showerror("Error", "No image Charger!")
    def cree_poserV(self):
        if self.image is not None:
            self.image = poserV(self.image, self.image)
            messagebox.showinfo("Succée", "Image poser verticalement!")
    
    def cree_inverser(self):
        if self.image is not None:
            self.image = inverser(self.image)
            messagebox.showinfo("Succée", "Image est bien inverser!")
        else:
            messagebox.showerror("Error", "No image Charger!")(self.image)
            messagebox.showinfo("Succée", "Image est bien inverser!")
        

if __name__ == "__main__":
    # Crée une fenêtre principale avec Tkinter
    root = tk.Tk()
    # Crée une instance de l'application ImageApp avec la fenêtre principale
    app = ImageApp(root)
    # Démarre la boucle principale de l'interface graphique, permettant l'interaction avec l'utilisateur
    root.mainloop()


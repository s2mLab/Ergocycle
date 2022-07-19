from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * #QApplication, QMainWindow
from PyQt5.QtGui import * #QIcon, QPixmap
from PIL import Image, ImageTk
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    ### 1. Faire l'initialisation du menu principal ###

    ### 1.1. Instaurer la taille, la couleur de fond et le titre du menu principal ###
    win.setGeometry(100, 100, 1400, 850)
    win.setWindowTitle("Menu principal des stimulations électriques fonctionnelles avec PyQt5")
    win.setStyleSheet("background-color: white;")

    ### 1.2. Mettre le logo du laboratoire dans le coin gauche de la fenêtre ###
    imageS2M = Image.open("img_S2M_JPG.jpg")
    petite_imageS2M = imageS2M.resize((200, 150))
    petite_imageS2M.save('image_400.jpg')
    label_logo = QtWidgets.QLabel(win)
    logo_jpg = QPixmap('image_400.jpg')
    label_logo.setPixmap(logo_jpg)
    label_logo.resize(200, 150)

    ### 1.3. Titre du menu principal ###
    label_title = QtWidgets.QLabel(win)
    label_title.setText("Bienvenue au menu principal de l'interface usager des stimulations électriques fonctionnelles")
    label_title.setFont(QFont("Calibri", 16))
    label_title.adjustSize() 
    label_title.move(210,75)
    
    ### 1.3. Temps d'entraînement ###
    label_tt = QtWidgets.QLabel(win)
    label_tt.setText("Durée de l'entraînement (min):")
    label_tt.setFont(QFont("Calibri", 10))
    label_tt.adjustSize() 
    label_tt.move(10,160)



    win.show()
    sys.exit(app.exec_())
window()
#Imports
from tkinter import *
from tkinter.ttk import *
import os
from makeGraph import loadGraphe
from graphePondere import Graphe_D
from dijkstra import getPath
import csv
import geopy
from geopy.geocoders import Nominatim
from adresse import adresse_
import folium
from Map import Map_
from math import sqrt
from geopy.distance import geodesic
import webview

#Prompts

#--------------------------------------------------------------------------
#_tkinter.TclError: failed to create an iconphoto with image "homepage.png"

# import os
# 
# # Chemin absolu basé sur l'emplacement du script
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# self.photo = PhotoImage(file=os.path.join(BASE_DIR, "homepage.png"))
#--------------------------------------------------------------------------

class UI:
    def __init__(self):
                
        #Architecture de la fenetre
        
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        
        self.fenetre = Tk()
        self.cadre = Frame(self.fenetre)
        self.cadre.grid()
        self.fenetre.title("Home_Page")
        self.photo = PhotoImage(file=os.path.join(BASE_DIR, "homepage.ico"))
        self.logo = self.fenetre.iconphoto(False, self.photo)                               # Applies on each page ? ; photo
        
        self.fenetre.geometry('300x250')
        
        ##########################
        
        #Entrées
        
        self.start = StringVar()
        self.depart = Entry(self.cadre, textvariable = self.start)
        self.depart.grid(row=0, column=0, sticky="w")
        self.depart.insert(0, "Départ") #index ; str
        
        self.end = StringVar()
        self.fin = Entry(self.cadre, textvariable = self.end)
        self.fin.grid(row=1, column=0, sticky="w")
        self.fin.insert(0, "Arrivée") #index ; str
        
        ########
        
        # Bouton
        self.send = Button(self.cadre, command=lambda:self.DisplayPath(self.depart.get(), self.fin.get())) # La doc tkinter n'est pas à jour
        self.send.grid(row = 2, column=0, sticky="w")
        
        #
        self.GestionAdresses = adresse_()
        
        #
        self.rows = 0
        self.cols = 1
        
        #Map
        self.map = Map_()
        
    def Display(self):
        self.fenetre.mainloop()
        
    def DisplayPath(self, dep, arr):
        pa = getPath(loadGraphe("arrets.csv"), dep, arr)
        chemin = pa[1]
        self.path = Label(text=str(chemin), justify=LEFT)
        self.rows += 1
        self.path.grid(row=self.rows, column=self.cols, sticky="w")

        ListeChemins = []
        for arrets in chemin:
            try:
                Che = self.Convert(arrets)
                self.path2 = Label(text=str(Che), justify=LEFT)
                self.rows += 1
                self.path2.grid(row=self.rows, column=self.cols, sticky="w")
                print(Che, type(Che))
                self.map.PlaceMarker([Che[1], Che[2]], str(Che[0]))
                ListeChemins.append((Che[1], Che[2]))
            except:
                pass
        self.map.Trait(ListeChemins)
        prec = None
        dist = 0
        for coos in self.map.trail_coordinates:
            if prec == None:
                prec = coos
            else:
                dist += geodesic(prec, coos).km                                             # Les docs du module
                prec = coos
        self.distance = Label(text=str(dist), justify=LEFT)
        self.rows += 1
        self.distance.grid(row=self.rows, column=self.cols, sticky="w")
        self.map.MAJ()
        self.MapWindow()
        
    def Convert(self, arret):
        self.GestionAdresses.get_loc(arret)
        return self.GestionAdresses.afficher()
    
    def MapWindow(self):
        window = webview.create_window('Map', os.path.abspath('index.html'))                # Docs du module
        webview.start()
Main = UI(); Main.Display()
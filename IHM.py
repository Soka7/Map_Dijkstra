#Imports
from tkinter import *
from tkinter.ttk import *
import os
from makeGraph import loadGraphe
from graphePondere import Graphe_D
from dijkstra import getPath
import csv

#Traceback (most recent call last):
#  File "d:\Map_Dijkstra\IHM.py", line 18, in <module>
#    Main = UI(); Main.Display()
#           ^^^^
#  File "d:\Map_Dijkstra\IHM.py", line 13, in __init__
#    self.Logo = self.fenetre.iconphoto(True, self.photo)
#                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#  File "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.2544.0_x64__qbz5n2kfra8p0\Lib\tkinter\__init__.py", line 2200, in wm_iconphoto
#    self.tk.call('wm', 'iconphoto', self._w, "-default", *args)
#_tkinter.TclError: failed to create an iconphoto with image "homepage.png"

# import os
# 
# # Chemin absolu basé sur l'emplacement du script
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# self.photo = PhotoImage(file=os.path.join(BASE_DIR, "homepage.png"))

class UI:
    def __init__(self):
                
        #Architecture de la fenetre
        
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        
        self.fenetre = Tk()
        self.cadre = Frame(self.fenetre)
        self.cadre.grid()
        self.fenetre.title("Home_Page")
        self.photo = PhotoImage(file=os.path.join(BASE_DIR, "homepage.ico"))
        self.logo = self.fenetre.iconphoto(False, self.photo) # Applies on each page ? ; photo
        
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
        
        self.send = Button(self.cadre, command=lambda:self.DisplayPath(self.depart.get(), self.fin.get()))
        self.send.grid(row = 2, column=0, sticky="w")
        
    def Display(self):
        self.fenetre.mainloop()
        
    def DisplayPath(self, dep, arr):
        self.path = Label(text=str(getPath(loadGraphe("arrets.csv"), dep, arr)))
        self.path.grid(row=1, column=1, sticky="w")

Main = UI(); Main.Display()
import folium                                                                       #https://python-visualization.github.io/folium/latest/getting_started.html

class Map_:
    def __init__(self):
        self.m = folium.Map(location=(47.2, -1.54), zoom_start=8)
        self.trail_coordinates = []
        
    def PlaceMarker(self, locs: list, Titre: str, Couleur: str):
        """
        Docstring pour PlaceMarker
        
        :type locs: list
        :type Titre: str
        :type Couleur: str

        return None
        """
        folium.Marker(
            location = locs,
            tooltip="Click me!",
            popup=Titre,
            icon=folium.Icon(color=Couleur),
        ).add_to(self.m)

        return None
        
    def Trait(self, coos: list):
        """
        Faire un trait sur la map entre 2 points
        :type coos: list

        return None
        """
        self.trail_coordinates = coos
        folium.PolyLine(self.trail_coordinates, tooltip="Road").add_to(self.m)

        return None

    def MAJ(self):
        """
        Enregistrer la nouvelle version de la page HTML

        return None
        """
        self.m.save("index.html")

        return None
import folium

class Map_:
    def __init__(self):
        self.m = folium.Map(location=(47, -1.5), zoom_start=14)
        self.trail_coordinates = []
        
    def PlaceMarker(self, locs: list, Titre: str):
        folium.Marker(
            location = locs,
            tooltip="Click me!",
            popup=Titre,
            icon=folium.Icon(color="green"),
        ).add_to(self.m)
        
    def Trait(self, coos: list):
        self.trail_coordinates = coos
        folium.PolyLine(self.trail_coordinates, tooltip="Road").add_to(self.m)

    def MAJ(self):
        self.m.save("index.html")
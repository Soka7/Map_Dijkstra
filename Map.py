import folium

class Map_:
    def __init__(self):
        self.m = folium.Map(location=(47, -1.5))
        
    def PlaceMarker(self, locs: list, Titre: str):
        folium.Marker(
            location = locs,
            tooltip="Click me!",
            popup=Titre,
            icon=folium.Icon(color="green"),
        ).add_to(self.m)

    def MAJ(self):
        self.m.save("index.html")
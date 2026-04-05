import geopy
from geopy.geocoders import Nominatim
class adresse_:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="my_geocoder")
        
    def get_loc(self, arret):
        self.location = self.geolocator.geocode(f"{arret}, Pays de la Loire, France")

    def afficher(self):
        assert self.location, 'No location provided'
        return(f"Adresse: {self.location.address} Latitude: {self.location.latitude} Longitude: {self.location.longitude}")
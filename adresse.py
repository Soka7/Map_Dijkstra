import geopy
from geopy.geocoders import Nominatim
class adresse_:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="my_geocoder")
        
    def get_loc(self, arret):
        self.location = self.geolocator.geocode(f"{arret}, Pays de la Loire, France")

    def afficher(self):
        assert self.location, 'No location provided'
        return((self.location.address, self.location.latitude, self.location.longitude))
import geopy
from geopy.geocoders import Nominatim
 
# Création d'un objet géocodeur Nominatim
geolocator = Nominatim(user_agent="my_geocoder")
 
# Géocodage d'une adresse
location = geolocator.geocode("Bac, Pays de la Loire, France")
 
# Affichage des informations de localisation
print(f"Adresse: {location.address} Latitude: {location.latitude} Longitude: {location.latitude}")
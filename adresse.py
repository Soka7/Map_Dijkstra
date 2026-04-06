import geopy
from geopy.geocoders import Nominatim

class Adress:
    def __init__(self) -> None:
        """
        Create an adress object.\n
        :return: None
        """
        self.GeoLocator : Nominatim = Nominatim(user_agent = "my_geocoder")
        self.Location = None
        return None
        
    def SetLocation(self, Stop : str) -> None:
        """
        Store the location of a wanted Stop.

        :param Stop: The stop you want to store location of
        :type Stop: str

        :return: None
        """
        self.Location = self.GeoLocator.geocode(f"{Stop}, Pays de la Loire, France")
        return None

    def Show(self) -> tuple:
        """
        Give the adress, latitude and longitude of the stored location.

        :return: Adress, Latitude, Longitude of the stored location 
        :rtype: 3-uplet
        """
        assert self.Location, 'You need to provide a location first.'
        Data : tuple = ((self.Location.address, self.Location.latitude, self.Location.longitude))
        return Data
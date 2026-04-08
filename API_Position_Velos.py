import requests
import csv

class Positions:
    def __init__(self):
        self.ListeCoos = []
    
    def HttpRequest(self):
        # <Response [200]>: Success
        Reponse = requests.get("https://data.nantesmetropole.fr/api/explore/v2.1/catalog/datasets/244400404_stations-velos-libre-service-nantes-metropole/records")
        print(Reponse)
        Decoded = Reponse.json()
        for key, value in Decoded.items():
            print(key, ":", value)
            if key == "results":
                for element in value:
                    print(element, "\n\n")
                    self.ListeCoos.append(element['geo_point_2d'])
        return(self.ListeCoos)
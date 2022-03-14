import urllib.request
import json

class Donnee_ISS:
    def __init__(self):
        self.__urlData = "http://api.open-notify.org/iss-now.json"
        self.__latitude = 0
        self.__longitude = 0

    def lectureDonnees(self):
        position = urllib.request.urlopen(self.__urlData).read().decode('utf-8')
        positionJson = json.loads(position)
        self.__longitude = positionJson["iss_position"]["longitude"]
        self.__latitude = positionJson["iss_position"]["latitude"]

    @property
    def latitude(self):
        return self.__latitude

    @property
    def longitude(self):
        return self.__longitude


if __name__ == "__main__":
    pISS = Donnee_ISS()
    pISS.lectureDonnees()
    print(pISS.latitude, pISS.longitude)
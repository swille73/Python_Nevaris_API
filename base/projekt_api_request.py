import requests
import nevaris_api_base as nb
from nevaris_class import Projekt
from speicherort_api_request import get_speicherorte

# Projekt Objekt erstellen
def create_projekt(projektInfo):
    try:
        bez = nb.get_value(projektInfo, "bezeichnung")
        nr = nb.get_value(projektInfo, "nummer")
        id = projektInfo["id"]

        return Projekt(id=id, nummer=nr, bezeichnung=bez)
    except Exception as ex:
        print(f"Error: {ex}")    

# Ermitteln der Projekt anhand der übergenen Datenbank.
def get_projektInfos(speicherort):
    try:
        #Projekte in der übergebenen Datenhaltung ermitteln    
        speicherort_url = f"{nb.base_url}/build/global/speicherorte/{speicherort.Id}"
        print(speicherort_url)
        response = requests.get(speicherort_url)
        print(response.status_code, response.reason)
        data_json = response.json()  

        if "projektInfos" in data_json:             
            # Projektinfos lesen und ausgeben
            projektInfos = data_json["projektInfos"]            
            print(f"Anzahl der Projekte: {len(projektInfos)} --> Speicherort: [{speicherort}]")
            Projekte = []
            for prj in projektInfos:
                projekt = create_projekt(prj)
                Projekte.append(projekt)
                print(f"    {projekt}")

            return Projekte
        else:
            print("Keine Projekte vorhanden.")
    except Exception as e:
        print(f"Error: {e.args}")

def runmain():
    Speicherorte = get_speicherorte()
    Projekte = {}
    for speicherort in Speicherorte:
        _projekte = get_projektInfos(speicherort)
        Projekte[speicherort.Id] = _projekte

    print("")
    newdict = {key: len(value) for key, value in Projekte.items()}
    summe = sum(list(newdict.values()))
    print(f"Anzahl aller Projekte in meiner Datenhaltung: {summe}")

if __name__ == "__main__":
    runmain()


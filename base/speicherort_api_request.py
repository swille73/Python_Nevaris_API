import requests
import nevaris_api_base as nb
from nevaris_class import Speicherort, SpeicherortArt

# Speichort Objekt erstellen
def create_speicherort(speicherorte_data):
    try:        
        speicherort = ()
        # Speicherort überprüfen auf Typ
        if "datenbankInfo" in speicherorte_data:
            server = nb.get_value(speicherorte_data["datenbankInfo"], "server")
            db = nb.get_value(speicherorte_data["datenbankInfo"], "datenbank")
            speicherort = (SpeicherortArt.DATABASE, server, db)
        elif "ordnerInfo" in speicherorte_data:
            pfad = nb.get_value(speicherorte_data["ordnerInfo"], "pfad")
            speicherort = (SpeicherortArt.ORDNER, pfad)            

        bez = nb.get_value(speicherorte_data, "bezeichnung")
        id = speicherorte_data["id"]

        return Speicherort(id=id, bezeichnung=bez, info=speicherort)
    except Exception as e:
        print(f"Error: {e}")

# Speicherorte ermitteln
def get_speicherorte():
    try:
        speicherorte = f"{nb.base_url}/build/global/speicherorte"
        response = requests.get(speicherorte)
        print(response.status_code, response.reason)
        speicherorte_data = response.json()
        print("Verfügbare Speicherorte:")

        if speicherorte_data:
            list = []
            for sp in speicherorte_data:
                speicherort = create_speicherort(sp)
                list.append(speicherort)     
                print(f"    {speicherort}")

            return list
        else:
            print("Keine Speicherorte vorhanden.")
    except Exception as e:
        print(f"Error: {e}")

def runmain():
    Speicherorte = get_speicherorte()

if __name__ == "__main__":
    runmain()

from enum import Enum

class SpeicherortArt(Enum):
    ORDNER = 1
    DATABASE = 2

class Projekt:
    Nummer: str
    Bezeichnung: str
    Summe:float
    Id: str

    def __init__(self, id, nummer, bezeichnung, summe=None):
        self.Bezeichnung = bezeichnung
        self.Nummer = nummer
        self.Summe = summe
        self.Id = id
    
    # String Repräsentation bei. z.B. print()
    def __str__(self):
        return f"{self.Nummer} - {self.Bezeichnung}: {self.Summe}"

    # String Repräsentation bei z.B. interativen Interpreter, debugging
    def __repr__(self): 
        return f"{self.Id} {self.Nummer} {self.Bezeichnung} {self.Summe}"

class Speicherort:
    Bezeichnung: str
    Id: str
    SpeicherortInfo: tuple

    def __init__(self, id, bezeichnung, info):
        self.Bezeichnung = bezeichnung
        self.Id = id
        self.SpeicherortInfo = info

    # String Repräsentation bei z.B. interativen Interpreter, debugging
    def __repr__(self):
        return f"{self.Id} {self.Bezeichnung} {self.SpeicherortInfo}"
    
    # String Repräsentation bei. z.B. print()
    def __str__(self):
        info = self.SpeicherortInfo
        if info[0] is SpeicherortArt.DATABASE:
            info = f"{info[1]}@{info[2]}"
        else:
            info = f"{info[1]}"
        return f"{self.Bezeichnung} --> {info}"
    
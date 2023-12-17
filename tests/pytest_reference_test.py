'''
pytest Module zum Testen von Python Code.
Installieren mit:
    pip install -U pytest

Prüfen der Version:
    pytest --version

Es werden rekursiv in einem Verzeichnis alle Dateien gefunden die am Anfang oder am Ende
das Schlüsselwort 'test' im Dateinamen stehen haben. Plural 'tests' wird nicht gefunden.

Mit den Befehlen können die Tests dann über die Console ausgeführt werden.
    'pytest' --> Dabei werden die Tests in einem Protokoll angezeigt.
    'pytest -q' --> Führt Tests aus und zeigt lediglich wieviele durchgelaufen bzw. nicht durchgelaufen sind. 
'''

# Weitere Infos und Beschreibungen zum 'pytest' Module unter: https://docs.pytest.org/en/7.4.x/

import pytest

# Tests können in Methoden sein.
def test_zero():
    y = "test"
    assert "e" in y

'''
Tests können aber auch in Klassen gruppiert werden.
Wichtig ist dass die Klasse mit 'TestClass' beginnt 
und die Methoden dann das self Schlüsselwort übergeben bekommen.
'''
class TestClass_Myfirsttest:
    def test_one(self):
        x = "this"
        assert "h" in x
    

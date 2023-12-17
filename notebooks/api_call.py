import sys
sys.path.append('C:\\Users\\wist\\Documents\\Python\\NevarisApi\\base')

from projekt_api_request import get_projektInfos, get_speicherorte

speicherorte = get_speicherorte()

for i in speicherorte:
    projekte = get_projektInfos(i)
    print(i)
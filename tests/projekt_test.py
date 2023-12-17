import sys
import requests
import pytest
sys.path.append('C:\\Users\\wist\\Documents\\Python\\NevarisAPI\\Python_Nevaris_API\\base')
import nevaris_api_base as nb

class Projekt_Call:

    def test_connection(self):
        try:
            response=requests.get(nb.base_url)           
            assert response.status_code == 200
            assert response.reason == "OK"

            if not response.text:
                pytest.fail(reason="response from has no data")
        except Exception as ex:
            pytest.fail(reason="response from url failed")
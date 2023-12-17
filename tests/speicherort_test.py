import sys
import pytest
import requests
sys.path.append('C:\\Users\\wist\\Documents\\Python\\NevarisAPI\\Python_Nevaris_API\\base')
import nevaris_api_base as nb

class TestClass_Speichort:

    def test_baseurl(self):
        try:
            speicherorte = f"{nb.base_url}/build/global/speicherorte"
            response = requests.get(speicherorte)
            assert response.status_code == 200
            assert response.reason == "OK"

            if not response.text:
                pytest.fail(reason="response from has no data")
        except Exception as ex:
            pytest.fail(reason="response from url failed")
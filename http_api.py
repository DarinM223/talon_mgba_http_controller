from mgba_api import MGBA_API, Key
import requests


class HTTP_API(MGBA_API):
    """
    Controls mGBA by sending HTTP requests to the server running
    [mGBA-http](https://github.com/nikouu/mGBA-http).
    """

    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def add_key(self, key: Key) -> None:
        response = requests.post(f"{self.endpoint}/core/addkey?key={key.value}")
        assert response.status_code == 200

    def add_keys(self, bitmask: int) -> None:
        response = requests.post(f"{self.endpoint}/core/addkeys?keyBitmask={bitmask}")
        assert response.status_code == 200

    def clear_key(self, key: Key) -> None:
        response = requests.post(f"{self.endpoint}/core/clearkey?key={key.value}")
        assert response.status_code == 200

    def clear_keys(self, bitmask: int) -> None:
        response = requests.post(f"{self.endpoint}/core/clearkeys?keyBitmask={bitmask}")
        assert response.status_code == 200

    def tap(self, key: Key) -> None:
        response = requests.post(
            f"{self.endpoint}/mgba-http/button/tap?button={str(key)}"
        )
        assert response.status_code == 200

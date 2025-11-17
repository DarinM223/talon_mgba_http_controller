import logging
from mgba_api import MGBA_API, Key
from requests.adapters import Retry, HTTPAdapter
from requests.sessions import Session

logger = logging.getLogger(__name__)


class HTTP_API(MGBA_API):
    """
    Controls mGBA by sending HTTP requests to the server running
    [mGBA-http](https://github.com/nikouu/mGBA-http).
    """

    def __init__(self, endpoint: str):
        self.endpoint = endpoint
        self.session = Session()
        retries = Retry(total=5, backoff_factor=1)
        self.session.mount("http://", HTTPAdapter(max_retries=retries))

    def add_key(self, key: Key) -> None:
        response = self.session.post(f"{self.endpoint}/core/addkey?key={key.value}")
        if response.status_code != 200:
            logger.warning(
                f"HTTP request for adding key {key} got status code {response.status_code}"
            )

    def add_keys(self, bitmask: int) -> None:
        response = self.session.post(
            f"{self.endpoint}/core/addkeys?keyBitmask={bitmask}"
        )
        if response.status_code != 200:
            logger.warning(
                f"HTTP request for adding keys {bitmask:>10b} got status code {response.status_code}"
            )

    def clear_key(self, key: Key) -> None:
        response = self.session.post(f"{self.endpoint}/core/clearkey?key={key.value}")
        if response.status_code != 200:
            logger.warning(
                f"HTTP request for clearing key {key} got status code {response.status_code}"
            )

    def clear_keys(self, bitmask: int) -> None:
        response = self.session.post(
            f"{self.endpoint}/core/clearkeys?keyBitmask={bitmask}"
        )
        if response.status_code != 200:
            logger.warning(
                f"HTTP request for clearing keys {bitmask:>010b} got status code {response.status_code}"
            )

    def tap(self, key: Key) -> None:
        response = self.session.post(
            f"{self.endpoint}/mgba-http/button/tap?button={str(key)}"
        )
        if response.status_code != 200:
            logger.warning(
                f"HTTP request for tapping key {key} got status code {response.status_code}"
            )

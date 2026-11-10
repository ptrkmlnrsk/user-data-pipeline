import requests

from user_data_pipeline.data_access.exceptions import APIRequestError

# from user_data_pipeline.models.response import User


class JSONPlaceholderClient:
    # rozważyć wstrzykniecie sesji do inita
    def __init__(
        self,
        base_url: str,
        timeout: float = 10.0,
        session: requests.Session | None = None,
    ):
        self.base_url = base_url
        self.timeout = timeout
        self.session = session or requests.Session()  # jeśli nie poda to zrobi sesje

    def _get(self, endpoint: str) -> list[dict]:
        "HTTP request, timeout, status, JSON"
        # is shared by other get methods

        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()

        except requests.exceptions.Timeout as exc:
            raise RuntimeError(f"Request to {url} timed out") from exc

        except requests.exceptions.ConnectionError as exc:
            raise RuntimeError(f"Connection failed for {url}") from exc

        except requests.exceptions.HTTPError as exc:
            raise APIRequestError(f"HTTP request failed for {url}") from exc

        # except requests.exceptions.RequestException as exc:
        #     raise APIRequestError(f"Failed to fetch {url}") from exc

        fetched_data = response.json()

        # zwrócić na tym etapie pydantic
        # modele często powstają jako pierwsze po rozmowach z zespołem dostarczającym API

        return fetched_data

    def get_users(self) -> list[dict]:
        return self._get("/users")

    def get_posts(self) -> list[dict]:
        return self._get("/posts")

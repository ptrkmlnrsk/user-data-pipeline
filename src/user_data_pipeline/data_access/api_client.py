import requests

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

        response = self.session.get(url, timeout=self.timeout)
        response.raise_for_status()

        fetched_data = response.json()

        # zwrócić na tym etapie pydantic
        # modele często powstają jako pierwsze po rozmowach z zespołem dostarczającym API
        if not isinstance(fetched_data, list):
            raise TypeError("Expected a list of dictionaries")

        if not all(isinstance(item, dict) for item in fetched_data):
            raise TypeError("Expected list of dictionaries")

        return fetched_data

    def get_users(self) -> list[dict]:
        return self._get("/users")

    def get_posts(self) -> list[dict]:
        return self._get("/posts")

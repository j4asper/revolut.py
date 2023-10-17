from .models import Environment


class Client:
    def __init__(self, secret_key: str, environment: Environment = Environment.PRODUCTION):
        self._secret_key = secret_key
        self._environment = environment
        self._api_version = "2023-09-01"
        self._base_url = f"https://{environment.value}.revolut.com/api/"
        self._headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Revolut-Api-Version": self._api_version,
            "Authorization": f"Bearer {secret_key}"
        }

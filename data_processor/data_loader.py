import json
from typing import Any, Dict

from requests import get


def generate_params(**kwargs) -> Dict[str, Any]:
    return dict(kwargs)


def fetch_data_from_api(url: str, params: Dict[str, Any]) -> str:
    response = get(url, params=params)
    response.raise_for_status()
    return response.text


def fetch_multiple_pages_kmdb(url: str, params: Dict[str, Any]) -> Dict[str, Any]:
    response = fetch_data_from_api(url, params)
    return json.loads(response)

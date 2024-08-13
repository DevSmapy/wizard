from .spark_session import get_spark_session
from pyspark.sql import DataFrame
from requests import get
from typing import Any, Dict


def generate_params(**kwargs) -> Dict[str, Any]:
    params = {}
    params.update(kwargs)
    return params


def str2dict(data: str) -> Dict[str, Any]:
    return eval(data)


def fetch_data_from_api(url: str, params: Dict[str, Any]) -> str:
    response = get(url, params=params)
    if response.status_code == 200:
        return response.text


def fetch_multiple_pages_kmdb(url: str, params: Dict[str, Any]) -> Dict[str, Any]:
    response = fetch_data_from_api(url, params)
    data = str2dict(response)
    return data


def load_data(parquet_path: str) -> DataFrame:
    spark = get_spark_session()
    return spark.read.parquet(parquet_path)

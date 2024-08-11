from .spark_session import get_spark_session

def load_data(parquet_path: str):
    spark = get_spark_session()
    return spark.read.parquet(parquet_path)
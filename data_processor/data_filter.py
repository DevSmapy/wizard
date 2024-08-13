from datetime import datetime, timedelta
from typing import Any, Dict, List
from pyspark.sql import DataFrame


def filter_weekly_release(df: DataFrame, date_format: str) -> DataFrame:
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    start_of_week_str = start_of_week.strftime(date_format)
    end_of_week_str = end_of_week.strftime(date_format)

    df_filtered = df.filter(
        (df["openDt"] >= start_of_week_str) & (df["openDt"] <= end_of_week_str)
    )

    return df_filtered


def extract_movie_details(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    if not data:
        return []

    movie_details = []
    results = data.get("Data", [{}])[0].get("Result", [])

    for result in results:
        movie = {
            "title": result.get("title", ""),
            "release_date": result.get("repRlsDate", ""),
            "genre": result.get("genre", ""),
            "directors": [
                director["directorNm"]
                for director in result.get("directors", {}).get("director", [])
            ],
            "actors": [
                actor["actorNm"] for actor in result.get("actors", {}).get("actor", [])
            ],
            "plots": [
                plot["plotText"] for plot in result.get("plots", {}).get("plot", [])
            ],
            "posters": result.get("posters", ""),
        }
        movie_details.append(movie)

    return movie_details

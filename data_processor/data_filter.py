from typing import Any, Dict, List


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

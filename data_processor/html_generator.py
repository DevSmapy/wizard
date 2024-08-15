from typing import List, Dict
from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"

def load_template(template_path: str) -> str:
    with open(template_path, "r", encoding="utf-8") as template_file:
        return template_file.read()

def make_movie_card(movie_id: str, movie: Dict[str, str], template: str) -> str:
    release_date = datetime.strptime(movie["release_date"], "%Y%m%d").strftime(DATE_FORMAT)
    return template.format(
        content_id=movie_id,
        poster_url=movie["posters"].split("|")[0],
        title=movie["title"],
        release_date=release_date,
        genre=movie["genre"],
        directors=", ".join(movie["directors"]),
        cast=", ".join(movie["actors"]),
        synopsis=''.join(movie["plots"]),
    )

def make_index_block(movie_id: str, movie: Dict[str, str], template: str) -> str:
    release_date = datetime.strptime(movie["release_date"], "%Y%m%d").strftime(DATE_FORMAT)
    return template.format(
        content_id=movie_id,
        title=movie["title"],
        poster_url=movie["posters"].split("|")[0],
        release_date=release_date,
        genre=movie["genre"],
    )

def generate_html(template_path: str, data: List[Dict[str, str]]) -> str:
    movie_card = load_template(template_path+"movie_card.html")
    top_index = load_template(template_path+"top_index.html")
    index_blocks = []
    movie_blocks = []

    for idx, movie in enumerate(data):
        print(movie["title"])
        movie_id = f"movie{idx + 1}"
        movie_block = make_movie_card(movie_id, movie, movie_card)
        index_block = make_index_block(movie_id, movie, top_index)
        movie_blocks.append(movie_block)
        index_blocks.append(index_block)

    complete_index = "\n".join(index_blocks)
    complete_mcards = "\n".join(movie_blocks)

    return complete_index, complete_mcards
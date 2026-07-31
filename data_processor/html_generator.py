from datetime import datetime
from typing import Dict, List

DATE_FORMAT = "%Y-%m-%d"

PAGE_HEADER = """\
<div style="max-width: 600px; margin: auto; padding: 10px; font-family: 'Nunito', sans-serif;">
<div style="text-align: center; margin-bottom: 20px;">
<p style="font-size: 24px; font-weight: bold; color: #333;" data-ke-size="size16">주간 개봉 영화</p>
</div>
<div style="margin-bottom: 20px; border: 2px solid #ccc; border-radius: 10px; padding: 15px; background-color: #f9f9f9;">
<p style="font-size: 18px; font-weight: bold; color: #007bff;" data-ke-size="size16">목차</p>
"""


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
        synopsis="".join(movie["plots"]),
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
    movie_card = load_template(template_path + "movie_card.html")
    top_index = load_template(template_path + "top_index.html")
    index_blocks = []
    movie_blocks = []

    for idx, movie in enumerate(data):
        print(movie["title"])
        movie_id = f"movie{idx + 1}"
        movie_blocks.append(make_movie_card(movie_id, movie, movie_card))
        index_blocks.append(make_index_block(movie_id, movie, top_index))

    index_body = "\n".join(index_blocks)
    mcards = "\n".join(movie_blocks)
    return f"{PAGE_HEADER}{index_body}</div>{mcards}</div>"

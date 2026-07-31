import json

from data_processor import (
    extract_movie_details,
    fetch_multiple_pages_kmdb,
    generate_html,
)


def main() -> None:
    with open("config.json", encoding="utf-8") as config_file:
        config = json.load(config_file)

    data = fetch_multiple_pages_kmdb(config["api_url"], params=config["params"])
    movie_details = extract_movie_details(data)
    html = generate_html("templates/", movie_details)

    output_path = config["output_path"]
    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(html)

    print(f"Weekly report written to {output_path}")


if __name__ == "__main__":
    main()

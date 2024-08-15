import json
from data_processor import (
    load_data,
    filter_weekly_release,
    summarize_release,
    fetch_multiple_pages_kmdb,
    extract_movie_details,
    generate_html,
)


def main():
    with open("config.json") as config_file:
        config = json.load(config_file)

    parquet_path = config["parquet_path"]
    data_format = config["data_format"]
    output_path = config["output_path"]

    df = load_data(parquet_path)
    df_filtered = filter_weekly_release(df, data_format)
    summaries = summarize_release(df_filtered)

    print(summaries)

    with open(output_path, "w") as output_file:
        for row in summaries:
            output_file.write(f"{row}\n")

    print(f"Summaries written to {output_path}")


def main_kmdb():
    with open("config.json") as config_file:
        config = json.load(config_file)

    api_url = config["api_url"]
    params = config["params"]
    output_path = config["output_path"]

    data = fetch_multiple_pages_kmdb(api_url, params=params)
    movie_details = extract_movie_details(data)
    index_body, mcards = generate_html("templates/", movie_details)

    with open("Aug3rd.html", "w") as output_file:
        output_file.write(
            """
            <div style="max-width: 600px; margin: auto; padding: 10px; font-family: 'Nunito', sans-serif;">
<div style="text-align: center; margin-bottom: 20px;">
<p style="font-size: 24px; font-weight: bold; color: #333;" data-ke-size="size16">주간 개봉 영화</p>
</div>
<div style="margin-bottom: 20px; border: 2px solid #ccc; border-radius: 10px; padding: 15px; background-color: #f9f9f9;">
<p style="font-size: 18px; font-weight: bold; color: #007bff;" data-ke-size="size16">목차</p>
            """
        )
        output_file.write(index_body)
        output_file.write("</div>")
        output_file.write(mcards)

if __name__ == "__main__":
    main_kmdb()

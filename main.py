import json
from data_processor import load_data, filter_weekly_release, summarize_release

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

if __name__ == "__main__":
    main()
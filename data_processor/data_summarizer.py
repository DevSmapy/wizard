def summarize_release(df):
    return df.select("movieNm", "openDt", "prdtYear", "repGenreNm").collect()
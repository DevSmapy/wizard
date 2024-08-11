from datetime import datetime, timedelta

def filter_weekly_release(df, date_format):
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    start_of_week_str = start_of_week.strftime(date_format)
    end_of_week_str = end_of_week.strftime(date_format)

    df_filtered = df.filter(
        (df["openDt"] >= start_of_week_str) &
        (df["openDt"] <= end_of_week_str)
    )

    return df_filtered
def add_temperature_features(df):
    temp_sensors = ["sensor_2", "sensor_3", "sensor_4", "sensor_11"]

    # Average temperature
    df["avg_temp"] = df[temp_sensors].mean(axis=1)

    # Lag features (t-1)
    for col in temp_sensors + ["avg_temp"]:
        df[f"{col}_lag1"] = df.groupby("engine_id")[col].shift(1)

    # Remove NaNs from first cycle
    df = df.dropna().reset_index(drop=True)

    return df

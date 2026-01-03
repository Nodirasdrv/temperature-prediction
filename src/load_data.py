import pandas as pd

def load_cmapss_data(path):
    cols = (
        ["engine_id", "cycle"] +
        [f"os_{i}" for i in range(1, 4)] +
        [f"sensor_{i}" for i in range(1, 22)]
    )

    df = pd.read_csv(
        path,
        sep=r"\s+",
        header=None,
        names=cols
    )

    return df


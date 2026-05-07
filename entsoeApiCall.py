import os
import pandas as pd
from entsoe import EntsoePandasClient

client = EntsoePandasClient(api_key='YOUR API KEY')

start = pd.Timestamp("20240101", tz="Europe/Zurich")
end   = pd.Timestamp("20260101", tz="Europe/Zurich")

os.makedirs("data", exist_ok=True)

neighbors = ["AT", "DE_AT_LU", "DE_LU", "FR", "IT_NORD", "IT_NORD_CH"]

frames = []
for n in neighbors:
    print(f"Fetching CH ↔ {n}")
    try:
        imports = client.query_crossborder_flows(n, "CH", start=start, end=end)
        exports = client.query_crossborder_flows("CH", n, start=start, end=end)
        net = imports - exports
        net.name = f"net_import_{n}"
        frames.append(net)
    except Exception as e:
        print(f"  WARNING {n}: {e}")

df = pd.concat(frames, axis=1)
df["net_import_total"] = df.sum(axis=1)
df.index.name = "timestamp"
df.to_csv("data/net_import_ch_2024_2025.csv")
print(f"Saved {len(df)} rows → data/net_import_ch_2024_2025.csv")

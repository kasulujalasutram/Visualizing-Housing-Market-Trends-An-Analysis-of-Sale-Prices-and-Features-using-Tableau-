import pandas as pd
from datetime import datetime

current_year = datetime.now().year

df = pd.read_csv("../data/housing_raw.csv")

df["house_age"] = current_year - df["yr_built"]

df["renovation_status"] = df["yr_renovated"].apply(
    lambda x: "Not Renovated" if x == 0 else "Renovated"
)

df["years_since_renovation"] = df["yr_renovated"].apply(
    lambda x: None if x == 0 else current_year - x
)

df.to_csv("../data/housing_processed.csv", index=False)

print("housing_processed.csv created successfully!")

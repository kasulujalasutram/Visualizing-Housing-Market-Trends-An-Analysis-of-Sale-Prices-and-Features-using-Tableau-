import pandas as pd
import numpy as np
import random
from datetime import datetime

np.random.seed(42)

rows = 500
current_year = datetime.now().year

data = {
    "id": range(1, rows + 1),
    "price": np.random.randint(50000, 800000, rows),
    "bedrooms": np.random.randint(1, 6, rows),
    "bathrooms": np.random.randint(1, 4, rows),
    "floors": np.random.randint(1, 3, rows),
    "sqft_basement": np.random.randint(0, 1500, rows),
    "yr_built": np.random.randint(1950, 2023, rows),
    "yr_renovated": np.random.choice(
        [0] + list(range(1990, 2023)), rows
    )
}

df = pd.DataFrame(data)

df.to_csv("../data/housing_raw.csv", index=False)

print("housing_raw.csv generated successfully!")

import pandas as pd


# Load the dataframe
df = pd.read_csv('data/festivals-global-festivals-_-pl.csv', sep=';')
df = df.dropna(subset=["Géocodage xy"])
print(df.columns)

# Adds lat and lon columns from the Géocodage_xy column
df["lat"] = df["Géocodage xy"].apply(lambda x: str(x).split(",")[0])
df["lon"] = df["Géocodage xy"].apply(lambda x: str(x).split(",")[1])

print(df.head())

# Save the dataframe
df.to_csv('data/festivals-processed.csv', sep=';', index=False)
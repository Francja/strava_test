import pandas as pd

df = pd.read_csv("strava_activities.csv")

print("DataFrame Columns:", df.columns)
print(df.head())
import pandas as pd
import numpy as np

df = pd.read_csv("ncr_ride_bookings.csv", sep=",")

#column name she extra space remove kar dega or first charector ko chepital keke shabhi ko shamol kar dega
df.columns = df.columns.str.strip().str.title()

# remove duplicates all columne
df = df.drop_duplicates()

# remove all columne value extra space or first char chapital all shmall
for col in df.select_dtypes(include="str").columns:
    df[col] = df[col].str.strip().str.title()

# Avg Vtat (Avreag vating time of customer)
df["Avg Vtat"] = df["Avg Vtat"].fillna(df["Avg Vtat"].mean())

# Avg ctat (Avreag raid time of customer)
df["Avg Ctat"] = df["Avg Ctat"].fillna(df["Avg Ctat"].mean())

print(df["Cancelled Rides By Customer"].unique())

# print(df.inf)
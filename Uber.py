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

#Cancelled Rides By Customer fill nan to 0
df["Cancelled Rides By Customer"]=df["Cancelled Rides By Customer"].fillna(0)

#Reason For Cancelling By Customer
df["Reason For Cancelling By Customer"] = df["Reason For Cancelling By Customer"].fillna("Not Cancelled")

#Cancelled Rides By Driver 
df["Cancelled Rides By Driver"] = df["Cancelled Rides By Driver"].fillna(0)

# Driver Cancellation Reason
df["Driver Cancellation Reason"] = df["Driver Cancellation Reason"].fillna("Not Cancellation")

#Incomplete Rides 
df["Incomplete Rides"] = df["Incomplete Rides"].fillna(0)

#Incomplete Rides Reason
df["Incomplete Rides Reason"] = df["Incomplete Rides Reason"].fillna("Complete Rides")
#Booking Value 
df["Booking Value"] = df["Booking Value"].fillna(df["Booking Value"].median())

#Ride Distance
df["Ride Distance"] = df["Ride Distance"].fillna(df["Ride Distance"].mean())

# Driver Ratings
df["Driver Ratings"] = df["Driver Ratings"].fillna(df["Driver Ratings"].mean()).round(1)

# Customer Ratings
df["Customer Rating"] = df["Customer Rating"].fillna(df["Customer Rating"].mean()).round()

df["Payment Method"] = df["Payment Method"].fillna("No Payment")


df.to_csv("NCR_Ride_Booking_clean_Data.csv", index=False)

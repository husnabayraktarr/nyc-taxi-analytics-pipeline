import pandas as pd
import matplotlib.pyplot as plt

# Peak hours
df = pd.read_csv("peak_hours.csv")
df.columns = ["hour", "total_trips"]

plt.figure()
plt.bar(df["hour"], df["total_trips"])
plt.xlabel("Hour of Day")
plt.ylabel("Number of Trips")
plt.title("Taxi Demand by Hour")
plt.show()

# Payment type
df = pd.read_csv("payment_type.csv")
df.columns = ["payment_type", "count"]

plt.figure()
plt.pie(df["count"], labels=df["payment_type"], autopct="%1.1f%%")
plt.title("Payment Type Distribution")
plt.show()

# Distance vs fare
df = pd.read_csv("distance_fare.csv")
df.columns = ["distance", "avg_fare"]

plt.figure()
plt.plot(df["distance"], df["avg_fare"])
plt.xlabel("Distance")
plt.ylabel("Average Fare")
plt.title("Distance vs Fare")
plt.show()

# Total revenue
df = pd.read_csv("total_revenue.csv")
df.columns = ["total_revenue"]

plt.figure()
plt.bar(["Revenue"], df["total_revenue"])
plt.title("Total Revenue")
plt.ylabel("USD")
plt.show()

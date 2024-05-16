import pandas as pd
import matplotlib.pyplot as plt
Jan24 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Jan2024.csv")
Jan24.head()
Jan24.shape
Feb24 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Feb24.csv")
Feb24.head()
Feb24.shape
Dec23 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Dec23.csv")
Dec23.head()
Dec23.shape
Nov23 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Nov23.csv")
Nov23.head()
Nov23.shape
Oct23 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Oct23.csv")
Oct23.head()
Oct23.shape
Sept23 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Sept23.csv")
Sept23.head()
Sept23.shape
Aug23 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Aug23.csv")
Aug23.head()
Aug23.shape
Jul23 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\July23.csv")
Jul23.head()
Jul23.shape
Jun23 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Jun23.csv")
Jun23.head()
Jun23.shape
May23 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\May23.csv")
May23.head()
May23.shape
Apr23 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Apr23.csv")
Apr23.head()
Apr23.shape
Mar23 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Mar23.csv")
Mar23.head()
Mar23.shape
Feb23 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Feb23.csv")
Feb23.head()
Feb23.shape
Jan23 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Jan23.csv")
Jan23.head()
Jan23.shape
Dec22 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Dec22.csv")
Dec22.head()
Dec22.shape
Nov22 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Nov22.csv")
Nov22.head()
Nov22.shape
Oct22 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Oct22.csv")
Oct22.head()
Oct22.shape
Sept22 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Sept22.csv")
Sept22.head()
Sept22.shape
Aug22 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Aug22.csv")
Aug22.head()
Aug22.shape
Jul22 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Jul22.csv")
Jul22.head()
Jul22.shape
Jun22 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Jan23.csv")
Jun22.head()
Jun22.shape
May22 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\May22.csv")
May22.head()
May22.shape
Apr22 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Apr22.csv")
Apr22.head()
Apr22.shape
Mar22 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Mar22.csv")
Mar22.head()
Mar22.shape
Feb22 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Feb22.csv")
Feb22.head()
Feb22.shape
Jan22 = pd.read_csv(r"C:\Users\Kelvin\OneDrive\Documents\Flight Delays\Jan22.csv")
Jan22.head()
Jan22.shape

dfs = [Feb24,Jan24,Dec23,Nov23,Oct23,Sept23,Aug23,Jul23,Jun23,May23,Apr23,Mar23,Feb23,Jan23,Dec22,Nov22,Oct22,Sept22,Aug22,Jul22,Jun22,May22,Apr22,Mar22,Feb22,Jan22]
final_df = pd.concat(dfs, axis=0, ignore_index=True)

# Display the final DataFrame
print(final_df)
final_df.shape
final_df.info()
final_df.isna().any()
final_df.columns
#Percentage of column missing values
final_df.isna().mean() * 100
final_df.ARR_DELAY_GROUP.nunique()
final_df.ARR_DELAY_GROUP.unique()
df = final_df[["YEAR","QUARTER","MONTH","DAY_OF_MONTH","DAY_OF_WEEK","FL_DATE","TAIL_NUM","ORIGIN","DEST","CRS_DEP_TIME","DEP_TIME","DEP_DELAY","DEP_DEL15","CRS_ARR_TIME","ARR_TIME","ARR_DELAY","ARR_DEL15","WEATHER_DELAY"]]
df.shape
df.ORIGIN.nunique()
df.DEST.nunique()
df.DEST.unique()
df.DEP_DEL15.unique()
# About 18% of flights departed with delays. We will have to deal with class imbalance in the modeling process later.
# About 1.5% of flights don't have labels on delays (These are cancelled flights).
total_flight = df.count()
delayed_flight = df[df.DEP_DEL15 == 1]
on_time_flight = df[df.DEP_DEL15 == 0]
cancelled_flight = df[df.DEP_DEL15.isNull()]
print(f'Total Flight: {total_flight}')
print(f'Total Flight delayed by more than 15 minutes: {delayed_flight.count()}')
print(f'Delayed Flight: {delayed_flight.count() / total_flight }')
print(f'On Time Flight: {on_time_flight.count() / total_flight}')
print(f'Cancelled Flight: {cancelled_flight.count() / total_flight}')

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import io

plt.figure(figsize=(8, 6))
plt.imshow(df.isnull(), cmap='viridis', aspect='auto')
plt.title('Heatmap of Missing Data')
plt.xlabel('Columns')
plt.ylabel('Rows')
plt.colorbar(label='Missing Data')
plt.show()

df.MONTH.value_counts().plot.barh()
airports = ('ATL','CLT','DEN','DFW','EWR','IAH','JFK','LAS','LAX','MCO','MIA','ORD','PHX','SEA','SFO')
df = df[df["Origin"].isin(airports)]
df = df[df["Dest"].isin(airports)]

print(df.info())
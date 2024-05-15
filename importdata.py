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
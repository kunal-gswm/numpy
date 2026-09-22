import os
import yfinance as yf

os.makedirs("data",exist_ok=True)
print("Donwloading Nifty 50 data...")
df=yf.download("^NSEI",start="2023-01-01",end="2026-09-19")
path = "data/nifty.csv"
df.to_csv(path)
print(f"Successfully saved data to {path}")
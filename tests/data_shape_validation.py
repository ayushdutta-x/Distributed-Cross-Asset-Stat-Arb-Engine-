from data.downloader import download_prices
from data.validator import validate_prices

TICKERS = [
    "SPY",
    "QQQ",
    "XLF",
    "XLK",
    "XLE",
    "XLI"
]

df  = download_prices(
    start = "2015-01-01",
    end = "2025-01-01"
)

df = df[TICKERS]


'''Data Shape'''

print(df.head())
print(df.tail())
print(df.shape)
print(df.isna().sum())

'''Data Validation Check'''

validate_prices(df)
print("Data validation check complete")
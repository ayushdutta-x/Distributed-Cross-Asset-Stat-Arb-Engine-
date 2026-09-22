from data.downloader import download_prices
from econometrics.stationarity import check_i1

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


results = check_i1(df)
print("\nADF Stationarity Results")
print(results)

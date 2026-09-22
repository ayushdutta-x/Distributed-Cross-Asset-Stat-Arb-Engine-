import yfinance as yf

TICKERS = {
    "SPY",
    "QQQ",
    "XLF",
    "XLK",
    "XLE",
    "XLI"
}

def download_prices(start,end):
    data = yf.download(
        TICKERS,
        start = start,
        end = end,
        auto_adjust = False
    )
    prices = data["Adj Close"]
    return prices


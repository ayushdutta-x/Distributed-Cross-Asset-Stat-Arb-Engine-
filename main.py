from data.downloader import download_prices
from econometrics.johansen_vecm import johansen_test, get_cointegration_rank, estimate_vecm, get_pi

#==========================================
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
#===========================================

"""Run Tests for 
                Data Validation
                Stationarity
                                before proceeding"""



#### Getting the cointegration rank from the Johansen Test

johansen_result = johansen_test(df)
rank = get_cointegration_rank(johansen_result)
print(f"\nCointegration rank: {rank}")



### Estimation of alpha-beta using VECM

vecm_result = estimate_vecm(
    df,
    rank=rank
)

print("\nVECM Beta:")
print(vecm_result.beta)

print("\nVECM Alpha:")
print(vecm_result.alpha)

pi = get_pi(vecm_result)

print("\nPi Matrix:")
print(pi)


"""Augmented Dickey-Fuller Test for Stationarity of a Time Series"""

from statsmodels.tsa.stattools import adfuller


def adf_test(series):

    result = adfuller(
        series.dropna(),
        autolag="AIC",
        result_object=False
    )

    return result[1]   # return only p-value


def check_i1(df, significance=0.05):

    results = {}

    for ticker in df.columns:

        series = df[ticker]

        level_pvalue = adf_test(series)
        diff_pvalue = adf_test(series.diff())

        is_i1 = (
            level_pvalue > significance
            and diff_pvalue < significance
        )

        results[ticker] = is_i1

    return results

import numpy as np
from statsmodels.tsa.vector_ar.vecm import coint_johansen
from statsmodels.tsa.vector_ar.vecm import VECM

def johansen_test(df, det_order=0, k_ar_diff=1):
    result = coint_johansen(
        df,
        det_order=det_order,
        k_ar_diff=k_ar_diff
    )

    return result

def get_cointegration_rank(result, significance=0.05):
    critical_column = {
        0.10: 0,
        0.05: 1,
        0.01: 2
    }

    column = critical_column[significance]

    rank = 0

    for trace_stat, critical_values in zip(result.lr1, result.cvt):
        if trace_stat > critical_values[column]:
            rank += 1
        else:
            break

    return rank


def estimate_vecm(df, rank, k_ar_diff=1, deterministic="ci"):
    model = VECM(
        df,
        k_ar_diff=k_ar_diff,
        coint_rank=rank,
        deterministic=deterministic
    )

    return model.fit()


def get_pi(result):
    return result.alpha @ result.beta.T
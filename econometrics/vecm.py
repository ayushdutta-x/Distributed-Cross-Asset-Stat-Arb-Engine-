import numpy as np
from statsmodels.tsa.vector_ar.vecm import VECM


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
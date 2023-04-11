import pandas as pd
import numpy as np


chat_id = 288759659 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    from scipy.stats import ttest_1samp,t
    alpha = 0.02
    threshold = 500
    mean = np.mean(historical_data)
    std_dev = np.std(historical_data)
    t_statistic, p_value = ttest_1samp(historical_data, threshold)
    df = len(historical_data) - 1
    t_critical = np.abs(t.ppf(alpha / 2, df))
    des = t_statistic > t_critical
    return des # Ваш ответ, True или False

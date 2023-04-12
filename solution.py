import pandas as pd
import numpy as np


chat_id = 288759659 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool:
    import scipy.stats as st
    alpha = 0.02
    threshold = 500
    t_statistic, p_value = st.ttest_1samp(x, threshold, alternative='less')
    return p_value >= alpha

# Get libraries
import Orange
from Orange.data import Table
import pandas as pd
import numpy as np

# How Orange passes data to widget
df = in_data.copy()

#radiometric data
K = df[:,['K']]
eU = df[:,['eU']]
eTh = df[:,['eTh']]

lower_K = np.mean(K)/10
upper_K = np.quantile(K,0.995)

lower_eU = np.mean(eU)/10
upper_eU = np.quantile(eU,0.995)

lower_eTh = np.mean(eTh)/10
upper_eTh = np.quantile(eTh,0.995)

K = np.where((K <= lower_K),lower_K, K)
K = np.where((K >= upper_K),upper_K, K)

eU = np.where((eU <= lower_eU),lower_eU, eU)
eU = np.where((eU >= upper_eU),upper_eU, eU)

eTh = np.where((eTh <= lower_eTh),lower_eTh, eTh)
eTh = np.where((eTh >= upper_eTh),upper_eTh, eTh)

df[:,['K']] = K
df[:,['eU']] = eU
df[:,['eTh']] = eTh

out_data = Orange.data.Table(df)
# Get libraries
import Orange
import numpy as np
from Orange.data import Domain, Table

# How Orange passes data to widget
df = in_data.copy()

# Normalizing data
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

# Get table of data (X) and normalizing
norm_X = scaler.fit_transform(df.X)

#SMOTE code
from imblearn.over_sampling import SMOTE

# set variables for SMOTE
sm = SMOTE(sampling_strategy = 'auto', random_state = 15,  k_neighbors = 5, n_jobs = 1)

# get table of data (X) and class variables (y)
X, y = norm_X, df.Y

# resample data and classes
X_res, y_res = sm.fit_resample(X, y)

# Restoring original scale
inverse_X = scaler.inverse_transform(X_res)

# Get the target and feature variables
d = Domain(df.domain.attributes, df.domain.class_vars)

# Create a new Orange Table object with the appropriate headers
# This is how Orange passes the data on to the next widget
out_data = Orange.data.Table(d, inverse_X, y_res)
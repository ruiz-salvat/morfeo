#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
import numpy as np
from numpy import sqrt
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsRegressor, RadiusNeighborsRegressor
from sklearn import metrics
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import GridSearchCV
import seaborn as sns


# In[19]:


results = pd.read_csv('../../Data/ResultData/ADAUSDT_7_5_wave_trend_results.csv')
df = results[results['clean_gains'] != 0]
df = df.drop(columns = ['symbol', 'indicator', 'start_date', 'end_date', 'mean', 'n_total_partitions', 'n_partitions'])


# In[20]:


df.head()


# In[21]:


sns.pairplot(df[['ob_level', 'os_level', 'k', 'std', 'skewness', 'kurtosis', 'entropy', 'clean_gains']], diag_kind='kde')


# In[22]:


X = df[['ob_level', 'os_level', 'k', 'std', 'skewness', 'kurtosis', 'entropy']].to_numpy()
y = df['clean_gains'].to_numpy()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)


# In[59]:


model_scores = []  # List of tuples


# # MLP Regressor

# In[39]:


param_grid = {'activation': ['identity', 'logistic', 'tanh', 'relu'],
             'solver': ['lbfgs', 'sgd', 'adam'],
             'learning_rate': ['constant', 'invscaling', 'adaptive']}

model = MLPRegressor(random_state=1, max_iter=1000)

clf = GridSearchCV(model, param_grid)

clf.fit(X_train, y_train)

mlp = clf.best_estimator_

mlp_y_pred = mlp.predict(X_test)


# In[60]:


mlp_r2 = metrics.r2_score(y_test, mlp_y_pred)
model_scores.append((mlp, mlp_r2))
print(mlp_r2)


# # Gradient Boosting Regressor

# In[44]:


param_grid = {'loss': ['ls', 'lad', 'huber', 'quantile'],
             'criterion': ['friedman_mse', 'mse', 'mae'],
             'max_features': ['auto', 'sqrt', 'log2']}

model = GradientBoostingRegressor()

clf = GridSearchCV(model, param_grid)

clf.fit(X_train, y_train)

gbr = clf.best_estimator_

gbr_y_pred = gbr.predict(X_test)


# In[46]:


gbr_r2 = metrics.r2_score(y_test, gbr_y_pred)
model_scores.append((gbr, gbr_r2))
print(gbr_r2)


# # Gaussian Process Regressor

# In[55]:


param_grid = {'normalize_y': [True, False]}

model = GaussianProcessRegressor()

clf = GridSearchCV(model, param_grid)

clf.fit(X_train, y_train)

gpr = clf.best_estimator_

gpr_y_pred = gpr.predict(X_test)


# In[61]:


gpr_r2 = metrics.r2_score(y_test, gpr_y_pred)
model_scores.append((gpr, gpr_r2))
print(gpr_r2)


# # Decission Tree Regressor

# In[47]:


param_grid = {'criterion': ['mse', 'friedman_mse', 'mae'],
             'splitter': ['best', 'random'],
             'max_features': ['auto', 'sqrt', 'log2']}

model = DecisionTreeRegressor()

clf = GridSearchCV(model, param_grid)

clf.fit(X_train, y_train)

dt = clf.best_estimator_

dt_y_pred = dt.predict(X_test)


# In[63]:


dt_r2 = metrics.r2_score(y_test, dt_y_pred)
model_scores.append((dt, dt_r2))
print(dt_r2)


# # Random Forests

# In[53]:


param_grid = {'n_estimators': [75, 100, 125, 150], 
             'criterion': ['mse', 'mae']}

model = RandomForestRegressor()

clf = GridSearchCV(model, param_grid)

clf.fit(X_train, y_train)

rf = clf.best_estimator_

rf_y_pred = rf.predict(X_test)


# In[64]:


rf_r2 = metrics.r2_score(y_test, rf_y_pred)
model_scores.append((rf, rf_r2))
print(rf_r2)


# # K Neighbors Regressor

# In[56]:


param_grid = {'n_neighbors': range(2, 30)}

model = KNeighborsRegressor()

clf = GridSearchCV(model, param_grid)

clf.fit(X_train, y_train)

knr = clf.best_estimator_

knr_y_pred = knn.predict(X_test)

print(clf.best_params_)


# In[65]:


knr_r2 = metrics.r2_score(y_test, knr_y_pred)
model_scores.append((knr, knr_r2))
print(knr_r2)


# # Model Selection

# In[66]:


max_r2 = 0
best_model = None
for t in model_scores:
    if max_r2 < t[1]:
        max_r2 = t[1]
        best_model = t[0]


# In[67]:


print(best_model)


# In[68]:


print(max_r2)


# # Predicting optimal parameters

# In[69]:


# Mock parameters
std = 0.003
skewness = 0.041
kurtosis = -0.9
entropy = 9.123


# In[70]:


best_pred = 0
best_params = {'ob_level': None,
              'os_level': None,
              'k': None}

for ob_level in range(43, 63, 5):
    for os_level in range(-63, -43, 5):
        for k in np.arange(0.001, 0.030, 0.001):
            x = [[std, skewness, kurtosis, entropy, ob_level, os_level, k]]
            pred = et.predict(x)
            if pred > best_pred:
                best_pred = pred
                best_params['ob_level'] = ob_level
                best_params['os_level'] = os_level
                best_params['k'] = k


# In[71]:


best_pred


# In[72]:


best_params


# In[ ]:





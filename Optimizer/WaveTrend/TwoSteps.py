import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import timedelta
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet, SGDRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import LinearSVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.experimental import enable_halving_search_cv
from sklearn.model_selection import HalvingGridSearchCV
from sklearn.metrics import classification_report
from sklearn import metrics

results = pd.read_csv('../../Data/ResultData/wave_trend_results.csv')

df = results[results['clean_gains'] != 0]

start_date = df.iloc[0]['start_date']
start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
end_date = start_date + timedelta(days=7)
df = df[(df['start_date'] >= str(start_date)) & (df['end_date'] < str(end_date))]

while df.shape[0] > 0:

    start_date = df.iloc[0]['start_date']
    start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    end_date = start_date + timedelta(days=7)
    df = df[(df['start_date'] >= str(start_date)) & (df['end_date'] < str(end_date))]

df = df.sample(frac=1)
df = df.reset_index(drop=True)

X = df['k'].to_numpy()
y = df['clean_gains'].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)
y_train = y_train.reshape(-1, 1)
y_test = y_test.reshape(-1, 1)


# # Linear regression

# In[7]:


linear = LinearRegression()

linear.fit(X_train, y_train)

linear_y_pred = linear.predict(X_test)


# In[8]:


plt.scatter(X, y)
plt.scatter(X_test, linear_y_pred, color='r') 


# In[9]:


linear_R2 = metrics.r2_score(y_test, linear_y_pred)
print(linear_R2)


# # Ridge regression

# In[10]:


ridge = Ridge(alpha = 0.00001) # TODO: tunning

ridge.fit(X_train, y_train)

ridge_y_pred = ridge.predict(X_test)


# In[11]:


plt.scatter(X, y)
plt.scatter(X_test, ridge_y_pred, color='r')


# In[12]:


ridge_R2 = metrics.r2_score(y_test, ridge_y_pred)
print(ridge_R2)


# # Lasso regression

# In[13]:


lasso = Lasso(alpha = 0.00001) # TODO: tunning

lasso.fit(X_train, y_train)

lasso_y_pred = lasso.predict(X_test)


# In[14]:


plt.scatter(X, y)
plt.scatter(X_test, lasso_y_pred, color='r')


# In[15]:


lasso_R2 = metrics.r2_score(y_test, lasso_y_pred)
print(lasso_R2)


# # ElasticNet

# In[16]:


elastic_net = ElasticNet(alpha=0.00001, l1_ratio=0.1)

elastic_net.fit(X_train, y_train)

elastic_net_y_pred = elastic_net.predict(X_test)


# In[17]:


plt.scatter(X, y)
plt.scatter(X_test, elastic_net_y_pred, color='r')


# In[18]:


elastic_net_R2 = metrics.r2_score(y_test, elastic_net_y_pred)
print(elastic_net_R2)


# # Stochastic Gradient Descent

# In[19]:


sgd = SGDRegressor(max_iter=1000, tol=1e-3)

sgd.fit(X_train, y_train)

sgd_y_pred = sgd.predict(X_test)


# In[20]:


plt.scatter(X, y)
plt.scatter(X_test, sgd_y_pred, color='r')


# In[21]:


sgd_R2 = metrics.r2_score(y_test, sgd_y_pred)
print(sgd_R2)


# # DecisionTreeRegressor

# In[22]:


dt = DecisionTreeRegressor(random_state=0)

dt.fit(X_train, y_train)

dt_y_pred = dt.predict(X_test)


# In[23]:


plt.scatter(X, y)
plt.scatter(X_test, dt_y_pred, color='r')


# In[24]:


dt_R2 = metrics.r2_score(y_test, dt_y_pred)
print(dt_R2)


# # Linear Support Vector Regressor

# In[25]:


svr = LinearSVR(random_state=0, tol=1e-5)

svr.fit(X_train, y_train)

svr_y_pred = svr.predict(X_test)


# In[26]:


plt.scatter(X, y)
plt.scatter(X_test, svr_y_pred, color='r')


# In[27]:


svr_R2 = metrics.r2_score(y_test, svr_y_pred)
print(svr_R2)


# # KNN Regressor

# In[28]:


knn = KNeighborsRegressor(n_neighbors=2)

knn.fit(X_train, y_train)

knn_y_pred = knn.predict(X_test)


# In[29]:


plt.scatter(X, y)
plt.scatter(X_test, knn_y_pred, color = 'r')


# In[30]:


knn_R2 = metrics.r2_score(y_test, knn_y_pred)
print(knn_R2)


# # Gradient Boosting Regressor

# In[31]:


gbr = GradientBoostingRegressor(random_state=0)

gbr.fit(X_train, y_train)

gbr_y_pred = gbr.predict(X_test)


# In[32]:


plt.scatter(X, y)
plt.scatter(X_test, gbr_y_pred, color = 'r')


# In[33]:


gbr_R2 = metrics.r2_score(y_test, gbr_y_pred)
print(gbr_R2)


# # KNN hyperparameter tunning

# In[34]:


param_grid = {'n_neighbors': [2, 3, 4, 5, 6, 7, 8, 9]}

model = KNeighborsRegressor()

clf = HalvingGridSearchCV(model, param_grid, scoring='r2')
clf.fit(X_train, y_train)


# In[35]:


print("Best parameters set found on development set:")
print(clf.best_params_)


# In[ ]:





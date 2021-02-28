import pandas as pd
import numpy as np
from datetime import timedelta
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, SGDRegressor, ARDRegression, BayesianRidge
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR, NuSVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
from sklearn import metrics

results = pd.read_csv('../Data/ResultData/ADAUSDT_7_5_wave_trend_results.csv')
results = results[results['clean_gains'] != 0]
final_df = pd.DataFrame(columns=['mean', 'std', 'skewness',	'kurtosis',	'entropy', 'ob_level', 'os_level', 'k',
                                 'clean_gains', 'r2'])

start_date = results.iloc[0]['start_date']
start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
end_date = start_date + timedelta(days=7)
df = results[(results['start_date'] >= str(start_date)) & (results['end_date'] < str(end_date))]

while df.shape[0] > 0:

    df = df.sample(frac=1)
    df = df.reset_index(drop=True)

    X = df[['ob_level', 'os_level', 'k']].to_numpy()
    y = df['clean_gains'].to_numpy()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    r2_scores = []  # stores the performance results of all the models

    # Linear Regression
    linear = LinearRegression()
    linear.fit(X_train, y_train)
    linear_y_pred = linear.predict(X_test)
    linear_R2 = metrics.r2_score(y_test, linear_y_pred)
    arr = [linear, linear_R2]
    r2_scores.append(arr)

    # Ridge Regression
    param_grid = {'alpha': np.arange(0.00001, 0.001, 0.00001)}
    model = Ridge()
    clf = GridSearchCV(model, param_grid)
    clf.fit(X_train, y_train)
    ridge = clf.best_estimator_
    ridge_y_pred = ridge.predict(X_test)
    ridge_R2 = metrics.r2_score(y_test, ridge_y_pred)
    arr = [ridge, ridge_R2]
    r2_scores.append(arr)

    # Stochastic Gradient Descent
    sgd = SGDRegressor()
    sgd.fit(X_train, y_train)
    sgd_y_pred = linear.predict(X_test)
    sgd_R2 = metrics.r2_score(y_test, sgd_y_pred)
    arr = [sgd, sgd_R2]
    r2_scores.append(arr)

    # Bayesian ARD Regression
    ard = ARDRegression()
    ard.fit(X_train, y_train)
    ard_y_pred = linear.predict(X_test)
    ard_R2 = metrics.r2_score(y_test, ard_y_pred)
    arr = [ard, ard_R2]
    r2_scores.append(arr)

    # Bayesian Ridge
    bayesian_ridge = BayesianRidge()
    bayesian_ridge.fit(X_train, y_train)
    bayesian_ridge_y_pred = bayesian_ridge.predict(X_test)
    bayesian_ridge_R2 = metrics.r2_score(y_test, bayesian_ridge_y_pred)
    arr = [bayesian_ridge, bayesian_ridge_R2]
    r2_scores.append(arr)

    # Decision Tree Regressor
    param_grid = {'random_state': range(0, 10),
                  'criterion': ['mse', 'friedman_mse', 'mae'],
                  'splitter': ['best', 'random']}
    model = DecisionTreeRegressor()
    clf = GridSearchCV(model, param_grid)
    clf.fit(X_train, y_train)
    dt = clf.best_estimator_
    dt_y_pred = dt.predict(X_test)
    dt_R2 = metrics.r2_score(y_test, dt_y_pred)
    arr = [dt, dt_R2]
    r2_scores.append(arr)

    # Support Vector Regressor
    param_grid = {'C': [1, 10, 100, 1000],
                  'epsilon': np.arange(0.01, 1, 0.01)}
    model = SVR()
    clf = GridSearchCV(model, param_grid)
    clf.fit(X_train, y_train)
    svr = clf.best_estimator_
    svr_y_pred = svr.predict(X_test)
    svr_R2 = metrics.r2_score(y_test, svr_y_pred)
    arr = [svr, svr_R2]
    r2_scores.append(arr)

    # NuSVR
    param_grid = {'C': [1, 10, 100, 1000],
                  'nu': np.arange(0.01, 1, 0.01)}
    model = NuSVR()
    clf = GridSearchCV(model, param_grid)
    clf.fit(X_train, y_train)
    nu_svr = clf.best_estimator_
    nu_svr_y_pred = nu_svr.predict(X_test)
    nu_svr_R2 = metrics.r2_score(y_test, nu_svr_y_pred)
    arr = [nu_svr, nu_svr_R2]
    r2_scores.append(arr)

    # KNN Regressor
    param_grid = {'n_neighbors': range(2, 30)}
    model = KNeighborsRegressor()
    clf = GridSearchCV(model, param_grid)
    clf.fit(X_train, y_train)
    knn = clf.best_estimator_
    knn_y_pred = knn.predict(X_test)
    knn_R2 = metrics.r2_score(y_test, knn_y_pred)
    arr = [knn, knn_R2]
    r2_scores.append(arr)

    # Gradient Boosting Regressor
    param_grid = {'learning_rate': np.arange(0.1, 0.5, 0.1),
                  'loss': ['ls', 'lad', 'huber', 'quantile'],
                  'criterion': ['friedman_mse', 'mse']}
    model = GradientBoostingRegressor()
    clf = GridSearchCV(model, param_grid)
    clf.fit(X_train, y_train)
    gbr = clf.best_estimator_
    gbr_y_pred = gbr.predict(X_test)
    gbr_R2 = metrics.r2_score(y_test, gbr_y_pred)
    arr = [gbr, gbr_R2]
    r2_scores.append(arr)

    # Model selection
    best_model = r2_scores[0]
    for arr in r2_scores:
        if arr[1] > best_model[1]:
            best_model = arr
    model = best_model[0]

    # Optimize
    best_result = 0
    best_parameters = {'ob_level': -1,
                       'os_level': -1,
                       'k': -1}
    for k in np.arange(0.001, 0.030, 0.001):
        for ob_level in range(43, 63):
            for os_level in range(-63, -43):
                prediction = model.predict([[ob_level, os_level, k]])
                if prediction > best_result:
                    best_result = prediction
                    best_parameters = {'ob_level': ob_level,
                                       'os_level': os_level,
                                       'k': k}

    first_df_row = df.iloc[0]
    aux_df = pd.DataFrame([[first_df_row['mean'], first_df_row['std'], first_df_row['skewness'], first_df_row['kurtosis'],
                            first_df_row['entropy'], best_parameters['ob_level'], best_parameters['os_level'],
                            best_parameters['k'], best_result[0], best_model[1]]], columns=['mean', 'std', 'skewness',
                            'kurtosis', 'entropy', 'ob_level', 'os_level', 'k', 'clean_gains', 'r2'])
    final_df = final_df.append(aux_df, ignore_index=True)

    print(str(start_date) + ' - ' + str(end_date) + '    DONE.')
    start_date = end_date
    end_date = start_date + timedelta(days=7)
    df = results[(results['start_date'] >= str(start_date)) & (results['end_date'] < str(end_date))]

final_df.to_csv('../Data/OptimizationData/ADAUSDT_7_5_wave_trend_optimizations.csv', index=False)

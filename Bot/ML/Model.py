import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn import metrics
from sklearn.model_selection import GridSearchCV


class Model:

    def __init__(self, file_path):
        results = pd.read_csv(file_path)
        df = results[results['clean_gains'] != 0]
        df = df.drop(
            columns=['symbol', 'indicator', 'start_date', 'end_date', 'mean', 'n_total_partitions', 'n_partitions'])

        X = df[['ob_level', 'os_level', 'k', 'std', 'skewness', 'kurtosis', 'entropy']].to_numpy()
        y = df['clean_gains'].to_numpy()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

        model_scores = []  # List of tuples

        # Multilayer Perceptron Regressor
        param_grid = {'activation': ['identity', 'logistic', 'tanh', 'relu'],
                      'solver': ['lbfgs', 'sgd', 'adam'],
                      'learning_rate': ['constant', 'invscaling', 'adaptive']}
        model = MLPRegressor(random_state=1, max_iter=1000)
        clf = GridSearchCV(model, param_grid)
        clf.fit(X_train, y_train)
        mlp = clf.best_estimator_
        mlp_y_pred = mlp.predict(X_test)
        mlp_r2 = metrics.r2_score(y_test, mlp_y_pred)
        model_scores.append((mlp, mlp_r2))
        print('MLP: ' + str(mlp_r2))

        # Gradient Boosting Regressor
        param_grid = {'loss': ['ls', 'lad', 'huber', 'quantile'],
                      'criterion': ['friedman_mse', 'mse', 'mae'],
                      'max_features': ['auto', 'sqrt', 'log2']}
        model = GradientBoostingRegressor()
        clf = GridSearchCV(model, param_grid)
        clf.fit(X_train, y_train)
        gbr = clf.best_estimator_
        gbr_y_pred = gbr.predict(X_test)
        gbr_r2 = metrics.r2_score(y_test, gbr_y_pred)
        model_scores.append((gbr, gbr_r2))
        print('GBR: ' + str(gbr_r2))

        # Gaussian Process Regressor
        param_grid = {'normalize_y': [True, False]}
        model = GaussianProcessRegressor()
        clf = GridSearchCV(model, param_grid)
        clf.fit(X_train, y_train)
        gpr = clf.best_estimator_
        gpr_y_pred = gpr.predict(X_test)
        gpr_r2 = metrics.r2_score(y_test, gpr_y_pred)
        model_scores.append((gpr, gpr_r2))
        print('GPR: ' + str(gpr_r2))

        # Decision Tree Regressor
        param_grid = {'criterion': ['mse', 'friedman_mse', 'mae'],
                      'splitter': ['best', 'random'],
                      'max_features': ['auto', 'sqrt', 'log2']}
        model = DecisionTreeRegressor()
        clf = GridSearchCV(model, param_grid)
        clf.fit(X_train, y_train)
        dt = clf.best_estimator_
        dt_y_pred = dt.predict(X_test)
        dt_r2 = metrics.r2_score(y_test, dt_y_pred)
        model_scores.append((dt, dt_r2))
        print('DT: ' + str(dt_r2))

        # Random Forests Regressor
        param_grid = {'n_estimators': [75, 100, 125, 150],
                      'criterion': ['mse', 'mae']}
        model = RandomForestRegressor()
        clf = GridSearchCV(model, param_grid)
        clf.fit(X_train, y_train)
        rf = clf.best_estimator_
        rf_y_pred = rf.predict(X_test)
        rf_r2 = metrics.r2_score(y_test, rf_y_pred)
        model_scores.append((rf, rf_r2))
        print('RF: ' + str(rf_r2))

        # K Neighbors Regressor
        param_grid = {'n_neighbors': range(2, 30)}
        model = KNeighborsRegressor()
        clf = GridSearchCV(model, param_grid)
        clf.fit(X_train, y_train)
        knr = clf.best_estimator_
        knr_y_pred = knr.predict(X_test)
        knr_r2 = metrics.r2_score(y_test, knr_y_pred)
        model_scores.append((knr, knr_r2))
        print('KNR: ' + str(knr_r2))

        # Model Selection
        self.max_r2 = 0
        self.best_model = None
        for t in model_scores:
            if self.max_r2 < t[1]:
                self.max_r2 = t[1]
                self.best_model = t[0]

    def predict(self, std, skewness, kurtosis, entropy):
        best_pred = 0
        best_params = {'ob_level': None,
                       'os_level': None,
                       'k': None}

        for ob_level in range(43, 63, 5):
            for os_level in range(-63, -43, 5):
                for k in np.arange(0.001, 0.030, 0.001):
                    x = [[std, skewness, kurtosis, entropy, ob_level, os_level, k]]
                    pred = self.best_model.predict(x)
                    if pred > best_pred:
                        best_pred = pred
                        best_params['ob_level'] = ob_level
                        best_params['os_level'] = os_level
                        best_params['k'] = k

        return best_params

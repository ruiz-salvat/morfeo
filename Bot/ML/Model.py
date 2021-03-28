import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from Util.Constants import wave_trend_pattern_id, wave_trend_parameters, model_global_parameters, pattern_not_found, \
    wave_trend_parameter_ranges


class Model:

    def __init__(self, file_path, pattern_id):
        self.pattern_id = pattern_id
        if self.pattern_id == wave_trend_pattern_id:
            self.model_parameters = wave_trend_parameters
        else:
            raise Exception(pattern_not_found)

        # Load data sets
        results = pd.read_csv(file_path)
        df = results[results['clean_gains'] != 0]
        parameters = self.model_parameters.copy()
        parameters.extend(model_global_parameters)
        X = df[parameters].to_numpy()
        y = df['clean_gains'].to_numpy()
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

        # List of tuples
        model_scores = []

        # Gradient Boosting Regressor
        param_grid = {'loss': ['ls', 'lad', 'huber', 'quantile'],
                      'criterion': ['friedman_mse', 'mse'],
                      'max_features': ['auto', 'sqrt', 'log2']}
        model = GradientBoostingRegressor()
        clf = GridSearchCV(model, param_grid)
        clf.fit(X_train, y_train)
        gbr = clf.best_estimator_
        gbr_y_pred = gbr.predict(X_test)
        gbr_r2 = metrics.r2_score(y_test, gbr_y_pred)
        model_scores.append((gbr, gbr_r2))

        # Gaussian Process Regressor
        param_grid = {'normalize_y': [True, False]}
        model = GaussianProcessRegressor()
        clf = GridSearchCV(model, param_grid)
        clf.fit(X_train, y_train)
        gpr = clf.best_estimator_
        gpr_y_pred = gpr.predict(X_test)
        gpr_r2 = metrics.r2_score(y_test, gpr_y_pred)
        model_scores.append((gpr, gpr_r2))

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

        # K Neighbors Regressor
        param_grid = {'n_neighbors': range(2, 30)}
        model = KNeighborsRegressor()
        clf = GridSearchCV(model, param_grid)
        clf.fit(X_train, y_train)
        knr = clf.best_estimator_
        knr_y_pred = knr.predict(X_test)
        knr_r2 = metrics.r2_score(y_test, knr_y_pred)
        model_scores.append((knr, knr_r2))

        # Model Selection
        self.max_r2 = 0
        self.best_model = None
        for t in model_scores:
            if self.max_r2 < t[1]:
                self.max_r2 = t[1]
                self.best_model = t[0]

    def predict(self, std, skewness, kurtosis, entropy):
        best_pred = 0
        best_params = {'pattern_id': self.pattern_id}
        for p in self.model_parameters:
            best_params[p] = None

        parameter_combinations = generate_iterable(self.pattern_id)
        for comb in parameter_combinations:
            aux = comb.copy()
            aux.extend([std, skewness, kurtosis, entropy])
            x = [aux]
            pred = self.best_model.predict(x)
            if pred > best_pred:
                best_pred = pred
                count = 0
                for k in self.model_parameters:
                    best_params[k] = comb[count]
                    count += 1

        return best_params


def generate_iterable(pattern_name):
    model_parameters = None
    if pattern_name == wave_trend_pattern_id:
        model_parameters = wave_trend_parameters
    else:
        raise Exception(pattern_not_found)

    if model_parameters is not None:
        a = wave_trend_parameter_ranges[0]
        b = []
        for i in range(len(model_parameters) - 1):
            for j in a:
                for k in wave_trend_parameter_ranges[i + 1]:
                    if isinstance(j, int):
                        aux = [j].copy()
                    else:
                        aux = j.copy()
                    aux.extend([k])
                    b.append(aux)
            a = b
            b = []

        return a
    else:
        raise Exception('Model parameter list is null')

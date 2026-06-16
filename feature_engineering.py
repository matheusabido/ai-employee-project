from sklearn.base import BaseEstimator, TransformerMixin

class FeatureEngineering(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X['age_x_experience'] = X['Age'] * X['YearsAtCompany']
        X['age_group'] = X['Age'] // 10
        return X
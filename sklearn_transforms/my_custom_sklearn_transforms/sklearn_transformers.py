from pandas import Categorical, get_dummies
from sklearn.base import TransformerMixin, BaseEstimator

class CategoricalEncoder(BaseEstimator, TransformerMixin):
    """One hot encoder for all categorical features"""
    def __init__(self, attribute_names):
        #list of column names with categorical variables
        self.attribute_names = attribute_names

    def fit(self, X, y=None):
        #create empty dictionary
        cats = {}
        #for each categorical column, create a key in the dictionary
        #with the column name and create keys from the unique values in that column
        for column in self.attribute_names:
            cats[column] = X[column].unique().tolist()
        self.categoricals = cats
        return self

    def transform(self, X, y=None):
        df = X.copy()
        for column in self.attribute_names:
            df[column] = Categorical(df[column], categories=self.categoricals[column])
        new_df = get_dummies(df, drop_first=False)
        # in case we need them later
        self.columns = new_df.columns
        return new_df

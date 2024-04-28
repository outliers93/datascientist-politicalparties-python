import pandas as pd

from political_party_analysis.dim_reducer import DimensionalityReducer
from fitter import Fitter, get_common_distributions, get_distributions


class DensityEstimator:
    """Class to estimate Density/Distribution of the given data.
    1. Write a function to model the distribution of the political party dataset
    2. Write a function to randomly sample 10 parties from this distribution
    3. Map the randomly sampled 10 parties back to the original higher dimensional
    space as per the previously used dimensionality reduction technique.
    """

    def __init__(
        self,
        data: pd.DataFrame,
        dim_reducer: DimensionalityReducer,
        high_dim_feature_names,
    ):
        self.data = data
        self.dim_reducer_model = dim_reducer.model
        self.feature_names = high_dim_feature_names

    def distribution(self, variable: str):
        col = self.data[variable].values
        f = Fitter(col, distributions=["gamma", "lognorm", "beta", "burr", "norm"])
        f.fit()
        return f.get_best(method="sumsquare_error")[0], f.get_best(method="sumsquare_error")[1]

    def ramdom_sample(self, distribution: pd.Series):
        mu, sigma = 0, 0.1  # mean and standard deviation
        data = np.random.normal(mu, sigma, 10000)
        distribution.sample(n=10)
        pass

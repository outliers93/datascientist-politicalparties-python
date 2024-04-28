import pandas as pd
from sklearn.decomposition import PCA


class DimensionalityReducer:
    """Class to model a dimensionality reduction method for the given dataset.
    1. Write a function to convert the high dimensional data to 2 dimensional.
    """

    def __init__(self, data: pd.DataFrame, n_components: int = 2):
        self.n_components = n_components
        self.data = data
        self.feature_columns = data.columns
        self.model = PCA(n_components=n_components)
        self._data_reduced = None

    def _process_data(self) -> pd.DataFrame:
        data = pd.DataFrame(
            self.model.fit_transform(self.data),
            columns=[f"C_{i+1}" for i in range(self.n_components)],
            index=self.data.index,
        )
        return data

    @property
    def data_reduced(self) -> pd.DataFrame:
        if self._data_reduced is None:
            self._data_reduced = self._process_data()
        return self._data_reduced

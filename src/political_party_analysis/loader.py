from pathlib import Path
from typing import List
from urllib.request import urlretrieve

import pandas as pd
from sklearn.preprocessing import StandardScaler


class DataLoader:
    """Class to load the political parties dataset"""

    data_url: str = "https://www.chesdata.eu/s/CHES2019V3.dta"

    def __init__(self):
        self.party_data = self._download_data()
        self.non_features = []
        self.index = ["party_id", "party", "country"]

    def _download_data(self) -> pd.DataFrame:
        data_path, _ = urlretrieve(
            self.data_url,
            Path(__file__).parents[2].joinpath(*["data", "CHES2019V3.dta"]),
        )

        return pd.read_stata(data_path)

    @staticmethod
    def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
        """Write a function to remove duplicates in a dataframe"""
        # Probablemente si no hacemos nada más en este metodo, podemos omitirlo
        return df.drop_duplicates()

    def remove_nonfeature_cols(
        self, df: pd.DataFrame, non_features: List[str], index: List[str]
    ) -> pd.DataFrame:
        """Write a function to remove certain features cols and set certain cols as indices
        in a dataframe"""
        ##### YOUR CODE GOES HERE #####
        df = df.drop(columns=non_features).set_index(keys=index)
        df.index.name = "id"
        return df

    def handle_NaN_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Write a function to handle NaN values in a dataframe"""
        ##### YOUR CODE GOES HERE #####
        df_boolean: pd.Series = df.isnull().all()
        all_nan_cols: List[str] = list(df_boolean[df_boolean == True].index)
        df = df.drop(columns=all_nan_cols)
        return df.fillna(df.mean())

    def scale_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Write a function to normalise values in a dataframe. Use StandardScaler."""
        scaler = StandardScaler()
        scaler.fit(df)
        return pd.DataFrame(scaler.transform(df), columns=df.columns, index=df.index)

    def preprocess_data(self):
        """Write a function to combine all pre-processing steps for the dataset"""
        # Remove Non Feature columns
        self.party_data = self.remove_nonfeature_cols(
            df=self.party_data, non_features=self.non_features, index=self.index
        )
        # Remove duplicates
        self.party_data = self.remove_duplicates(df=self.party_data)

        self.party_data = self.handle_NaN_values(df=self.party_data)

        self.party_data = self.scale_features(df=self.party_data)

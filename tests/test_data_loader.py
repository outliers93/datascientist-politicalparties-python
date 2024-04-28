import numpy as np
import pandas as pd
import pytest
from pandas.testing import assert_frame_equal
from political_party_analysis.loader import DataLoader


@pytest.fixture
def mock_df() -> pd.DataFrame:
    data = {
        "id": [0, 1, 2, 2],
        "col1": [1, 2, 3, 3],
        "col2": [30.0, np.nan, 30.0, 30.0],
        "col3": [5, 7, 12, 12],
        "non_feature": ["a", "b", "c", "c"],
        "all_nans": [np.nan] * 4,
    }
    df = pd.DataFrame(data=data)
    return df


def test_download_data(mocker):
    data_loader = DataLoader()
    assert data_loader.party_data.shape == (277, 55)


def test_preprocess_data(mocker, mock_df: pd.DataFrame):
    mocker.patch(
        "political_party_analysis.loader.DataLoader._download_data",
        return_value=mock_df,
    )
    # Mock DataLoader._download_data first to do not attempt to pull real data
    data_loader = DataLoader()
    mocker.patch.object(data_loader, "non_features", ["non_feature"])
    mocker.patch.object(data_loader, "index", "id")
    data_loader.preprocess_data()
    expected_df = pd.DataFrame(
        data={
            "col1": [-1.225, 0, 1.225],
            "col2": [0.0] * 3,
            "col3": [-1.019, -0.340, 1.359],
        },
        index=[0, 1, 2],
    )
    expected_df.index.name = "id"
    assert_frame_equal(data_loader.party_data, expected_df, check_less_precise=3)

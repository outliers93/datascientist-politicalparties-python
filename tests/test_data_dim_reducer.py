import pandas as pd
import pytest

from political_party_analysis.dim_reducer import DimensionalityReducer


@pytest.fixture
def mock_df() -> pd.DataFrame:
    df = pd.DataFrame(
        data={
            "col1": [-1.225, 0, 1.225],
            "col2": [-1.175, -0.1, 1.257],
            "col3": [-1.019, -0.340, 1.359],
        },
        index=[0, 1, 2],
    )
    df.index.name = "id"
    return df


def test_dim_reducer(mock_df):
    # Esta prueba esta siendo testeada para n_component = 2
    reducer = DimensionalityReducer(data=mock_df)
    assert reducer.data_reduced.shape == (mock_df.shape[0], 2)
    assert list(reducer.data_reduced.columns) == ["C_1", "C_2"]
    # No usar expected_df como caso de prueba acá por que es el output de un algoritmo
    # dificil de calcular por fuera del mismo código (a mano)

from political_party_analysis.loader import DataLoader
from fitter import Fitter, get_common_distributions, get_distributions

data_loader = DataLoader()
print(data_loader.party_data)
print(data_loader.party_data.info())
print(data_loader.party_data.describe())
print(len(data_loader.party_data.columns))
# data_loader.preprocess_data()
# data_pre = data_loader.party_data

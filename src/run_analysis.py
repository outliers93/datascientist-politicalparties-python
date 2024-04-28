from pathlib import Path

from matplotlib import pyplot

from political_party_analysis.loader import DataLoader
from political_party_analysis.visualization import scatter_plot

from political_party_analysis.dim_reducer import DimensionalityReducer

if __name__ == "__main__":

    data_loader = DataLoader()
    # Data pre-processing step
    data_loader.preprocess_data()
    data_pre = data_loader.party_data

    # Dimensionality reduction step
    dim_reducer = DimensionalityReducer(data=data_pre, n_components=2)
    reduced_dim_data = dim_reducer.data_reduced

    pyplot.figure()
    splot = pyplot.subplot()
    scatter_plot(
        reduced_dim_data,
        color="r",
        splot=splot,
        label="dim reduced data",
    )
    pyplot.savefig(Path(__file__).parents[1].joinpath(*["plots", "dim_reduced_data.png"]))

    # Density estimation/distribution modelling step

    import pdb

    pdb.set_trace
    # Plot density estimation results here
    ##### YOUR CODE GOES HERE #####
    pyplot.savefig(Path(__file__).parents[1].joinpath(*["plots", "density_estimation.png"]))

    # Plot left and right wing parties here
    pyplot.figure()
    splot = pyplot.subplot()
    ##### YOUR CODE GOES HERE #####
    pyplot.savefig(Path(__file__).parents[1].joinpath(*["plots", "left_right_parties.png"]))
    pyplot.title("Lefty/righty parties")

    # Plot finnish parties here
    ##### YOUR CODE GOES HERE #####

    print("Analysis Complete")

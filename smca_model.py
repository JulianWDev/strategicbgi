# Python implementation of the SMCA model
# Required inputs:
# - Three raster files representing the three (kriged/calculated) input criteria
# - A numpy array representing the weights for each criterion
# - A numpy array indicating the type of each criterion (1 for benefit, 0 for cost)
import numpy as np
import rasterio as rio

def smca_model(criterion1, criterion2, criterion3, weights, types):
    """
    Perform the SMCA model calculation.

    Parameters:
    criterion1 (numpy.ndarray): First criterion raster.
    criterion2 (numpy.ndarray): Second criterion raster.
    criterion3 (numpy.ndarray): Third criterion raster.
    weights (numpy.ndarray): Weights for each criterion.
    types (numpy.ndarray): Types of each criterion (1 for benefit, 0 for cost).

    Returns:
    numpy.ndarray: Resulting raster after applying the SMCA model.
    """
    
    # Normalize the criteria
    norm_criterion1 = (criterion1 - np.min(criterion1)) / (np.max(criterion1) - np.min(criterion1))
    norm_criterion2 = (criterion2 - np.min(criterion2)) / (np.max(criterion2) - np.min(criterion2))
    norm_criterion3 = (criterion3 - np.min(criterion3)) / (np.max(criterion3) - np.min(criterion3))

    # Apply weights and types
    result = (
        weights[0] * norm_criterion1 * types[0] +
        weights[1] * norm_criterion2 * types[1] +
        weights[2] * norm_criterion3 * types[2]
    )

    return result


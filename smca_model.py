# Python implementation of the SMCA model
# Required inputs:
# - Dict with the arrays representing the three (kriged/calculated) input criteria rasters
# - A numpy array representing the weights for each criterion
# - A numpy array indicating the type of each criterion (1 for benefit, 0 for cost)
import numpy as np
import rasterio as rio

def smca_model(data, weights, types, output_file, profile_file):
    """
    SMCA model implementation.
    
    Parameters:
    ksat (rasterio.DatasetReader): Saturated hydraulic conductivity raster.
    wcs (rasterio.DatasetReader): Water content saturation raster.
    alt_dev (rasterio.DatasetReader): Altitude deviation raster.
    weights (np.ndarray): Weights for each criterion.
    types (np.ndarray): Types of each criterion (1 for benefit, 0 for cost).
    
    Returns:
    np.ndarray: Resulting raster after applying the SMCA model.
    """
        
    # Stack the data
    data = np.stack((data['ksat'], data['wcs'], data['alt_dev']), axis=-1)

    # Apply weights and types
    weighted_data = data * weights * types[:, np.newaxis]
    
    # Sum the weighted data
    result = np.sum(weighted_data, axis=-1)
    
    # Save the result to a file
    profile = rio.open(profile_file).profile
    with rio.open(output_file, 'w', **profile) as dst:
        dst.write(result, 1)

    return result
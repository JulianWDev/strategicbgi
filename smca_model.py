# Python implementation of the SMCA model
# Required inputs:
# - Three arrays representing the three (kriged/calculated) input criteria rasters
# - A list representing the weights for each criterion
# - A list indicating the type of each criterion (1 for benefit, 0 for cost)
import numpy as np
import rasterio as rio

def model(ksat_data, wcs_data, alt_dev_data, weights, types):
    # Check if data are the same size/shape, if not raise an error
    if ksat_data.shape != wcs_data.shape or ksat_data.shape != alt_dev_data.shape:
        raise ValueError("Input data must have the same shape")

    # Multiply ksat by the appropriate weight and invert if required
    if types[0] == 0:
        ksat_data = 1 - ksat_data
    ksat_weighted = ksat_data * weights[0]

    # Multiply wcs by the appropriate weight and invert if required
    if types[1] == 0:
        wcs_data = 1 - wcs_data
    wcs_weighted = wcs_data * weights[1]

    # Multiply alt_dev by the appropriate weight and invert if required
    if types[2] == 0:
        alt_dev_data = 1 - alt_dev_data
    alt_dev_weighted = alt_dev_data * weights[2]
    
    # Sum the weighted data
    result = np.sum([ksat_weighted, wcs_weighted, alt_dev_weighted], axis=0)

    return result

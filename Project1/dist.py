# File contains functions for computing the 2-D and 3-D distances between points in SDSS
import numpy as np

# Start with the 2-D distance finder
def dist_2D(ra1, ra2, dec1, dec2):
    # Inputs should be given in degrees, since this is how the SDSS data is formatted
    # Thus, output will be an angular separation in degrees

    # Make sure all of the inputs have the same shape
    shape = np.shape(ra1);
    if np.shape(ra2) != shape or np.shape(dec1) != shape or np.shape(dec2) != shape:
        raise Exception('Inputs passed to dist_2D() have incompatible sizes:\n'
            f'{np.shape(ra1)},\t{np.shape(ra2)},\t{np.shape(dec1)},\t{np.shape(dec2)}');

    # Start by turning everything into radians
    ra1 = np.deg2rad(ra1);
    ra2 = np.deg2rad(ra2);
    dec1 = np.deg2rad(dec1);
    dec2 = np.deg2rad(dec2);

    # Get all of the needed sines and cosines
    dec1s = np.sin(dec1); dec1c = np.cos(dec1);
    dec2s = np.sin(dec2); dec2c = np.cos(dec2);
    drac = np.cos(ra1-ra2);

    # Finally, compute the output
    dr = np.arccos(np.multiply(dec1s, dec2s) + np.multiply(np.multiply(dec1c, dec2c), drac));

    # Get output in degrees
    dr = np.rad2deg(dr);
    if dr < 0:
        dr += 90;

    # Return output in range of degrees [0, 180];
    return dr

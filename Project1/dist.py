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

# The 3-D distance finder is harder
# One version for computing from redshift
def dist_3D_from_z(ra1, ra2, dec1, dec2, z1, z2):
    # Inputs are given in degrees and in redshift
    # Convert from redshift to comoving dist, then call the regular 3D distance function
    # Outputs a comoving distance in Megaparsecs

    # Get the comoving distances of each galaxy based on redshift
    d1 = z2d_comoving(z1);
    d2 = z2d_comoving(z2);
    
    # Call the regular 3D distance function
    return dist_3D(ra1, ra2, dec1, dec2, d1, d2);

# Second (regular) version computes from comoving distances
def dist_3D(ra1, ra2, dec1, dec2, d1, d2):
    # Inputs are given in degrees and in comoving distances
    # Outputs a comoving distance in Megaparsecs

    # We want the modulus of r_1 - r_2, so we need to compute r_1.r_2
    # Get angle between two galaxies using dist_2D
    angle = dist_2D(ra1, ra2, dec1, dec2);
    # Convert to radians
    angle = np.deg2rad(angle);
    # Compute the dot product
    dot = d1*d2*np.cos(angle);

    # Now compute magnitude of r_1-r_2 in Mpc
    dr = np.sqrt(d1**2 + d2**2 - 2*dot);

    # Return this distance
    return dr

# Helper function to convert from reshift to comoving distance
def z2d_comoving(z, lambda_M=0.315, lambda_L=0.689, h=0.674):
    # Inputs are redshift
    # Default cosmological parameters are those of the latest Planck release

    # Do the 1/H(z') integral from z'=0 to z'=z
    d = int_1overH(z, M=lambda_M, L=lambda_L);

    # Multiply by factor of comoving Hubble Horizon for answer in Mpc
    return np.multiply(d, 3000/h);

# Helper function for computing the comoving distance integral
def int_1overH(zs, zl=0, M=0.315, L=0.689, dz=1e-5):
    # Define a numpy array of the redshift bin centers that we will use
    z = np.arange(zl, zs, dz) + dz/2;

    # Compute height of integrand at each value of z
    f = np.power(M*np.power(1+z, 3) + L, -0.5);

    # Sum over heights and multiply by dz
    value = np.sum(f) * dz;

    return value
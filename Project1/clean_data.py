# Script to extract and clean data from SDSS data file
from astropy.io import fits
import numpy as np
import pandas
import os.path
from dist import z2d_comoving
from tqdm import tqdm

# Look for SDSS data file
filename = 'galaxy_DR12v5_CMASSLOWZ_North.fits';
if not os.path.isfile(filename):
    Exception(f'{filename} is not found. See README.md for instructions on prepping the data file!');

# Assuming file exists, we continue
# Read in the file, [1] ignores headers
fitsdat=fits.open(filename)[1];

# Extract the RA, Dec, and redshift of each galaxy
ra = fitsdat.data.field('RA');
dec = fitsdat.data.field('DEC');
z = fitsdat.data.field('Z');

# Convert from redshift to comoving distance in units of Mpc
d = [None] * len(z)
for i in tqdm(range(len(z))):
    d[i] = z2d_comoving(z[i]);

# Create a pandas dataframe to hold these three variables
datframe = pandas.DataFrame({'RA': ra, 'Dec': dec, 'redshift': z, 'd_comoving': d});

# Save data as a .csv
outname = 'galdata.csv';
datframe.to_csv(outname);
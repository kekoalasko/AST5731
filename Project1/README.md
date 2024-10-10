# AST 5731 - Project 1
Analyzing density distribution of galaxies using SDSS data.

## Setup
Not really sure what the rules are for uploading data sets to a git repo, so here's how to obtain the data yourself

1. Go to public [SDSS Data repository](https://data.sdss.org/sas/dr12/boss/lss/?C=M&O=D)
2. Download the file: `galaxy_DR12v5_CMASSLOWZTOT_North.fits.gz`
3. Move to the `Project1/` directory - both the command line (using `cd`) and the downloaded file
4. Unzip the .gz file. For Linux and Mac users, this can be done through the gzip command line utility
    ```bash
    gzip -d galaxy_DR12v5_CMASSLOWZTOT_North.fits.gz
    ```
    Good luck if you're on Windows.
5. Run the `clean_data.py` script. This can be done through the command line
    ```bash
    python clean_data.py
    ```
6. You can now delete the ``galaxy_DR12v5_CMASSLOWZTOT_North.fits` file if desired. It is no longer needed.

## Running the code
If computing the 3D distances, then the longest step of running the code is converting from redshift to comoving distances (units of Mpc).

**We should set up the code to first compute the distances to every galaxy (function `dist.dist_3D_from_z()`) and save this output. Then we can compute the distances between each galaxy using the comoving distances instead of the redshifts (function `dist.dist_3D()`).**

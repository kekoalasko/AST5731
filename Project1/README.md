# AST 5731 - Project 1
Analyzing density distribution of galaxies using SDSS data.

## Setup
Not really sure what the rules are for uploading data sets to a git repo, so here's how to obtain the data yourself

+ Go to public [SDSS Data repository](https://data.sdss.org/sas/dr12/boss/lss/?C=M&O=D)
+ Download the file: `galaxy_DR12v5_CMASSLOWZTOT_North.fits.gz`
+ Unzip the .gz file. For Linux and Mac users, this can be done through the gzip command line utility
    ```bash
    gzip -d /PATH/TO/galaxy_DR12v5_CMASSLOWZTOT_North.fits.gz
    ```
    Good luck if you're on Windows.

Put the `.fits` file in this directory. Loading the data requires the path be the local `./` directory.

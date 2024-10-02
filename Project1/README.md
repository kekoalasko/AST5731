First project for AST 5731 course. Analyzing density distribution of galaxies using SDSS data.

Not really sure what the rules are for uploading data sets to a git repo, so here's how to obtain the data yourself
<ul>
    <li>Go to public SDSS Data repository: https://data.sdss.org/sas/dr12/boss/lss/?C=M&O=D</li>
    <li>Download the file: galaxy_DR12v5_CMASSLOWZTOT_North.fits.gz</li>
    <li>Unzip the .gz file. For Linux and Mac users, this can be done through the gzip command line utility <code>$ gzip -d /PATH/TO/galaxy_DR12v5_CMASSLOWZTOT_North.fits.gz</code>. Good luck if you're on Windows.</li>
</ul>
Put the .fits file in this directory. Loading the data requires the path be the local <code>./</code> directory.
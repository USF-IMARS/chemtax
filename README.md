# CHEMTAX v2+

This project is a retooling of the CHEMTAX methods originally implemented in MATLAB (v1), then again released as a standalone software working with excel files ([v1.95](https://data.aad.gov.au/metadata/records/CHEMTAX)).

## Planning
1. user input
    1. samples pigment data table
        1. (csv file) - one sample per row, one pigment per column 
        2. or seabass file?
    3. list of taxa present
        1. (extra feature?) Would a taxa liklihood value be useful here? What about a taxa co-occurence matrix?
    4. (extra feature?) include/exclude specific pigment columns
    5. (optional) matrix init random seed(s)
    6. (optional) custom pigment-ratio-to-taxa matrix
3. run multiple solutions starting from different randomized input matricies
    1. (optional) show graphical representation of convergence
4. results
    1. collate and plot the final pigment:chla ratios for each taxon in each run vs RMS residuals of Chl a. Example plot [TODO](ln_here).
        1. allows user to check robustness of the convergence
        2. allows user to check if there is “flip-flopping”, i.e. taxa w/ similar pigments effectively swapping identities bc the randomisation process has made the starting ratio for taxon A more like the actual ratio for taxon B than the starting point for taxon B.

## Other Links

* R implementation of CHEMTAX [[1](https://github.com/MarPolar/CHEMTAX)], [[2](https://github.com/silviageor/chemtax)].
* [docs for R implementation included within the limSolve R library](https://www.rdocumentation.org/packages/limSolve/versions/1.5.6/topics/Chemtax)
* example .txt matricies used by oceanspace?](https://github.com/oceanspace/chemtax-tools) 
* (broken?) [chemtax google forum](http://groups.google.com/forum/#!forum/chemtax_users)

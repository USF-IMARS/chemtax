# CHEMTAX v2+

This project is a retooling of the CHEMTAX methods originally implemented in MATLAB (v1), then again released as a standalone software working with excel files ([v1.95](https://data.aad.gov.au/metadata/records/CHEMTAX)).

This repo contains general information and is used for planning around the CHEMTAX-IMaRS collaboration.

Other relevant repos:
* [chemtax-r](https://github.com/USF-IMARS/rCHEMTAX) : R port of CHEMTAX
* [chemtax-shiny-gui](https://github.com/USF-IMARS/chemtax-shiny-gui) GUI to help with using chemtax

[![Open a demo with myBinder.org](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/USF-IMARS/chemtax/HEAD)

## Planning
1. user input
    1. cluster sample rows into similar environments (like depth ranges) before running 
        1. (optional) auto-cluster
        2. (optional) allow selection of cluster groups 
    2. samples pigment data table (all data goes in, but the cluster is what we are focusing on)
        1. (csv file) - one sample per row, one pigment per column 
        2. or SeaBASS file? (also includes lat, lon, timestamp)
    3. list of taxa present
        1. (extra feature) Taxa liklihood value (ones you know are present & ones that might be) 
        2. (extra feature) What about a taxa co-occurence matrix?
    4. (extra feature?) include/exclude specific pigment columns
    5. (optional) matrix init random seed(s)
    6. (optional) custom pigment-ratio-to-taxa tables (from culture data) 
        1. open-data table repository to pick & submit tables from
3. run multiple solutions starting from different randomized input matricies
    0. 20 (TODO: play w/ this number) randomized starting ratio tables, 60 gradient decent iterations (TODO: play w/ number of iterations) 
    1. (optional) show graphical representation of convergence
    2. Start from assumed ratios from lit & iteratively minimizes RMS between current taxa occurence matrix & expected.
        3. TODO: try other methods to avoid local minima 
        4. current method to avoid local minima is to do multiple starts from randoms
    3. original code in MATLAB, rewritten C++
    4. new algorithm (more efficient) written in OCTAVE
        1. assumes normal distribtion for pigment ratios (not an issue b/c of multiple starts) 
4. results
    1. collate and plot the final pigment:chla ratios for each taxon in each run vs RMS residuals of Chl a. Example plot [TODO](ln_here).
        1. units of ug/L taxa-contributed-chlorophyll per sample (percent chl contribution * net chl contribution) 
        1. allows user to check robustness of the convergence
        2. allows user to check if there is “flip-flopping”, i.e. taxa w/ similar pigments effectively swapping identities bc the randomisation process has made the starting ratio for taxon A more like the actual ratio for taxon B than the starting point for taxon B.
            3. e.g. hapto 6 & 8 - they have eseentially the same ratios
        4. If results are not good, user can modify taxa community present or samples input.

## Other Links

TODO: CSRO code link & attrib

* R implementation of CHEMTAX [[1](https://github.com/MarPolar/CHEMTAX)], [[2](https://github.com/silviageor/chemtax)].
* [docs for R implementation included within the limSolve R library](https://www.rdocumentation.org/packages/limSolve/versions/1.5.6/topics/Chemtax)
* example .txt matricies used by oceanspace?](https://github.com/oceanspace/chemtax-tools) 
* (broken?) [chemtax google forum](http://groups.google.com/forum/#!forum/chemtax_users)

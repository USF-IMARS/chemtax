def guess_taxa_from_pigments(pigment_dataframe, taxa_list, pigment_exclude=[], matrix_init_seed=0): 
    """
    params:
    -------
    pigment_dataframe: pandas.DataFrame
        Pigments observed from samples. 
        One sample per row, one pigment per column.
        ???Samples rows are assumed to be from one water sample taken at a particular time & location.???
    taxa_list: iterable
        Taxa which may be present in the sample.
        Should be determined using domain knowledge about the location, season, time of day, and other environmental params.
    TODO: add the other params.
    
    returns:
    -------
    pandas.DataFrame of taxa occurrence estimates    

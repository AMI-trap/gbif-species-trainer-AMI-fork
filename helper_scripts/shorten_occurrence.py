import os
import pandas as pd
import sys
from collections import Counter

from dwca.read import DwCAReader
from dwca.descriptors import shorten_term
from dwca.darwincore.utils import qualname as qn

# Define variables
home_dir = os.path.dirname(os.getcwd())
# data_dir = "/Users/lbokeria/Documents/projects/gbif-species-trainer-data/"
data_dir = "/bask/projects/v/vjgo8416-amber/data/gbif-species-trainer-AMI-fork/"

family_name = "lepidoptera"

dwca_file_path       = os.path.join(data_dir,"dwca_files",family_name+".zip")
occurrence_file_path = os.path.join(data_dir,"dwca_files",family_name,"occurrence.txt")

# Remove the extra rows and compare the size
fields_to_keep = [
    "id",
    "decimalLatitude",
    "decimalLongitude",
    "order",
    "family",
    "genus",
    "species",
    "acceptedScientificName",
    "year",
    "month",
    "day",
    "datasetName",
    "taxonID",
    "acceptedTaxonKey",
    "lifeStage",
    "basisOfRecord",
]

print("Starting to read...")


# Read the occurrence.txt
kwargs = {}
with DwCAReader(dwca_file_path) as dwca:
    # Get the file descriptor
    datafile_descriptor = dwca.get_descriptor_for("occurrence.txt")
    
    kwargs['delimiter'] = datafile_descriptor.fields_terminated_by
    kwargs['skiprows'] = datafile_descriptor.lines_to_ignore
    kwargs['header'] = None
    kwargs['names'] = datafile_descriptor.short_headers
    kwargs['parse_dates'] = True
    kwargs['on_bad_lines'] = "skip"
    kwargs['usecols'] = fields_to_keep
    
    df1 = pd.read_csv(occurrence_file_path, **kwargs)
    
    # Add a column for default values, if present in the file descriptor
    for field in datafile_descriptor.fields:
        field_default_value = field['default']
        if field_default_value is not None:
            df1[shorten_term(field['term'])] = field_default_value

print("Finished reading!")

print(sys.getsizeof(df1)/1024/1024)
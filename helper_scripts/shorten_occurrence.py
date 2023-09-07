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

family_name_small = "Sesiidae"
family_name_big = "lepidoptera"

dwca_file_path_small = os.path.join(data_dir,"dwca_files",family_name_small+".zip")
dwca_file_path_big   = os.path.join(data_dir,"dwca_files",family_name_big+".zip")
occurrence_file_path = os.path.join(data_dir,"dwca_files",family_name_big,"occurrence.txt")

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

# Read the datafile descriptors for the smalle one
with DwCAReader(dwca_file_path_small) as dwca:
    # Get the file descriptor
    datafile_descriptor = dwca.get_descriptor_for("occurrence.txt")


# Read the occurrence.txt
kwargs = {}
        
kwargs['delimiter'] = datafile_descriptor.fields_terminated_by
kwargs['skiprows'] = datafile_descriptor.lines_to_ignore
kwargs['header'] = None
kwargs['names'] = datafile_descriptor.short_headers
kwargs['parse_dates'] = True
kwargs['on_bad_lines'] = "skip"
kwargs['usecols'] = fields_to_keep
kwargs['chunksize'] = 500000

occ_df = []

for chunk in pd.read_csv(occurrence_file_path, **kwargs):

    # Add a column for default values, if present in the file descriptor
    for field in datafile_descriptor.fields:
        field_default_value = field['default']
        if field_default_value is not None:
            chunk[shorten_term(field['term'])] = field_default_value


    occ_df.append(chunk)

occ_df = pd.concat(occ_df)
    
   
    # occ_df = pd.read_csv(occurrence_file_path, **kwargs)
    
    # # Add a column for default values, if present in the file descriptor
    # for field in datafile_descriptor.fields:
    #     field_default_value = field['default']
    #     if field_default_value is not None:
    #         occ_df[shorten_term(field['term'])] = field_default_value

print("Finished reading!")

print(sys.getsizeof(occ_df)/1024/1024)

# Now, save the DF
occ_df.to_csv(os.path.join(data_dir,"dwca_files","occurrence_"+family_name_big+"_chunks.csv"))
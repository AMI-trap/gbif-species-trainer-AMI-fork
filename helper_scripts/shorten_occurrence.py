import os
import pandas as pd
import sys
from collections import Counter

from dwca.read import DwCAReader
from dwca.darwincore.utils import qualname as qn

# Define variables
home_dir = os.path.dirname(os.getcwd())
data_dir = "/bask/projects/v/vjgo8416-amber/data/gbif-species-trainer-AMI-fork/"

family_name = "lepidoptera"

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

with DwCAReader(os.path.join(data_dir,"dwca_files",family_name+".zip")) as dwca:
    occ_df_usecols = dwca.pd_read("occurrence.txt", 
                                  parse_dates=True,
                                  on_bad_lines="skip",
                                  usecols = fields_to_keep)
    


print("Finished reading!")

print(sys.getsizeof(occ_df_usecols)/1024/1024)
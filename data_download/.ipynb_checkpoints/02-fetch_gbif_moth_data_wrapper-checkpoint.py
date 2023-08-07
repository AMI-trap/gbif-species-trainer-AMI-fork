#!/usr/bin/env python
# coding: utf-8

"""
Author	      : Levan Bokeria
Last modified : 07 Aug 2023
About	      : A wrapper file to fetch GBIF images for different taxonomic families
"""

import pygbif
from pygbif import occurrences as occ
from pygbif import species as species_api
from dwca.read import DwCAReader
import pandas as pd
import numpy as np
import os
import shutil
import tqdm
import urllib
import json
import math
import argparse
from multiprocessing import Pool

from fetch_gbif_moth_data_serial import download_data, fetch_image_data, fetch_meta_data

# If local mac
# write_directory_lists  = "/Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/data_download/"
# write_directory_images = "/Users/lbokeria/Documents/projects/gbif-species-trainer-data/gbif_images/try_wrapper/"
# species_list           = "/Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/data_download/uksi-macro-moths-drepanidae-sesiidae-keys.csv"
# dwca_directory         = "/Users/lbokeria/Documents/projects/gbif-species-trainer-data/dwca_files/"

# If on linux server
write_directory_lists  = "/bask/projects/v/vjgo8416-amber/projects/gbif-species-trainer-AMI-fork/data_download/"
write_directory_images = "/bask/projects/v/vjgo8416-amber/data/gbif-species-trainer-AMI-fork/gbif_images/try_wrapper/"
species_list           = "/bask/projects/v/vjgo8416-amber/projects/gbif-species-trainer-AMI-fork/data_download/uksi-macro-moths-keys.csv"
dwca_directory         = "/bask/projects/v/vjgo8416-amber/data/gbif-species-trainer-AMI-fork/dwca_files/"

# Read the main species list file
moth_data = pd.read_csv(species_list)

# Get all unique family names
all_families = set(moth_data["family_name"])

print(all_families)

for i_family in all_families:
    
    # Filter the moth_data
    i_moth_data = moth_data[moth_data["family_name"] == i_family]
    
    # Save the moth_data file
    i_moth_data.to_csv(os.path.join(write_directory_lists,i_family+".csv"),
                       index=False)
    print("Saved the " + i_family + " file.")
    
    # Call the code to download the data
    print("Calling the download code")

    from types import SimpleNamespace
    args = SimpleNamespace()

    args.write_directory = write_directory_images
    args.species_checklist = os.path.join(write_directory_lists,i_family+".csv")
    args.max_images_per_species = 2
    args.dwca_file = os.path.join(dwca_directory,i_family + ".zip")
    args.resume_session = "False"
    
    download_data(args)
    
    # Delete the moth_data file
    # print("Deleting the csv file")
    # os.remove(os.path.join(write_directory_lists,i_family + ".csv"))
    
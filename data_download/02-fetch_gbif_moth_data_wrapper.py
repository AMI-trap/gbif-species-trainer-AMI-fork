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


def start_family_loop(args):
    """"""

    write_directory_lists = args.write_directory_lists
    write_directory_images = args.write_directory_images
    species_list = args.species_checklist
    dwca_directory = args.dwca_directory
    max_images_per_species = args.max_images_per_species
    resume_session = args.resume_session
    family_name = args.family_name

    # Read the main species list file
    moth_data = pd.read_csv(species_list)

    # Filter the moth_data
    i_moth_data = moth_data[moth_data["family_name"] == family_name]

    # Save the moth_data file
    i_moth_data.to_csv(os.path.join(write_directory_lists, family_name+".csv"),
                       index=False)
    print("Saved the " + family_name + " file.")

    # Call the code to download the data
    print("Calling the download code")

    from types import SimpleNamespace

    args_download_data = SimpleNamespace()

    args_download_data.write_directory = write_directory_images

    args_download_data.species_checklist = os.path.join(
        write_directory_lists, family_name+".csv")

    args_download_data.max_images_per_species = max_images_per_species

    args_download_data.dwca_file = os.path.join(
        dwca_directory, family_name + ".zip")

    args_download_data.resume_session = resume_session

    download_data(args_download_data)

    # Delete the moth_data file
    # print("Deleting the csv file")
    # os.remove(os.path.join(write_directory_lists,family_name + ".csv"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write_directory_lists", help="path of the folder to save the split CSV files", required=True
    )
    parser.add_argument(
        "--write_directory_images", help="path of the folder to save the gbif images", required=True
    )
    parser.add_argument(
        "--dwca_directory", help="path of the folder with the darwin core archive zip files", required=True
    )
    parser.add_argument(
        "--species_checklist",
        help="path of csv file containing list of species names along with unique GBIF taxon keys",
        required=True,
    )
    parser.add_argument(
        "--family_name",
        help="Which family name(s) to download images for",
        required=True,
    )
    parser.add_argument(
        "--max_images_per_species",
        help="maximum number of images to download for any speices",
        default=500,
        type=int,
    )
    parser.add_argument(
        "--resume_session",
        help="False/True; whether resuming a previously stopped downloading session",
        required=True,
    )

    args = parser.parse_args()

    start_family_loop(args)

# %% [markdown]
# Attempting to load the occurrence dataframe and make it smaller by retaining just the necessary columns.

# %%
import os
import pandas as pd
import sys
from collections import Counter

from dwca.read import DwCAReader
from dwca.darwincore.utils import qualname as qn

# %%
home_dir = os.path.dirname(os.getcwd())
data_dir = "/Users/lbokeria/Documents/projects/gbif-species-trainer-data/"

family_name = "Sesiidae"

# %%

# %%
# Now read in chunks
with DwCAReader(os.path.join(data_dir,"dwca_files",family_name+".zip")) as dwca:
    occ_df_smaller = []
    for chunk in dwca.pd_read("occurrence.txt", chunksize=10):
        print("read the chunk now")
        print(chunk.shape)
        # occ_df_smaller.append(chunk[fields_to_keep])



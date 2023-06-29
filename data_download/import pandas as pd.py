import pandas as pd
import os
from dwca.read import DwCAReader

# filepath = '/Users/lbokeria/Downloads/'


# dwca = DwCAReader(os.path.join(filepath, '0033583-230530130749713.zip'))

# df = dwca.pd_read("occurrence.txt", parse_dates=True, on_bad_lines="skip")

# print(df['acceptedTaxonKey'])

# print('done')

# columns = [
#     "accepted_taxon_key",
#     "family_name",
#     "genus_name",
#     "search_species_name",
#     "gbif_species_name",
#     "image_count",
# ]

# datacount_file = pd.DataFrame(columns=columns, dtype=object)

# search_species = "phegea"

# if search_species not in datacount_file["search_species_name"].tolist():
#     print('Not here')


#########################
# Load an occurrence.txt file

filepath = '/Users/lbokeria/Downloads/'
dwca = DwCAReader(os.path.join(filepath, '0033583-230530130749713.zip'))

df = dwca.pd_read("occurrence.txt", parse_dates=True, on_bad_lines="skip")

print('whatever')

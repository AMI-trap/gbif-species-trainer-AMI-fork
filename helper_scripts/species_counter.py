from collections import Counter

from dwca.read import DwCAReader
from dwca.darwincore.utils import qualname as qn

with DwCAReader('/Users/lbokeria/Documents/projects/gbif-species-trainer-data/dwca_files/Sesiidae.zip') as dwca:
    count_species = Counter()

    print("starting to count...")

    for row in dwca:
        count_species.update([row.data[qn('scientificName')]])

    print(count_species)

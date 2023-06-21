import pandas as pd
import os
from dwca.read import DwCAReader

filepath = '/Users/lbokeria/Downloads/'


dwca = DwCAReader(os.path.join(filepath, '0033583-230530130749713.zip'))

df = dwca.pd_read("occurrence.txt", parse_dates=True, on_bad_lines="skip")

print(df['acceptedTaxonKey'])

print('done')

#!/usr/bin/env python
# coding: utf-8

import sys

sys.modules["fetch"] = __import__("02-fetch_gbif_moth_data_serial")

from fetch import download_data

print('something random')

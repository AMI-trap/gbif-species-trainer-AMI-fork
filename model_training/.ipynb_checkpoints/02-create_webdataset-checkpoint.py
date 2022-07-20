#!/usr/bin/env python
# coding: utf-8

"""
Author        : Aditya Jain
Date Started  : July 5, 2022
About         : Creates a webdataset
"""

import json
import os
import random

from PIL import Image
from torchvision import transforms
import PIL
import numpy as np
import pandas as pd
import torch
import webdataset as wds
import argparse

def set_random_seed(random_seed):
	"""set random seed for reproducibility"""
	random.seed(random_seed)
	np.random.seed(random_seed)
	torch.manual_seed(random_seed)
	torch.cuda.manual_seed(random_seed)
	torch.backends.cudnn.deterministic = True


def create_webdataset(args):
	"""main function for creating webdataset"""
	
	dataset_dir       = args.dataset_dir
	dataset_filepath  = args.dataset_filepath
	label_filepath    = args.label_filepath
	img_resize        = args.image_resize
	webdataset_patern = args.webdataset_patern
	max_shard_size    = args.max_shard_size
	random_seed       = args.random_seed

	set_random_seed(random_seed)

	dataset_df = pd.read_csv(dataset_filepath)
	dataset_df = dataset_df.sample(frac=1)
	label_list = json.load(open(label_filepath))

	transformer = transforms.Compose([
					transforms.Resize((img_resize, img_resize))])

	sink        = wds.ShardWriter(webdataset_patern, max_shard_size)
	corrupt_img = 0

	for _, row in dataset_df.iterrows():
		image_path = dataset_dir + row['family'] + '/' + row['genus'] + '/' + row['species'] + '/' + row['filename'] 

		if not os.path.isfile(image_path):
			print(f'File {image_path} not found')
			continue
        
		# check issue with image opening; completely corrupted
		try:
			image = Image.open(image_path)
			image = image.convert('RGB')
		except PIL.UnidentifiedImageError:
			print(f'Unidentified Image Error on file {image_path}')
			corrupt_img += 1
			continue
		except OSError:
			print(f'OSError Error on file {image_path}')
			corrupt_img += 1
			continue    
        
		# check for partial image corruption
		try:
			image = transformer(image) 
		except:
			print(f'Partial corruption of file {image_path}')
			corrupt_img += 1
			continue    
    
		fpath        = row['family'] + '/' + row['genus'] + '/' + row['species'] + '/' + row['filename']
		fpath        = os.path.splitext(fpath)[0].lower()
    
		species_list = label_list['species_list']
		label        = row['species']    
		label        = species_list.index(label)
        
		sample = {
		  '__key__': fpath,
		  'jpg': image,
		  'cls': label
		}

		sink.write(sample)  
    
	sink.close()
	print(f'Total corrupted images are: {corrupt_img}')

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--dataset_dir', help = 'dataset directory containing the gbif data', required=True)
	parser.add_argument('--dataset_filepath', help = 'file path containing every data point information', required=True)
	parser.add_argument('--label_filepath', help = 'file path containing numerical label information', required=True)
	parser.add_argument('--image_resize', help = 'resizing image to (size x size)', required=True, type=int)
	parser.add_argument('--webdataset_patern', help = 'path and type to save the webdataset', required=True)
	parser.add_argument('--max_shard_size', help = 'the maximum shard size', default=100*1024*1024, type=int)
	parser.add_argument('--random_seed', help = 'random seed for reproducible experiments', default=42, type=int)
	args   = parser.parse_args()
	
	create_webdataset(args)
	
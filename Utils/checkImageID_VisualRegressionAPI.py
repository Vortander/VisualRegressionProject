# coding: utf-8

# ABOUT: Check images associated with an point ID. 
# For now, requires a list with id and point info, an point ID, and a path_to_images (name has to be <lat_lon_camview.jpg>)

# Change sys.path.append with your APIs (e.g. GridMapAPI, VisualRegressionAPI) path.
import sys
sys.path.append('/home/virginia/scripts/APIs/')

import VisualRegressionAPI.Datasets as datasets
import VisualRegressionAPI.utils as visutils
from VisualRegressionAPI.Datasets import StreetImages

import numpy as np

import torch
from torch.utils.data import DataLoader
from torchvision import utils

import matplotlib.pyplot as plt

if len(sys.argv) < 4:

	print("**************************************************************************************************")
	print("Usage: ")
	print("python checkImageID_VisualRegressionAPI.py [point_ID] [path/point_list] [path/images]")
	print("**************************************************************************************************")

	quit()

else:

	idx = sys.argv[1]
	point_list = sys.argv[2]
	image_path = sys.argv[3]

	batch_groups = datasets.get_point_by_id(point_list, idx)
	if len(batch_groups) > 0: 
		image_info = batch_groups[0]

		print("ID: ", image_info[0])
		print("Cell Location: ", image_info[1])
		print("Latitude: ", image_info[2])
		print("Longitude: ", image_info[3])
		print("True Value: ", image_info[4])

		batch_size = len(batch_groups)

		imagedata = StreetImages( batch_groups, image_path, camera_views=['0','90','180','270'], resize=True, imgsize=(227, 227) )
		dataloader = DataLoader( imagedata, batch_size=batch_size, shuffle=True, num_workers=8 )
		dataiter = iter(dataloader)
		example_batch = next(dataiter)

		plt.figure(figsize = (20,20))
		concatenated = torch.cat(example_batch['image'], 0)
		visutils.imshow(utils.make_grid(concatenated, nrow=4, padding=4))
	else:
		print("ID " + sys.argv[1] + " not found in " + sys.argv[2])

# coding: utf-8

# Change sys.path.append with your APIs (e.g. GridMapAPI, VisualRegressionAPI) path.
import sys
sys.path.append('/home/virginia/scripts/APIs/')

import VisualRegressionAPI.Datasets as datasets
import VisualRegressionAPI.utils as visutils
import VisualRegressionAPI.ConvNets as convnets
from VisualRegressionAPI.Datasets import StreetImages


#convnets.Net(self, architecture='alexnet', dataset='ImageNet', load_weights=True, frozen=True, remove_last_layer=False):
alexnet = convnets.Net('alexnet', dataset='Places', load_weights=True, frozen=True)
print(alexnet)


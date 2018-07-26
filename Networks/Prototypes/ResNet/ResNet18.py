# coding: utf-8

# Change sys.path.append with your APIs (e.g. GridMapAPI, VisualRegressionAPI) path.
import sys
sys.path.append('/home/virginia/scripts/APIs/')

import VisualRegressionAPI.Datasets as datasets
import VisualRegressionAPI.utils as visutils
import VisualRegressionAPI.PrototypeNetworks as prototypes
from VisualRegressionAPI.Datasets import StreetImages

architectures = {'ResNet':['18','34','50','101','152']}

resnet18 = prototypes.Net('ResNet', '18', load_weights=True, frozen=True, remove_last_layer=True)
print(resnet18)
# coding: utf-8

# Change sys.path.append with your APIs (e.g. GridMapAPI, VisualRegressionAPI) path.
import sys
sys.path.append('/home/virginia/scripts/APIs/')

import VisualRegressionAPI.utils as utils

#def check_images_DB( sourcepath, schema_name, city_table_name, dbname, user, imgtype='Street', camera_views=['0', '90', '180', '270'], ext='.jpg' ):
#utils.check_images_DB('/mnt/dataWD1/virginia/StreetImages/RioDeJaneiro/StreetView/images', 'citypoints', 'riodejaneiro', 'virginia', 'virginia', imgtype='Street', camera_views=['0', '90', '180', '270'], ext='.jpg', set_visited_no=True )
#utils.check_images_DB('/mnt/dataWD1/virginia/StreetImages/SaoPaulo/Satellite', 'citypoints', 'saopaulo', 'virginia', 'virginia', imgtype='Sat', camera_views=['19', '20', '21', '22'], ext='.png', set_visited_no=True )
#utils.check_images_DB('/mnt/dataWD1/virginia/StreetImages/SaoPaulo/StreetView/images', 'citypoints', 'saopaulo', 'virginia', 'virginia')

utils.check_images_DB('/mnt/dataWD1/virginia/StreetImages/RioDeJaneiro/Satellite', 'citypoints', 'riodejaneiro', 'virginia', 'virginia', imgtype='Sat', camera_views=['21'], ext='.png', set_visited_no=False )


#### importing libraries ####
import sys
import os
from qgis.utils import *
from qgis.core import *

#### These are the only variable that need to be changed ####
#### The remaining code referenced these definitions     ####
myProject = 'c:your\\project\\location.qgs'
layoutName = 'atlas_name'
atlasFilter = 'filter = query' # Use '' if no filter needed, otherwise e.g. '\"FeatureType\" = \'building\''
exportFormat = 'image' #'image' or 'pdf'
imageOutputName = '@atlas_featurenumber' #e.g.\"Parish\" || \' \' || \"Number\" where parish and number are columns
imageDPI = 200
imageExtension = '.jpg'
pdfOutputPath = 'c:your\\output\\location.pdf'
imageOutputFolder = 'c:your\\project\\folder\\'

#### Defining map path and contents ####
QgsProject.instance().read(myProject)
myLayout = QgsProject.instance().layoutManager().layoutByName(layoutName)
myAtlas = myLayout.atlas()
myAtlasMap = myAtlas.layout()

#### atlas query ####
myAtlas.setFilterFeatures(True) 
myAtlas.setFilterExpression(atlasFilter)

#### image output name ####
myAtlas.setFilenameExpression( imageOutputName )

#### image and pdf settings ####
pdf_settings=QgsLayoutExporter(myAtlasMap).PdfExportSettings()
image_settings = QgsLayoutExporter(myAtlasMap).ImageExportSettings()
image_settings.dpi = imageDPI

#### Export images or PDF (depending on flag) ####

if exportFormat == "image":
    for myLayout in QgsProject.instance().layoutManager().printLayouts():
        if myAtlas.enabled():
            result, error = QgsLayoutExporter.exportToImage(myAtlas, 
                                baseFilePath=imageOutputFolder, extension=imageExtension, settings=image_settings)
            if not result == QgsLayoutExporter.Success:
                print(error)
if exportFormat == "pdf":
    for myLayout in QgsProject.instance().layoutManager().printLayouts():
        if myAtlas.enabled():
            result, error = QgsLayoutExporter.exportToPdf(myAtlas, pdfOutputPath, settings=pdf_settings)
            if not result == QgsLayoutExporter.Success:
                print(error)

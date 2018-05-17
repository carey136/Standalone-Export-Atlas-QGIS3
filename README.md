# Standalone-Export-Atlas-QGIS3
#### This code is to be used as an example to export a QGIS atlas layout (or sections of one) from a QGIS template using a stand-alone python script.
### Version information/requirements:
* QGIS 3.0.2
* QGIS API (python 3.6)
* Probably OSGeo4W64 (for running outside of QGIS, when this works correctly)


#### Currently the script only functions correctly while the QGIS application is open

```python
#### importing libraries ####
import sys
import os
from qgis.utils import *
from qgis.core import *

#### These are the only variable that need to be changed ####
#### The remaining code referenced these definitions     ####
myProject = 'C:\\Temp\\py\\PYROW_3.qgs'
layoutName = 'A4_Atlas'
atlasFilter = '\"parishcode\" = 207'
exportFormat = 'image'
imageOutputName = '\"PC_name\" || \' \' || \"NUMBER_\"'
imageDPI = 200
imageExtension = '.jpg'
pdfOutputPath = 'C:\\Temp\\py\\output\\CyclicalSurvey.pdf'
imageOutputFolder = 'C:\\Temp\\py\\output\\'

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
```

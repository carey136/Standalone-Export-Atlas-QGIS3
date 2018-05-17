# Standalone-Export-Atlas-QGIS3
#### This code is to be used as an example to export a QGIS atlas layout (or sections of one) from a QGIS template using a stand-alone python script.
### Version information/requirements:
* QGIS 3.0.2
* QGIS API (python 3.6)
* Probably OSGeo4W64 (for running outside of QGIS)


#### Currently the script only functions correctly while the QGIS application is open

```python
####importing libraries
import sys
import os
from qgis.PyQt.QtXml import QDomDocument
from qgis.utils import *
from qgis.core import *
####Defining template (.qpt) and map (.qgs) locations
myFile = os.path.join('C:\Temp\py', "template_3.qpt")
myProject = os.path.join('C:\Temp\py', "PYROW_3.qgs")

#Can I define myLayout (line 16) without loading the project?
QgsProject.instance().read(myProject)
myTemplateFile = open(myFile, 'rt') 
myTemplateContent = myTemplateFile.read() 
myTemplateFile.close() 
myDocument = QDomDocument() 
myDocument.setContent(myTemplateContent) 
myLayout = QgsProject.instance().layoutManager().layoutByName('A4_Atlas')
myLayout.loadFromTemplate(myDocument,QgsReadWriteContext()) 

####Setup Atlas 
myAtlas = myLayout.atlas()
myAtlasMap = myAtlas.layout()
CoverLayer = QgsProject.instance().mapLayersByName('ROW buffer')[0]
myAtlas.setCoverageLayer(CoverLayer) 
myMap = myAtlasMap.referenceMap()
myMap.setAtlasDriven(True)
myMap.setAtlasScalingMode(myMap.Auto)

####Atlas Query
myAtlas.setFilterFeatures(True) 
myAtlas.setFilterExpression(" ""parishcode"" = 207")

####PDF data
exporter = QgsLayoutExporter(myAtlasMap)
#exporter.exportToPdf("C://Temp//py//output//", QgsLayoutExporter.PdfExportSettings() )

####image output name
outputname = '\"NUMBER_\" || \' ROWTEST\''
myAtlas.setFilenameExpression( outputname )

####image and Pdf settings
pdf_settings=exporter.PdfExportSettings()
image_settings = exporter.ImageExportSettings()
image_settings.dpi = 200

####Export PDF map book
for myLayout in QgsProject.instance().layoutManager().printLayouts():
    if myAtlas.enabled():
        result, error = QgsLayoutExporter.exportToPdf(myAtlas,'C:/Temp/py/output/207_external.pdf', settings=pdf_settings)
        if not result == QgsLayoutExporter.Success:
            print(error)
```

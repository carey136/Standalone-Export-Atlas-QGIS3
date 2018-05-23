#### importing libraries ####
import sys
import os
from os.path import expanduser
from qgis.utils import *
from qgis.core import *
from PyQt5.QtCore import QFileInfo
from PyQt5.QtWidgets import QApplication

####      Hardcode variables here      ####
#### Or use flags to override defaults ####


# -P = Project file
myProject = 'c:your\\project\\location.qgs'

# -L = Layout ("Layout name")
layoutName = 'atlas_name'

# -C = Coverage Layer Name ("Layer Name")
coverageLayer = 'Layer_name'

# -F = filter ("column" "operator" "value")
atlasFilter = '"column" = "value"'

# -O = Output Format (pdf or image)
outputFormat = 'pdf'

# -D = Output Directory ("c:your\output" - exclude trailing "\")
outputFolder = 'c:your\project\folder'

# -N = Image output Query
outputName = '@atlas_featurenumber' #e.g.\"Parish\" || \' \' || \"Number\" where parish and number are columns

# -Q = PDF Name
pdfName = 'Export'


#### Setting variables using flags ####
if("-P" in sys.argv):
    myProject = sys.argv[sys.argv.index("-P") + 1]
if("-L" in sys.argv):
    layoutName = sys.argv[sys.argv.index("-L") + 1]
if("-C" in sys.argv):
    coverageLayer = sys.argv[sys.argv.index("-C") + 1]
if("-F" in sys.argv):
    atlasFilter = "\"" + sys.argv[sys.argv.index("-F") + 1] + "\" " + sys.argv[sys.argv.index("-F") + 2] + " \'" + sys.argv[sys.argv.index("-F") + 3] + "\'"
if("-O" in sys.argv):
    outputFormat = sys.argv[sys.argv.index("-O") + 1]
if("-D" in sys.argv):
    outputFolder = sys.argv[sys.argv.index("-D") + 1]
if("-N" in sys.argv):
    outputName = sys.argv[sys.argv.index("-N") + 1]
if("-Q" in sys.argv):
    pdfName = sys.argv[sys.argv.index("-Q") + 1]

#### Initialising QGIS in back end (utilising users temp folder) ####
home = expanduser("~")
QgsApplication( [], False, home + "/AppData/Local/Temp" )
QgsApplication.setPrefixPath("C:/OSGeo4W64/apps/qgis", True) #Change path for standalone QGIS install
app = QApplication([])
QgsApplication.initQgis()

#### Defining map path and contents ####
QgsProject.instance().read(myProject)
myLayout = QgsProject.instance().layoutManager().layoutByName(layoutName)
myAtlas = myLayout.atlas()
myAtlasMap = myAtlas.layout()

#### atlas query ####
if(coverageLayer in locals()):
    myAtlas.setCoverageLayer(QgsProject.instance().mapLayersByName(coverageLayer))
myAtlas.setFilterFeatures(True) 
myAtlas.setFilterExpression(atlasFilter)

#### image output name ####
myAtlas.setFilenameExpression( outputName )

#### image and pdf settings ####
pdf_settings=QgsLayoutExporter(myAtlasMap).PdfExportSettings()
image_settings = QgsLayoutExporter(myAtlasMap).ImageExportSettings()
image_settings.dpi = 200
imageExtension = '.jpg'
#### Export images or PDF (depending on flag) ####
if outputFormat == "image":
    for myLayout in QgsProject.instance().layoutManager().printLayouts():
        if myAtlas.enabled():
            result, error = QgsLayoutExporter.exportToImage(myAtlas, 
                                baseFilePath=outputFolder + '\\', extension=imageExtension, settings=image_settings)
            if not result == QgsLayoutExporter.Success:
                print(error)
if outputFormat == "pdf":
    for myLayout in QgsProject.instance().layoutManager().printLayouts():
        if myAtlas.enabled():
            result, error = QgsLayoutExporter.exportToPdf(myAtlas, outputFolder + '\\' + pdfName + '.pdf', settings=pdf_settings)
            if not result == QgsLayoutExporter.Success:
                print(error)
print("Success!")

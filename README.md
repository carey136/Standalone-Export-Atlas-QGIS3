# Standalone-Export-Atlas-QGIS3
### This code exports a chosen atlas print layout from a QGS file using a stand-alone python script. The output can either be a multi-page PDF or a set of images.
## Version information/requirements:
* Windows 10 64x (untested on Windows 7 or earlier)
* QGIS 3.0.+ (preferably installed through OSGeo4W*)
* QGIS API (python 3.6 - usually installed with QGIS/default install through OSGeo4W)
* A QGIS file fully set up for atlas exports

 *The script makes use of ‪python-qgis.bat from the OSGeo4W bin directory (default ‪C:\OSGeo4W64\bin\python-qgis.bat).

## To run the script in command line:

### 1. Open AtlasExport.py in a syntax highlighting text editor
### 2. Change the 8 variables as required and save the file:

```python
myProject = "c:your\\project\\location.qgs"
layoutName = "atlas_name"
coverageLayer = "Layer_name"
atlasFilter = '"column" = "value"'
outputFormat = "pdf"
outputFolder = "c:your\project\folder"
outputName = "query producing unique value"
pdfName = "Export"
```
#### myProject (override with flag ``` -P "project path" ```)
The project file path in the following format: For example ``` "c:your\project\location.qgs" ```
#### layoutName (override with flag ``` -L "atlas_name" ```)
The name of layout set up for atlas exporting: For example ``` "Atlas_A4" ```
#### coverageLayer (override with flag ``` -C "layer_name" ```)
The name of the coverage layer used in the project file. This is derived from the layer name as displayed in the map's table of contents (and can contain spaces). Wrap the name in quotation marks: for example ``` "Rights of Way" ```
#### atlasFilter (override with flag ``` -F "layer_name" "operator" "values" ```)
* If you require a subset of your coverage layer to be exported (rather than the entire layer's worth of maps), type in a valid filter while escaping any quotes. e.g.``` '\"FeatureType\" = \'building\'' ```
* If you do not want to filter the coverage layer, instead use ``` '' ```
* If you want to override the hardcoded filter using the ``` '-F' ``` flag
    * use the flag -F followed by a space
    1. Column Name, wrapped in quotes e.g. ``` "Road_Type" ```
    2. Operator, wrapped in quotes e.g. ``` "=" ``` ``` "<>" ``` ``` ">" ``` ``` "<" ``` ``` "LIKE" ```
    3. Value, wrapped in quotes e.g. ``` "A Road" ```
    * A full query might look like the following: ``` -F "Road_Type" "=" "A Road" ```
#### outputFormat (override with flag ``` -O "Format" ```)
 ```"image" ``` or ``` "pdf" ``` - "image" produces multiple image files, "pdf" produces a multi-page pdf
#### outputFolder (override with flag ``` -D "directory" ```)
The output folder in the following format ``` "c:your\project\folder" ```
#### outputName (override with flag ``` -N "name query" ```)
The output name for to create names derived from attributes: For example ``` \"Parish\" || \' \' || \"Number\" ``` or simply ``` "@atlas_featurenid ```
#### pdfName (override with flag ``` -N "name" ```)
The output pdf name in the following format ``` "name" ```
### 3. open command line and type the following:
``` "C:\OSGeo4W64\bin\python-qgis.bat" "c:your\\script\\location\\AtlasExport.py" ```
* ``` "C:\OSGeo4W64\bin\python-qgis.bat" ``` is the default path for OSGeo4W's batch file. It executes several other batch files, loading the environment for python 3.6 to run with QGIS libraries
* ``` "c:your\\script\\location\\AtlasExport.py" ``` Is the location of the python file on your machine

The script will now output the images of PDFs to the location noted in the script. If you encounter any errors, the explicit reason will be displayed in command line allowing you to troubleshoot.

## Flags / Overrides examples
These can be used to change many input and output parameters without modifying the code. Below is an exmaples in action:
C:\OSGeo4W64\bin\python-qgis.bat C:\Temp\py\pyrow2.py -F "parishcode" "=" "207" -O image -D "C:\Users\Guy\Desktop"
* Flag -F changes the atlas query (dataset contains 3000 features, filtered set contains 7)
* Flag -O changes the output to images (from the default multi-page pdf)
* Flag -D overrides the output location to the desktop


## To run as a batch file
* Copy the code executed in the commandline in step 3 into a batch file: ``` "C:\OSGeo4W64\bin\python-qgis.bat" "c:your\\script\\location\\AtlasExport.py" ```
* Add any extra flags as needed
* Double click the file to run the script

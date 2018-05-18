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
### 2. Change the 9 variables as required and save the file:

```python
myProject = 'c:your\\project\\location.qgs'
layoutName = 'atlas_name'
atlasFilter = 'filter = query' # Use '' if no filter needed, otherwise e.g. '\"FeatureType\" = \'building\''
exportFormat = 'image' #'image' or 'pdf'
imageOutputName = 'query producing unique value' #e.g.\"Parish\" || \' \' || \"Number\" where parish and number are columns
imageDPI = 200
imageExtension = '.jpg'
pdfOutputPath = 'c:your\\output\\location.pdf'
imageOutputFolder = 'c:your\\project\\folder\\'
```
#### myProject
The project file path in the following format: ``` 'c:your\\project\\location.qgs' ```
#### layoutName
The name of layout set up for atlas exporting
#### atlasFilter
* If you require a subset of your coverage layer to be exported (rather than the entire layer's worth of maps), type in a valid filter while escaping any quotes. e.g.``` '\"FeatureType\" = \'building\'' ```
* If you do not want to filter the coverage layer, instead use ``` '' ```
#### exportFormat
 ```'image' ``` or ``` 'pdf' ``` - 'image' produces multiple image files, 'pdf' produces a multi-page pdf
#### imageDPI
The output resolution when using an image output
#### imageExtension
The output image type (support many types). Common types include ```'.jpg'``` ```'.png'``` ```'.tif'```
#### pdfOutputPath
The output file path in the following format ```'c:your\\output\\location.pdf'```
#### imageOutputFolder
The output path in the following format ```'c:your\\project\\folder\\'```
### 3. open command line and type the following:
``` "C:\OSGeo4W64\bin\python-qgis.bat" "c:your\\script\\location\\AtlasExport.py" ```
* ``` "C:\OSGeo4W64\bin\python-qgis.bat" ``` is the default path for OSGeo4W's batch file. It executes several other batch files, loading the environment for python 3.6 to run with QGIS libraries
* ``` "c:your\\script\\location\\AtlasExport.py" ``` Is the location of the python file on your machine

The script will now output the images of PDFs to the location noted in the script. If you encounter any errors, the explicit reason will be displayed in command line allowing you to troubleshoot.

## To run as a batch file
* Copy the code executed in the commandline in step 3 into a batch file: ``` "C:\OSGeo4W64\bin\python-qgis.bat" "c:your\\script\\location\\AtlasExport.py" ```
* Double click the file to run the script

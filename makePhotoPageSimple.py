#Resizes an image and keeps aspect ratio. Set mywidth to the desired with in pixels.

import PIL
from PIL import Image
import os

insertLine=15

def addToMain(baseName, outName, mainLineList):
	mainLineList.insert(insertLine, '    </div>\n')
	mainLineList.insert(insertLine, '        <a href = "' + outName + '"><img src="files/thumbnails/' + baseName + '_thumbnail.png"></a>\n')
	mainLineList.insert(insertLine, '    <div class="frame">\n')
	return(mainLineList)

iPath = "./files/images"
oPath = "./photoPages/"

#get the gallery page
galleryName = './gallery.html'
mainFile = open(galleryName, 'r')
mainLineList = mainFile.readlines()
mainFile.close

for root, dirs, files in os.walk(iPath):
	for name in files:
		baseName = name[:-10]

		outName = "files/images" + name
		if(not os.path.exists(outName)):
			mainLineList = addToMain(baseName, outName, mainLineList)


mainFile = open(galleryName, 'w')
#for line in mainLineList:
#	print(line)
mainFile.writelines(mainLineList)
mainFile.close()

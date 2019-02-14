from Preprocessing.imageconverter import ImageConverter

with open("setup.config",'r') as setupfile:
    mypath = setupfile.read()

imageConverter = ImageConverter(mypath)
imageConverter.convertToGrayScale()
imageConverter.add_noise()
imageConverter.addBlur()
imageConverter.de_noise()
imageConverter.deblurring()
imageConverter.normalizeImages()
imageConverter.imageSegmentation()
images=imageConverter.imageToVector()


print(images)

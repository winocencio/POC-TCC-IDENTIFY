import cv2
import glob
from ParametersClassifier import ParametersClassifier , getParametrosVariados
from Log import Log


cascadeVersion = '0.4.014'
images_path = [img for img in glob.glob("img/original/I-1*")]
images_name = [img[13:-4] for img in images_path]

# parameters_classifier = ParametersClassifier(1.1,1,(30,30),(40,40),0)
classifier = cv2.CascadeClassifier('haarcascadeXml/cascadeV' + cascadeVersion + '.xml')

for parameters_classifier in getParametrosVariados():
    index = 0  
    for image_i in images_path:

        image = cv2.imread(image_i)
        imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        deteccoes = classifier.detectMultiScale(imageGray, **parameters_classifier.getDict())

        for (x,y,l,a) in deteccoes:
            center = (x + l//2, y + a//2)
            cv2.ellipse(image, center, (l//2, a//2), 0, 0, 360, (255, 0, 255), 2)

        log = Log(images_name[index],cascadeVersion,parameters_classifier,len(deteccoes),deteccoes)
        log.logar()

        cv2.imwrite( "img/resultados/" + images_name[index] + "-F/" + images_name[index] +"-Log-" + str(log.id) +  "-.jpg", image)
        index+= 1

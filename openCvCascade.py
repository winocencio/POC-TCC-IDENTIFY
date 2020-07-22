import cv2
import glob
from ParametersClassifier import ParametersClassifier
from Log import Log


cascadeVersion = '0.3.2'
images_name = [img for img in glob.glob("img/original/imagem*")]

for image_i in images_name:

    # log = new Log(image_i,cascadeVersion,)

    image = cv2.imread(image_i)
    classifier = cv2.CascadeClassifier('haarcascadeXml/cascadeV' + cascadeVersion + '.xml')
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #{'minSize':(30,30),'maxSize':(40,40),'scaleFactor':1.1,'minNeighbors':1}
    deteccoes = classifier.detectMultiScale(imageGray, minSize=(30,30),maxSize=(40,40),scaleFactor=1.1,minNeighbors=1)

    for (x,y,l,a) in deteccoes:
        center = (x + l//2, y + a//2)
        cv2.ellipse(image, center, (l//2, a//2), 0, 0, 360, (255, 0, 255), 2)
        # cv2.rectangle(image, (x,y), (x + l , y + a), (0,255,0),2)

    qtdDetectados = str(len(deteccoes)) + 'Detectados'
    print(qtdDetectados)

    cv2.imwrite( "img/resultados/V" + cascadeVersion +"-" + qtdDetectados +  ".jpg", image )
    cv2.waitKey(0)
    cv2.destroyAllWindows()
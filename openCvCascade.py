import cv2
import glob

cascadeVersion = '0.3.2'
images_name = [img for img in glob.glob("img/original/imagem*")]

for image_i in images_name:

    image = cv2.imread(image_i)
    classifier = cv2.CascadeClassifier('haarcascadeXml/cascadeV' + cascadeVersion + '.xml')
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    deteccoes = classifier.detectMultiScale(imageGray)

    for (x,y,l,a) in deteccoes:
        cv2.rectangle(image, (x,y), (x + l , y + a), (0,255,0),2)

    qtdDetectados = str(len(deteccoes)) + 'Detectados'
    print(qtdDetectados)

    cv2.imwrite( "img/resultados/V" + cascadeVersion +"-" + qtdDetectados +  ".jpg", image )
    cv2.waitKey(0)
    cv2.destroyAllWindows()
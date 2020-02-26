import cv2

image = cv2.imread('img/imagem.jpg')
cascadeVersion = '0.2.1'

classifier = cv2.CascadeClassifier('haarcascadeXml/cascadeV' + cascadeVersion + '.xml')
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

deteccoes = classifier.detectMultiScale(imageGray)

for (x,y,l,a) in deteccoes:
    cv2.rectangle(image, (x,y), (x + l , y + a), (0,255,0),2)

qtdDetectados = str(len(deteccoes)) + 'Detectados'
print(qtdDetectados)

cv2.imwrite( "img/V" + cascadeVersion +"-" +qtdDetectados+".jpg", image )
cv2.waitKey(0)
cv2.destroyAllWindows()
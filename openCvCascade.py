import cv2
import glob
from ParametersClassifier import ParametersClassifier , getParametrosVariados
from Log import Log
import json
from json import JSONEncoder
import numpy

cascadeVersion = '0.4.014'
images_path = [img for img in glob.glob("img/original/I-2*")]
images_name = [img[13:-4] for img in images_path]

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

CONST_PATH_JSON = 'log.json'
# parameters_classifier = ParametersClassifier(1.1,1,(30,30),(40,40),0)
classifier = cv2.CascadeClassifier('haarcascadeXml/cascadeV' + cascadeVersion + '.xml')
countParameters = 0

with open(CONST_PATH_JSON, 'r') as f:
    json_f = json.load(f)
    countParameters = json_f[-1]['id']+1
    f.close()

for parameters_classifier in getParametrosVariados():
    index = 0  
    for image_i in images_path:

        log = Log(countParameters,images_name[index],cascadeVersion,parameters_classifier)

        image = cv2.imread(image_i)
        imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        deteccoes = classifier.detectMultiScale(imageGray, **parameters_classifier.getDict())

        for (x,y,l,a) in deteccoes:
            center = (x + l//2, y + a//2)
            cv2.ellipse(image, center, (l//2, a//2), 0, 0, 360, (255, 0, 255), 2)

        cv2.imwrite( "img/resultados/" + images_name[index] + "-F/" + images_name[index] +"-Log-" + str(log.id) +  "-.jpg", image)
        log.setDetecoes(deteccoes)
        log.logar()
        json_f.append(log.__dict__)

        index+= 1
    countParameters+=1

with open(CONST_PATH_JSON,'w') as f:
    f.write(json.dumps(json_f,indent=4,cls=NumpyArrayEncoder))
    f.close()



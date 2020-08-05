import json
from datetime import datetime 
import numpy
class Log:

    def __init__(self,id,name_image,version_cascade,parameters_classifier):
        self.id = id
        self.name_image = name_image
        self.version_cascade=version_cascade
        self.parameters_classifier= json.dumps(parameters_classifier.getDict())
        self.elapsed_time = datetime.now()

    def logar(self):
        self.elapsed_time = str(datetime.now() - self.elapsed_time)
        self.printLog()

    def setDetecoes(self,indexes_objects):
        self.info_extracted=len(indexes_objects)
        self.indexes_objects= numpy.array(indexes_objects)

    def printLog(self):
        print('id: {0} , image: {1} , version_cascade: {2} , info_qtd: {3} , elapsed_time: {4} , parameters: {5}'.format(self.id,self.name_image,self.version_cascade,self.info_extracted,self.elapsed_time,self.parameters_classifier))


import json
from json import JSONEncoder
import numpy
from datetime import datetime 
CONST_PATH_JSON = 'log.json'
class Log:

    def __init__(self,name_image,version_cascade,parameters_classifier,info_extracted,indexes_objects):
        self.id = 0
        self.name_image = name_image
        self.version_cascade=version_cascade
        self.parameters_classifier= json.dumps(parameters_classifier.getDict())
        self.info_extracted=info_extracted
        self.indexes_objects= numpy.array(indexes_objects)
        self.elapsed_time = datetime.now()
        self.loadId()

    def loadId(self):
        with open(CONST_PATH_JSON, 'r') as f:
            json_f = json.load(f)
            self.id = json_f[-1]['id']+1
            f.close()

    def logar(self):
        self.elapsed_time = str(datetime.now() - self.elapsed_time)
        with open(CONST_PATH_JSON,'r') as f:
            json_f = json.load(f)
            f.close()

        with open(CONST_PATH_JSON,'w') as f:
            json_f.append(self.__dict__)
            f.write(json.dumps(json_f,indent=4, cls=NumpyArrayEncoder))
            f.close()

        self.printLog()

    def printLog(self):
        print('id: {0} , image: {1} , version_cascade: {2} , info_qtd: {3} , elapsed_time: {4}'.format(self.id,self.name_image,self.version_cascade,self.info_extracted,self.elapsed_time))

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)
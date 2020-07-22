
class ParametersClassifier:

    def __init__(self,scaleFactor,minNeighbors,minSize,maxSize,flags):
        self.scaleFactor = scaleFactor
        self.minNeighbors=minNeighbors
        self.flags=flags
        self.minSize=minSize
        self.maxSize=maxSize

    def getDict(self):
        return self.__dict__

def getParametrosVariados():
    scaleFactorList = ['0.8','0.9','1.0','1.1','1.2','1.3','1.4','1.5']
    minNeighborsList = ['0','1','2','3','4','5']
    minSizeList = ['(0,0)','(10,10)','(15,15)','(20,20)','(25,25)','(30,30)']
    maxSizeList = ['(30,30)','(35,35)','(40,40)','(45,45)','(50,50)','(60,60)']
    flagsList = ['0']

    returnList = []
    for scaleFactor in scaleFactorList:
        for minNeighbors in minNeighborsList:
            for minSize in minSizeList:
                for maxSize in maxSizeList:
                    for flags in flagsList:
                        returnList.append( ParametersClassifier(scaleFactor,minNeighbors,minSize,maxSize,flags))
    return returnList

getParametrosVariados()

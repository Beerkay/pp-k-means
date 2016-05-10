from random import *
from math import *
import sys
import os

def datagen(numProcs=5, numClusters=4, numPoints=10, dim=1):
    data = []
    dataRange = 1000
    for cluster in range(numClusters):
        procData = []
        mean = [randint(1,dataRange) for i in range(dim)]
        print mean
        var = sqrt(dim)*dataRange
        variance = lambda : triangular(0.5*var, 1.5*var)
        for i in range(numPoints):
            data.append([int(gauss(mean[j],variance())) for j in range(dim)])
    
    ## Clear Data Files
    for procNumber in range(numProcs):
        datafile = "data/horizontal-k-means/"+str(procNumber)+".in"
        if os.path.exists(datafile):
            os.remove(datafile)
        f = open(datafile, 'w')
        f.close()
    
    ## Randomly Partition data horizontally
    for dataPoint in data:
        procNumber = randint(0,numProcs)
        datafile = "data/horizontal-k-means/"+str(procNumber)+".in"
        f = open(datafile, 'a')
        f.write("%s\n" % dataPoint)
        f.close()

dataSize = int(sys.argv[1])
numProcs = int(sys.argv[2])
datagen(numProcs, 4, dataSize, 2)

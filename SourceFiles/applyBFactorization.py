import datetime
from matrixFactorization import applyMatrixFactorization
import numpy
import math


tMatrix = numpy.loadtxt('movielensRatings.txt')
#applying matrix factorization on the updated matrix tMatrix
N = len(tMatrix)
M = len(tMatrix[0])
K = 20
P = numpy.random.rand(N,K)
Q = numpy.random.rand(M,K)
print("Started: ", datetime.datetime.now().time())
nP, nQ = applyMatrixFactorization(tMatrix, P, Q, K,50)
nR = numpy.dot(nP, nQ.T) #nR is the matrix after factorization
numpy.savetxt("factorizedMovielens.txt",nR,fmt='%.2f')
print("End at: ", datetime.datetime.now().time())



    
    
    
    
    


                
                



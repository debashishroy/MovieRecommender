from sklearn.metrics.pairwise import cosine_similarity
from array import *
import numpy
features=[]
similarityScore = numpy.loadtxt('sim.txt')

def loadFeatures():
    i=0
    featureFile= open('movieProfile4features.txt','r')
    for line in featureFile:
        line=line.strip()
        lineSP= line.split(',')
        features.insert(i,lineSP)
        i=i+1
    print("Data Loaded")
    featureFile.close()    

def getSimilarityScore(index1,index2):
    score= similarityScore[index1][index2]
    return score;

def generateSimilarityScore():
    psm=cosine_similarity(features)
    '''
    for i in range (0,1000):
        psm = cosine_similarity(features[i],features)#calculating the similarity scores between postid and all other posts
        print (psm[0])
        break        
        for temp in range(len(psm[0])):
            similarityScore[i][temp] = psm[0][temp]

    '''

    numpy.savetxt('sim.txt',psm,fmt='%.4f')
        
    
#loadFeatures()
#print(features[0])
#generateSimilarityScore()
'''
for m in features:
    print(m)

#print (similarityScore[0][2])
#generateSimilarityScore()
'''
f = getSimilarityScore(4,335)
print(f)



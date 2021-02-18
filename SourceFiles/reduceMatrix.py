import numpy as np

ratingMatrix= np.loadtxt('youTubeRatingMatrix2.txt')
print(len(ratingMatrix),len(ratingMatrix[0]))
for k in range(0,1):
    print(k)
    #print(len(ratingMatrix),len(ratingMatrix[0]))
    for u in range(0, len(ratingMatrix)):
        zeroCount=0
        for m in range(0, len(ratingMatrix[0])):
            if ratingMatrix[u][m]==0.0:
                zeroCount=zeroCount+1
        if zeroCount>=997:
            #print("got zerooooooooooooo")
            ratingMatrix=np.delete(ratingMatrix,u,axis=0)
            break

    
#print(zeroCount)

print(len(ratingMatrix),len(ratingMatrix[0]))         
    
'''
for i in range(ratingMatrix[0]):
    for j in range(0,)
'''
    
np.savetxt('youTubeRatingMatrix2.txt',ratingMatrix,fmt='%.2f')
    
    
    




    

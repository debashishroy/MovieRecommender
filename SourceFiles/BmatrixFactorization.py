try:
    import numpy
    from numpy import *
except:
    print ("This implementation requires the numpy module.")
    exit(0)


def applyMatrixFactorization(R, P, Q, K, steps=2, alpha=0.0002, beta=0.02):
    #print ("Starting Matrix factorization:")
    print("S: ", steps)
    Q = Q.T
    e=0
    for step in range(steps):
        print("step: ",step)
        where_are_NaNs = isnan(P)
        P[where_are_NaNs] = 0
        where_are_NaNs = isnan(Q)
        Q[where_are_NaNs] = 0        
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    eij = R[i][j] - numpy.dot(P[i,:],Q[:,j])
                    
                    for k in range(K):

                        kp = alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        P[i][k] = P[i][k] + kp
                        kq = alpha * (2 * eij * P[i][k] - beta * Q[k][j])
                        Q[k][j] = Q[k][j] + kq
                        
        e = 0

        totalItems=0
        
        where_are_NaNs = isnan(P)
        P[where_are_NaNs] = 0
        where_are_NaNs = isnan(Q)
        Q[where_are_NaNs] = 0
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    totalItems = totalItems +1
                    e = e + pow(R[i][j] - numpy.dot(P[i,:],Q[:,j]), 2)
                    for k in range(K):
                        e = e + (beta/2) * ( pow(P[i][k],2) + pow(Q[k][j],2) )
        
        e = round(e/totalItems,4)
        #print('Step', step, 'Error: ',e)
        if e < 0.001:
            break
    #print('e: ',e)
    return P, Q.T

###############################################################################


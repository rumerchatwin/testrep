# Lab 7
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
from numpy.linalg import inv 
from numpy.linalg import norm 

''' Main Driver for code (From Example)'''

def driver():
    f = lambda x: 1/(1+(10*x)**2)
    N = 3
    a = -1
    b = 1
   
    ''' create equispaced interpolation nodes'''
    xint = np.linspace(a,b,N+1)
    
    ''' create interpolation data'''
    yint = f(xint)
    
    ''' create points for evaluating the Lagrange interpolating polynomial'''
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    yeval_l= np.zeros(Neval+1)
    yeval_dd = np.zeros(Neval+1)
  
    '''Initialize and populate the first columns of the 
     divided difference matrix. We will pass the x vector'''
    y = np.zeros( (N+1, N+1) )
     
    for j in range(N+1):
       y[j][0]  = yint[j] 

    y = dividedDiffTable(xint, y, N+1)
    ''' evaluate lagrange poly '''
    for kk in range(Neval+1):
       yeval_l[kk] = eval_lagrange(xeval[kk],xint,yint,N)
       yeval_dd[kk] = evalDDpoly(xeval[kk],xint,y,N)
    ''' create vector with exact values'''
    fex = f(xeval)
    plt.figure(1)    
    plt.plot(xeval,fex,'ro-')
    plt.plot(xeval,yeval_l,'bs--') 
    plt.plot(xeval,yeval_dd,'c.--')
    plt.legend()
    plt.figure(2) 
    err_l = abs(yeval_l-fex)
    err_dd = abs(yeval_dd-fex)
    plt.semilogy(xeval,err_l,'ro--',label='lagrange')
    plt.semilogy(xeval,err_dd,'bs--',label='Newton DD')
    plt.legend()
    plt.show()

''' The Lagrange Code '''
def eval_lagrange(xeval,xint,yint,N):

    lj = np.ones(N+1)
    
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])

    yeval = 0.
    
    for jj in range(N+1):
       yeval = yeval + yint[jj]*lj[jj]
  
    return(yeval)
  
''' create divided difference matrix'''
def dividedDiffTable(x, y, n):
 
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) / (x[j] - x[i + j]))
    return y

''' Evaluating the polynomial terms and DD polynomial '''
def evalDDpoly(xval, xint,y,N):
    ''' evaluate the polynomial terms'''
    ptmp = np.zeros(N+1)
    ptmp[0] = 1.
    for j in range(N):
      ptmp[j+1] = ptmp[j]*(xval-xint[j])
     
    '''evaluate the divided difference polynomial'''
    yeval = 0.
    for j in range(N+1):
       yeval = yeval + y[0][j]*ptmp[j]  

    return yeval

''' Monomial Expansion'''

def monomial(yint, xint, Neval):
   row = Neval; column = Neval
   V = np.zeros((row, column))
   for i in range(len(row)):
      xint[i] = -1 + (i-1)
      for j in range(len(column)):
         V[i][j] = ( xint[i] ** j )

   Vinv = inv(V)

   a_vector  = np.dot(Vinv, yint)
   return[a_vector]
   



''' Code that runs '''
driver()        





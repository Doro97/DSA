
from numpy import array, dtype


def simpleArraySum(ar):
    # pseudocode
    # [1,2]=3
    # index 0+index 1=sum of array
    # ar[0] + ar[1] =3 
    # lenArray=len(ar)    
    sumArray=0
    for i in ar:
        sumArray=sumArray+i
        
            
            
    print (sumArray)
        


simpleArraySum([1, 2, 3, 4, 10, 11])
g
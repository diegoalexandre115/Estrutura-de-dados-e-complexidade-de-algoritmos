import os
""" def helperFunc(x,y):
    z = []
    for element in range(0,len(x)):
        aux = 0 
        aux2 = 0
        aux3 = False
        for member in range(0,len(y)):
            if(x[element] > y[member]):
                aux = member
                aux2 = element
                aux3 = True
            else:
                break      
        if(aux3):
            if(aux+1 < len(y)):
                y.insert(aux+1,x[aux2])
                z.append(x[aux2])
            else:
                y.append(x[aux2])
                z.append(x[aux2])
    x = [i for i in x if i not in z]               
    return x+y         """
def helperFunc(x,y):
    z = x + y
    k = []
    """ aux = 0
    aux2 = 0
    if(len(x) > len(y)):
        aux = len(x)
        aux2 = len(y)
    else:
        aux = len(y)
        aux2= len(x)     """
    for i in range(1,len(x)):
        aux=0
        aux2= False
        for j in range(len(x),len(z)):
            if(z[i] > z[j]):
                aux = j
                aux2 = True    
            else:
                break    
        if(aux2):
            if(aux+1 < len(z)):    
                z.insert(aux+1,z[i])
                k.append(i)
            else:
                z.append(z[i])
                k.append(i)
    for i in range(len(k)-1,-1,-1):
        z.pop(k[i])            
    return z        

def mergeSort(array):
    output = []
    size = len(array)
    if(size==1):
        return array
    x = mergeSort(array[0:size//2])
    y = mergeSort(array[size//2:size])

    if(x[0] < y[0]):
        output = helperFunc(x,y)
    else:
        output = helperFunc(y,x)   
                        
    return output 
    
    

def quickSort(A, lo, hi):
    if lo < hi:
        p = helperFuncQuick(A, lo, hi)
        quickSort(A, lo, p - 1)
        quickSort(A, p + 1, hi)

def helperFuncQuick(A, lo, hi):
    pivot = A[hi]
    i = lo
    for j in range(lo,hi):
        aux = 0
        if (A[j] < pivot):
            aux = A[i]
            A[i] = A[j]
            A[j] = aux
            i = i + 1
    aux = A[i]  
    A[i]= A[hi]
    A[hi] = aux
    return i
            


""" array=[9,8,10,7,3,2,1]
print(mergeSort(array))  """

def readFile(fileName):
    f= open(fileName,"r+")
    contents = f.readlines()
    contents.pop(0)
    return contents 

for r,d,f in os.walk("instancias-num"):
    for file in f:
        array = readFile(os.path.join(r,file).replace("\\\\","\\"))
        for f in range(0,len(array)):
            array[f] = int(array[f].replace("\\n",""))
        array2 = array.copy()
        array3 = array.copy()
        array = mergeSort(array)
        f = open(file + " mergesorted","w+")
        for n in array:
            f.write(str(n) + "\n")
        f.close()
        array2.sort()
        assert array2 == array
        print(file + " mergesorted") 
        quickSort(array3,0,len(array3)-1)
        assert array2 == array3        
        print(file + " quicksorted")
        f = open(file + " quicksorted","w+")
        for n in array:
            f.write(str(n) + "\n")
        f.close() 



import os

def selectionSort(array):
    size = len(array)
    for i in range(0,size):
        aux = array[i]
        aux2 = i
        aux3 = array[i]
        for j in range(i+1,size):
            if(array[j] < aux ):
                aux = array[j]
                aux2 = j
        aux3 = array[i] 
        array[i] = aux
        array[aux2] = aux3
    return array
def insertionSort(array):
    size = len(array)
    subarray= []
    for i in range(0,size):
        subarray.append(array[i])
        sizesub= len(subarray)
        for j in range(sizesub-1,0,-1):
            if(subarray[j] < subarray[j-1]):
                aux = subarray[j-1]
                subarray[j-1] = subarray[j]
                subarray[j] = aux
            else:
                break    
    return subarray            
            

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
        array2.sort()
        array = selectionSort(array)
        assert array2 == array
        print(file + " selectionsorted")
        f = open(file + " selectionsorted","w+")
        for n in array:
            f.write(str(n) + "\n")
        f.close()  
        array3 = insertionSort(array3)
        assert array2 == array3        
        print(file + " insertionsorted")
        f = open(file + " insertionsorted","w+")
        for n in array:
            f.write(str(n) + "\n")
        f.close()  



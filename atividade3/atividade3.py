import os


def maxHeapify(array,pos):
    r = 2 * pos + 1
    l = 2 * pos + 2
    size = len(array)
    maior = pos
    if((l <= size-1) and (array[l] > array[pos])):
        maior= l
    if((r <= size-1) and (array[r] > array[maior])):
        maior = r
    if(maior != pos):
        aux = array[pos]
        array[pos] = array[maior]
        array[maior] = aux
        maxHeapify(array,maior)
    return array    
            
def heapify(array):
    for i in range(len(array)//2,-1,-1):
        output = maxHeapify(array,i)
    return output

def heapSort(array):
    array = heapify(array)
    size = len(array)
    for i in range(size-1,-1,-1):
        aux = array[0]
        array[0] = array[i]
        array[i] = aux
        aux2 = array[i:]
        array = maxHeapify(array[0:i],0)
        array = array + aux2
    return array
""" array=[9,8,10,7,3,2,1,15]
print(heapsort(array))  """

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
        array = heapSort(array)
        f = open(file + " heapSorted","w+")
        for n in array:
            f.write(str(n) + "\n")
        f.close()
        array2.sort()
        assert array2 == array



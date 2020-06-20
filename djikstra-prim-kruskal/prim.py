import os
import math

class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    def printMST(self, parent): 
        print "Edge \t Weight"
        for i in range(1, self.V): 
            print parent[i], "-", i, "\t", self.graph[i][ parent[i] ] 

    def addEdge(self,i,j,num):
        self.graph[int(i)][int(j)] = int(num)
def readFile(fileName):
    f= open(fileName,"r+")
    vertices = f.readline().replace("\n","")
    g = Graph(vertices)
    i=0
    j=1
    for line in f.readlines():
        line = line.replace("\n","")
        line = line.replace("\t"," ")
        nums = line.split(' ')
        if(nums[len(nums)-1] == ''):
            nums.pop()
        for num in nums:
            if(num != ' '):
                g.addEdge(i,j,num)
                g.addEdge(j,i,num)
                j+=1
        i+=1
        j=i+1        
    return g 


g = readFile("dij10.txt")
g.Prim()


""" for r,d,f in os.walk("instancias-num"):
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
        assert array2 == array """



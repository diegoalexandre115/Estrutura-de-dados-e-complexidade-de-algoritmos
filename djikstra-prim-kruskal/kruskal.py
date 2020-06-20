import os
import re
import math
import bisect

class Graph: 
  
    def __init__(self,vertices): 
        self.V= int(vertices)
        self.graph = []
        self.kruskalAux = [-1] * int(vertices)
        self.primAux = []
          
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w])
    def sortKruskal(self):
        self.graph = sorted(self.graph,key = lambda x:x[2])
    def followThrough(self,src):
        orig = src
        while(self.kruskalAux[orig] >= 0):
            orig = self.kruskalAux[orig]
        return orig
    def checkCycle(self,src,dest):
        cycleFound = True
        newsrc= self.followThrough(src)
        newdest = self.followThrough(dest)
        if(newsrc != newdest):
            self.kruskalAux[newdest] += self.kruskalAux[newsrc]
            self.kruskalAux[newsrc] = newdest
            cycleFound = False
        
        return cycleFound
    def Kruskal(self):
        result = []
        self.sortKruskal()
        for edge in self.graph:
            if(not self.checkCycle(edge[0],edge[1])):
                result.append(edge)
        suma = 0        
        for edge in result:        
            print(str(edge[0]) + " =====> " + str(edge[1]) + " weight= "+ str(edge[2]))
            suma+= edge[2]
        print("Final weight= " + str(suma))


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
                g.addEdge(i,j,int(num))
                j+=1
        i+=1
        j=i+1        
    return g 


file = input("Digite o nome do arquivo \n")
g = readFile(file)

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



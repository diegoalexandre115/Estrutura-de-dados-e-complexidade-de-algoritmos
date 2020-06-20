import os
import math

class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        self.selected = [0] * vertices             
        self.dist = [math.inf] * vertices
    def addEdge(self,i,j,num):
        self.graph[int(i)][int(j)] = int(num)

    def minDist(self):
        
        minimum = math.inf
        for i in range(self.V):
            if(not math.isinf(self.dist[i]) and self.dist[i] < minimum
            and self.selected[i] == 0):
                minimum = self.dist[i]
                index = i

        return index

    def Djikstra(self):
        vertex = 0
        self.dist[0] = 0
        while(vertex < self.V-1):
            
            x = self.minDist()    
            self.selected[x] = True
            for i in range(self.V):
                if(self.graph[x][i] > 0 and self.selected[i] == False and
                self.dist[i] > self.dist[x] + self.graph[x][i]):
                   self.dist[i] = self.dist[x] + self.graph[x][i]
            vertex += 1
        
        print("Min distance: " + str(self.dist[self.V-1]))    

def readFile(fileName):
    f= open(fileName,"r+")
    vertices = f.readline().replace("\n","")
    g = Graph(int(vertices))
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

file = input("Digite o nome do arquivo \n")
g = readFile(file)
g.Djikstra()


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



import os
import math

class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        self.selected = [0] * vertices             
        self.mst = []

    def addEdge(self,i,j,num):
        self.graph[int(i)][int(j)] = int(num)

    def Prim(self):
        self.selected[0] = 1
        vertex = 0
        while(vertex < self.V-1):
            minimum = math.inf
            x = 0
            y = 0
            for i in range(self.V):
                if self.selected[i]:
                    for j in range(self.V):
                        if ((not self.selected[j]) and self.graph[i][j]):  
                            if minimum > self.graph[i][j]:
                                minimum = self.graph[i][j]
                                x = i
                                y = j
            self.mst.append((x,y,self.graph[x][y]))
            self.selected[y] = True
            vertex += 1

        suma = 0
        for i in self.mst:
            print(str(i[0]) + "  =======>  " + str(i[1]) + "  weight: " + str(i[2]))
            suma+= i[2]
        print("Final Weight: " + str(suma))    

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



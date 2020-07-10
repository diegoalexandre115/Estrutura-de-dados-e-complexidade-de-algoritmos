import math

class Graph(): 
  
    def __init__(self, vertices,name): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)]    
        self.iterations = 50
        self.name = name

    def calcDist(self,path,sel):
        dist = 0
        for i in range(0,len(path)-1):
            dist += self.graph[path[i]][path[i+1]]
        if(sel == 1):       
            dist += self.graph[path[len(path)-1]][path[0]]    
        return dist

    def closestInsertion(self,path,new):
        closest_dist = math.inf
        path_temp = []
        shortest_path = []
        count = 0
        while(count < len(path)):
            path_temp = path.copy()
            path_temp.insert(count,new)
            dist = self.calcDist(path_temp,1)
            if(dist < closest_dist):
                closest_dist = dist
                shortest_path = path_temp
            count += 1        
        return shortest_path    

    def shortestInsertion(self):
        count = 1
        selected = [0] * self.V
        selected[0] =  1
        smallest_dist = math.inf
        next_node = 0
        final_path = [0]
        while(count < self.V):
            for i in final_path:
                for j in range(0,self.V):
                    if(self.graph[i][j] < smallest_dist and i != j and selected[j] == 0):
                        smallest_dist = self.graph[i][j]
                        next_node = j
            final_path = self.closestInsertion(final_path,next_node)
            selected[next_node] = 1
            smallest_dist = math.inf
            count += 1
        return final_path

    def farthestInsertion(self):
        count = 1
        selected = [0] * self.V
        selected[0] =  1
        biggest_dist = 0
        next_node = 0
        final_path = [0]
        while(count < self.V):
            for i in final_path:
                for j in range(0,self.V):
                    if(self.graph[i][j] > biggest_dist and i != j and selected[j] == 0):
                        biggest_dist = self.graph[i][j]
                        next_node = j
            final_path = self.closestInsertion(final_path,next_node)
            selected[next_node] = 1
            biggest_dist = 0
            count += 1
        return final_path
    def dAux(self,i,j,k):
        return self.graph[i][k] + self.graph[k][j] - self.graph[i][j]
    def cheapestInsertion(self):
        smallest_dist = math.inf
        next_node = 0
        final_path = [0,0]
        for i in range(1, self.V):
            if(self.graph[0][i] < smallest_dist):
                smallest_dist = self.graph[0][i]
                next_node = i
        final_path.insert(1,next_node)
        smallest_dist = math.inf
        selected = [0] * self.V
        selected[0] =  1
        selected[next_node] = 1
        count = 2
        pos = 0
        while(count < self.V):
            for i in range(0,len(final_path)-1):
                for j in range(0,self.V):
                    if(final_path[i] != j and selected[j] == 0 and self.dAux(final_path[i],final_path[i+1],j) < smallest_dist):
                        smallest_dist = self.dAux(i, i+1, j)
                        next_node = j
                        pos = i+1
            smallest_dist = math.inf
            count += 1
            final_path.insert(pos,next_node)
            selected[next_node] = 1
        return final_path    

    def twoOptSwap(self,path,i,j):
        first_part = path[0:i-1]
        second_part = path[i-1:j]
        second_part.reverse()
        third_part = path[j:]
        return first_part + second_part + third_part
    def twoOpt(self,path):
        smallest_dist_global = self.calcDist(path,0)
        smallest_dist_local = math.inf
        temp_dist = 0
        temp_path = path
        local_path = []
        final_path = path 
        while(True):
            smallest_dist_local = math.inf
            for i in range(1,self.V-1):
                for j in range(i+1,self.V-1):
                    temp_path = self.twoOptSwap(temp_path,i,j)
                    temp_dist = self.calcDist(temp_path,0)
                    if(temp_dist < smallest_dist_local):
                        smallest_dist_local = temp_dist
                        local_path = temp_path
            if(smallest_dist_global < smallest_dist_local):
                break
            else:
                smallest_dist_global = smallest_dist_local
                final_path = local_path
        return final_path                    

    def vnd(self, paths):
        i = 0
        path = []
        new_path = []
        old_dist = 0
        new_dist = 0
        while(i < len(paths)):
            path = paths[i]
            new_path = self.twoOpt(path)
            old_dist = self.calcDist(path,0)
            new_dist = self.calcDist(new_path,0)
            if(old_dist > new_dist):
                paths[i] = new_path
            else:
                i += 1    
        return paths
    def calcMultiDists(self,paths):
        best_solution = math.inf
        solution = 0
        best_path = []
        for i in paths:
            solution = self.calcDist(i,0)
            if(solution < best_solution):
                best_solution = solution
                best_path = i
        return best_solution,best_path        
    def multiStart(self):
        paths = []
        paths.append(self.shortestInsertion().insert(0,0))
        paths.append(self.farthestInsertion().insert(0,0))
        paths.append(self.cheapestInsertion())
        best_solution,best_path = self.calcMultiDists(paths)
        count = 0
        local_solution = math.inf
        local_path = []
        while(count < self.iterations):
            paths = self.vnd(paths)
            local_solution,local_path = self.calcMultiDists(paths)
            if(local_solution < best_solution):
                count = 0
                best_path = local_path
                best_solution = best_path
            else:
                count += 1                     
        return best_solution,best_path
def readFile(fileName):
    f= open(fileName,"r+")
    name = f.readline().replace("\n","").replace("\w+\:\s+","")
    vertices = f.readline().replace("\n","").replace("\w+\:\s+","")
    g = Graph(int(vertices),name)
    nothing = f.readline()
    i=0
    j=0
    for line in f.readlines():
        line = line.replace("\n","")
        line = line.replace("\t"," ")
        nums = line.split(' ')
        if(nums[len(nums)-1] == ''):
            nums.pop()
        for num in nums:
            if(num != ' '):
                g.graph[i][j]= int(num)            
                j+=1
        i+=1
        j=0        
    return g 
#i = Graph(1,"xd")
#path = [1,2,3,4,5,6,7,8,1]
#j = 4
#k = 7

#path2 = i.twoOptSwap(path,j,k)
#print(path2)

#file = input("Digite o nome do arquivo \n")
file = "bayg29.txt"
g = readFile(file)
print(g.V)
print(g.name)
#z = g.cheapestInsertion()
#v = [x + 1 if(x != 0) else x for x in z]
#v = [x + 1 for x in z]
#print(v)
#print(g.calcDist(z,0))

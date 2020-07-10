import math
import re
import numpy as np
import random
import time

class Graph(): 
  
    def __init__(self, vertices,name): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)]    
        self.iterations = 50
        self.arrays = 5
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
                        smallest_dist = self.dAux(final_path[i], final_path[i+1], j)
                        next_node = j
                        pos = i+1
            smallest_dist = math.inf
            count += 1
            final_path.insert(pos,next_node)
            selected[next_node] = 1
        return final_path    

    def twoOptSwap(self,path,i,j):
        first_part = path[0:i]
        second_part = path[i:j]
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
                    temp_path = self.twoOptSwap(path,i,j)
                    temp_dist = self.calcDist(temp_path,0)
                    if(temp_dist < smallest_dist_local):
                        smallest_dist_local = temp_dist
                        local_path = temp_path
            if(smallest_dist_global <= smallest_dist_local):
                break
            else:
                #print("two_opt improved from "+ str(smallest_dist_global) + " to " + str(smallest_dist_local)  )
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
                i = 0
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

    def reinsertion(self,path):
        #random.seed(time.time())
        random_number = random.randint(1,int((self.V)/2))
        random_number_end = random.randint(int((self.V)/2),self.V-1)
        first_part = path[0:random_number]
        second_part = path[random_number:random_number_end]
        third_part= path[random_number_end:]
        random.shuffle(second_part)
        return first_part + second_part +third_part
    def reinsertion_try3(self,path):
        random_int = random.randint(0,1)
        if(random_int == 0):
            random_number = random.randint(1,int((self.V)/2))
            first_part = [0]
            second_part = path[1:random_number]
            third_part = path[random_number:]
        else:
            random_number = random.randint(int((self.V)/2),self.V-1)
            first_part = path[0:random_number]
            second_part = path[random_number:self.V-1]
            third_part = path[self.V-1:]
        random.shuffle(second_part)
        return first_part + second_part +third_part    
    def multiStart(self):
        paths = []
        paths.append(self.shortestInsertion())
        paths.append(self.farthestInsertion())
        for i in range(len(paths)):
            paths[i].insert(0,0)
        paths.append(self.cheapestInsertion())
        random.seed(time.time())
        chosen = []
        """ for i in range(self.arrays):
            chosen = paths[random.randint(0,2)].copy()
            chosen = [x  for x in chosen if x != 0]
            random.shuffle(chosen)
            chosen.append(0)
            chosen.insert(0,0)
            paths.append(chosen) """
        #for i in range(3):
        #    paths.pop(0)    
        best_solution,best_path = self.calcMultiDists(paths)
        count = 0
        local_solution = math.inf
        local_path = []
        while(count < self.iterations):
            for i in range(len(paths)):
                paths[i] = self.reinsertion_try3(paths[i])
            paths = self.vnd(paths)
            local_solution,local_path = self.calcMultiDists(paths)
            if(local_solution < best_solution):
                count = 0
                best_path = local_path
                best_solution = local_solution
                print("Solution improved")
            else:
                count += 1
                print("Solution did not improve for "+ str(count) + " iterations" )                     
        return best_solution,best_path
def readFile(fileName):
    f= open(fileName,"r+")
    name = f.readline().replace("\n","")
    name = re.sub("\w+\:\s+","",name)
    vertices = f.readline().replace("\n","")
    vertices = re.sub("\w+\:\s+","",vertices)
    g = Graph(int(vertices),name)
    nothing = f.readline()
    i=0
    j=0
    for line in f.readlines():
        line = line.replace("\n","")
        line = line.replace("\t"," ")
        #line = re.sub("\s+"," ",line)
        nums = line.split(' ')
        if(nums[len(nums)-1] == ''):
            nums.pop()
        for num in nums:
            if(num != ' ' and num != ''):
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
# file = "bays29.txt"
#file = "berlin52.txt"
#file = "bier127.txt"
# file = "brazil58.txt"
# file = "ch130.txt"
# file = "ch150.txt"
# file = "swiss42.txt"
g = readFile(file)
solution,path = g.multiStart()
print(g.name)

print(path)
print(solution)
#z = g.cheapestInsertion()
#v = [x + 1 if(x != 0) else x for x in z]
#v = [x + 1 for x in z]
#print(v)
#print(g.calcDist(z,0))
 
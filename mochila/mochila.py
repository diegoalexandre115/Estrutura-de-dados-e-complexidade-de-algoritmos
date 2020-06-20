import os
import math

class KnapSack(): 
  
    def __init__(self, pesoMax,numeroProdutos): 
        self.M = pesoMax 
        self.n = numeroProdutos
        self.products = []
        self.x = [[0 for column in range(self.M+1)]  
                    for row in range(self.n+1)]
        self.g = [[0 for column in range(self.M+1)]  
                    for row in range(self.n+1)]            

    def addProduct(self,p,v):
        self.products.append((p,v))

    def produtosNaMochila(self):
        self.addProduct(0,0)
        for i in range(self.n+1):
            for y in range(self.M+1):
                if (i == 0 or y == 0):
                    self.g[i][y] = 0
                elif(self.products[i-1][0] <= y):
                    if(self.g[i-1][y] > 
                    self.products[i-1][1] + self.g[i-1][y-self.products[i-1][0]]):
                        self.g[i][y] = self.g[i-1][y]
                        self.x[i-1][y] = 0
                    else:
                        self.g[i][y] = self.products[i-1][1] + self.g[i-1][y-self.products[i-1][0]]
                        self.x[i-1][y] = 1
                else:
                    self.g[i][y] = self.g[i-1][y]
                    self.x[i-1][y] = 1
        n=self.n
        M = self.M
        produtos = []            
        while (n != 0):
            if (self.g[n][M] != self.g[n - 1][M]):
                produtos.append(n)
                M = M - self.products[n-1][0]
            n-=1
        print("Produtos selecionados ")
        for i in produtos:
            print(i)
                     
        print("Valor final: " + str(self.g[self.n][self.M]))            




def readFile(fileName):
    f= open(fileName,"r+")
    x = f.readline().replace("\n","")
    x = x.replace("\n","")
    x = x.replace("\t"," ")
    numeroProdutos,pesoMax = x.split(' ')
   
    k = KnapSack(int(pesoMax),int(numeroProdutos))
    for line in f.readlines():
        line = line.replace("\n","")
        line = line.replace("\t"," ")
        nums = line.split(' ')
        if(nums[len(nums)-1] == ''):
            nums.pop()
        k.addProduct(int(nums[0]),int(nums[1]))
    return k 

file = input("Digite o nome do arquivo \n")
k = readFile(file)
k.produtosNaMochila()


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



class MyGraphMatrix:
    def __init__(self, n):
        self.adjbody = []
        for i in range(n):
            self.adjbody.append([0]*n)
    def adj(self,v1,v2):
        self.adjbody[v1-1][v2-1]=1

class MyGraphMatrix2(MyGraphMatrix):
    def __init__(self, n):
        super().__init__(n)

    def adj(self,v1,v2):
        super().adj(v1, v2)

    def qadj(self,i,j):
        ###CODE HERE###
        if(self.adjbody[i-1][ j-1]==1):
            return True
        else:
            return False

    def trypath(self,l):
        ###CODE HERE###
        result = [self.qadj(l[i], l[i+1]) for i in range(len(l)-1)]
        if False in result:
            return False
        else:
            return True
g = MyGraphMatrix2(5)
g.adj(1,2)
g.adj(1,5)
g.adj(2,1)
g.adj(2,5)
g.adj(2,3)
g.adj(2,4)
g.adj(3,2)
g.adj(3,4)
g.adj(4,2)
g.adj(4,5)
g.adj(4,3)
g.adj(5,4)
g.adj(5,1)
g.adj(5,2)
print(g.adjbody)
print(g.trypath([1,2,5,4,3]))
print(g.trypath([1,3,5,4,3]))
print(g.trypath([1,2,4,3,5]))
print(g.trypath([1,2,4,3,2,5]))
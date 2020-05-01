class Human:
    def __init__(self,name):
        self.name = name
    def hello(self):
        print("Hello!")

comm = [None]*2 # just a trick to allocate array
comm[1] = Human("John")

comm2 = []
comm2.append(Human("Jack"))
print(comm2)

comm3 = []
comm3.append(1)
print(comm3)
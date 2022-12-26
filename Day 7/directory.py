class File:
    def __init__(self) -> None:
        self.dir = None
        self.size = None
        self.name = None
    
class Dir:
    def __init__(self,name) -> None:
        self.parent = None
        self.name = name
        self.children = []
    
    def insert(self, name):
        child = Dir(name)
        child.setparent(self.name)
        self.children.append(child)
    
    def setparent(self,name):
        self.parent = name
        
    def __repr__(self) -> str:
        print(self.name)
        print(self.children)
        while self.children != None:
            for child in self.children:
                print(child)
    
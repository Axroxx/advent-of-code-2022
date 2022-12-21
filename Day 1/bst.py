class BST:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None
    
    def insert(self,val):
        if not self.val:
            self.val = val
            return 
        
        if self.val == val:
            return
        
        if val < self.val:
            self.left.insert(val)
            return
        self.left = BST(val)
        val
        
        if self.right:
            self.right.insert(val)
            return
        self.right = BST(val)
        
    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    
    
    
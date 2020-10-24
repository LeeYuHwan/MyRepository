class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key=key
        self.left=left
        self.right=right

class AVLDict:
    def __init__(self):
        self.node=None
        self.height=0
        self.balance=0
    def search(self, search_key):
        x=self.node 
        while x is not None:
            if x.key[0:x.key.find(":")]==search_key:
                return x.key
            elif x.key[0:x.key.find(":")]>search_key:
                x=x.left.node
            else:
                x=x.right.node

        return None

    def insert(self, v):
        x=self.node
        if x is None:
            self.node=Node(v)
            self.node.left=AVLDict()
            self.node.right=AVLDict()

        elif x.key[0:x.key.find(":")]>v[0:v.find(":")]:
            self.node.left.insert(v)

        else:
            self.node.right.insert(v)

        self.check_balance()

    def check_balance(self):
        self.update_heights(False)
        self.update_balances(False)

        while self.balance<-1 or self.balance>1:
            if self.balance>1:
                if self.node.left.balance<0:
                    self.node.left.rotate_left()
                self.rotate_right()
            else:
                if self.node.right.balance>0:
                    self.node.right.rotate_right()
                self.rotate_left()

            self.update_heights()
            self.update_balances()

    def rotate_right(self):
        g=self.node
        p=g.left.node
        x=p.right.node

        self.node=p
        p.right.node=g
        g.left.node=x

    def rotate_left(self):
        g=self.node
        p=g.right.node
        x=p.left.node

        self.node=p
        p.left.node=g
        g.right.node=x

    def update_heights(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_height()
                if self.node.right is not None:
                    self.node.right.update_height()
            self.height=max(self.node.left.height, self.node.right.height)+1
        else:
            self.height=0

    def update_balances(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_balances()
                if self.node.right is not None:
                    self.node.right.update_balances()
            self.balances=self.node.left.height-self.node.right.height
        else:
            self.balances=0
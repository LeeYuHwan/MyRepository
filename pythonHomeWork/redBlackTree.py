black=0
red=1

class Node:
    def __init__(self, color, key=None, left=None, right=None):
        self.color=color
        self.key=key
        self.left=left
        self.right=right

class Dict:
    def __init__(self): 
        self.z=Node(color=black, key="", left="", right="")
        self.z.left=self.z
        self.z.right=self.z
        self.head=Node(black, "", "", self.z)

    
    # 레드-블랙 트리 탐색
    def search(self, search_key): 
        x=self.head.right
        
        while x!=self.z:
            if x.key[0:x.key.find(":")]==search_key:
                return x.key
            elif x.key[0:x.key.find(":")]>search_key:
                x=x.left
            else:
                x=x.right

        return None

    def insert(self, v):
        x=p=g=self.head
        while(x!=self.z):        
            gg=g
            g=p
            p=x
            if x.key[0:x.key.find(":")]==v[0:v.find(":")]:
                return 
            elif x.key[0:x.key.find(":")]>v[0:v.find(":")]:
                x=x.left
            else:
                x=x.right
                    
            if x.left.color==red and x.right.color==red:
                self.split(x, p, g, gg, v)
                
        x=Node(red, v, self.z, self.z)
        if p.key[0:p.key.find(":")]>v[0:v.find(":")]:
            p.left=x
        else:
            p.right=x
            
        self.split(x, p, g, gg, v)
        self.head.right.color=black

    def split(self, x, p, g, gg, v):
        x.color=red
        x.left.color=black
        x.right.color=black

        if p.color==red:
            g.color=red
            if (g.key[0:g.key.find(":")]>v[0:v.find(":")])!=(p.key[0:p.key.find(":")]>v[0:v.find(":")]):
                p=self.rotate(v, g)
            x=self.rotate(v, gg)
            x.color=black

    def rotate(self, v, y):
        gc=c=Node
        if y.key[0:y.key.find(":")]>v[0:v.find(":")]:
            c=y.left
        else:
            c=y.right

        if c.key[0:c.key.find(":")]>v[0:v.find(":")]:
            gc=c.left
            c.left=gc.right
            gc.right=c
        else:
            gc=c.right
            c.right=gc.left
            gc.left=c

        if y.key[0:y.key.find(":")]>v[0:v.find(":")]:
            y.left=gc
        else:
            y.right=gc

        return gc
        

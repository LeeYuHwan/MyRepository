class HashingDict:
    def __init__(self, M):
        self.a=[None]*M

    def search(self, size, search_key, M):
        x=self.hash(size, M)
        u=self.hash2(size)
        while self.a[x]!=None:
            if search_key==self.a[x][0:self.a[x].find(":")]:
                return self.a[x]
            else:
                x=(x+u)%M
                
        return None

    def insert(self, size, v, M):
        x=self.hash(size, M)
        u=self.hash2(size)
        while self.a[x]!=None:
            x=(x+u)%M
        self.a[x]=v

    def hash(self, v, M):
        return v%M

    def hash2(self, v):
        return 13-(v%13)
        


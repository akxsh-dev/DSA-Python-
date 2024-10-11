class MyHash:
    def __init__(self,b):
        self.bucket=b
        self.table=[[]for x in range(b)]

    def insert(self,x):
        i=x%self.bucket
        self.table[i].append(x)

    def remove(self,x):
        i = x % self.bucket
        self.table[i].remove(x)

    def search(self,x):
        i = x % self.bucket
        return x in self.table[i]

    def display(self):
        for i in range(self.bucket):
            print(f"Bucket {i}: {self.table[i]}")



h=MyHash(7)
h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)
print(h.search(56))
h.remove(56)
h.display()
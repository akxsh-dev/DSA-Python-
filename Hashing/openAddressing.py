#open Addressing using Linear Probing
class MyHash:
    def __init__(self,c):
        self.cap=c
        self.table=[-1]*c
        self.size=0


    def hash(self,x):
        return x % self.cap

    def search(self,x):
        h=self.hash(x)
        t=self.table            #just to avoid writing self.table i am writing this
        i=h
        while t[i]!=-1:
            # if we find the key
            if t[i]==x:
                return True
            # if we dont find the key
            i=(i+1)%self.cap
            if i==h:
                return False
        return False

    def insert(self,x):
        # when our hash table is already full
        if self.size == self.cap:
            return False
        #when key is already present in our hash table
        if self.search(x)== True:
            return False

        #we insert
        i=self.hash(x)
        t=self.table
        #we will use both -1 and -2 mean empty and deleted slots for inserting the values
        while t[i] not in (-1,-2):
            i=(i+1)%self.cap
        # we come out of the loop and insert the value
        t[i]=x
        self.size +=1
        return True

    def remove(self, x):
        h = self.hash(x)
        t = self.table
        i = h
        # loop to find the element to be deleted
        while t[i] != -1:  # -1 means the slot is empty
            if t[i] == x:  # if we find the key
                t[i] = -2  # mark as deleted (using -2)
                self.size -= 1  # reduce the size
                return True
            i = (i + 1) % self.cap  # continue probing linearly
            if i == h:  # if we've come full circle
                return False
        return False  # return False if the key is not found

    def display(self):
        for i in range(self.cap):
            print(f"Bucket {i}: {self.table[i]}")

h=MyHash(7)
h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)
h.display()
print(h.search(56))
h.remove(56)
print(h.search(56))
h.display()

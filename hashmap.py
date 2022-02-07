class HashTable:
    def __init__(self):
        self.max = 100
        self.array = []
        for element in range(self.max):
            self.array.append(None)
        #print(self.array)
        #print(t.array)
       
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return (h % 100)
        #ord is a function tha gives unicode number for certain characters.
    def add(self, key, val):
        h = self.get_hash(key)
        self.array[h] = val

    def get(self, key):
        h = self.get_hash(key)
        return self.array[h]
        
    def delete(self,key):
        h = self.get_hash(key)
        self.array[h] = None

t = HashTable()
#print(t.get_hash("march 6"))
#print(t.array)
t.add('march 6',30)
t.add('march 4', 120)
t.add('march 8', 140)
t.add('march 10', 160)
print(t.array)
#print(t.get('march 6'))
print(t.get('march 6'))
print(t.get('march 4'))
print(t.get('march 8'))
print(t.get('march 10'))

t.delete('march 8')
print(t.array)


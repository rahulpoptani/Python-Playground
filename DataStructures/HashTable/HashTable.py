class HashTable:
    def __init__(self):
        # size of the hash table
        self.slots = 10
        self.size = 0
        self.bucket = [None] * self.slots
    
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def get_index(self, key):
        hash_code = hash(key)
        index = hash_code % self.slots
        return index
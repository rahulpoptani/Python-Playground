class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.key) + ", " + str(self.value)

entry = HashEntry(3, "Educative")
print(entry)
class HashTable:
    #initialize hash table
    def __init__(self, size=20):
        self.size = size
        self.table = [[] for i in range(size)]

    #function to hash key value used in other functions
    def _hash(self, key):
        return hash(key) % self.size


    #add item to table or update if exists
    def add(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for item in bucket:
            if item[0] == key:
                item[1] = value
                return

        bucket.append([key, value])

    #defines lookup function to return data in package
    def lookup(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for item in bucket:
            if item[0] == key:
                return item[1]
        return None

#built for testing to see all data in the hash table, mainly to see what time each package got delivered
    def print_all(self):
        for index, bucket in enumerate(self.table):
            if bucket:
                for key, value in bucket:
                    print(f"Index {index}: {key} => {value}")
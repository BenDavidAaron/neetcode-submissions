class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.lru = []

    def get(self, key: int) -> int:
        if key not in self.lru:
            return -1
        self.lru.remove(key)
        self.lru.append(key)
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru.remove(key)
            self.lru.append(key)
        else:
            self.lru.append(key)
            while len(self.lru) > self.cap:
                evicted = self.lru.pop(0)
                del self.cache[evicted]
        self.cache[key] = value
        return

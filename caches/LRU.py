from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def __getitem__(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return None

    def __setitem__(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value

c = LRUCache(3)
c['f'] = 'rocky'
c['s'] = 'kiko'
c['t'] = 'paul' 
c['f']
c['l'] = 'luna'
c['t']
# c['l2'] = 'luna'
print c.cache.keys()
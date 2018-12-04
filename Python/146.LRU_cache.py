import collections
class LinkList:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    # first solution, using orderDict
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # no key exists in cache
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value
#     # second solution, using dict + double linked list
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.dic = dict()
#         self.head = Node(0, 0)
#         self.tail = Node(0, 0)
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def get(self, key):
#         if key in self.dic:
#             n = self.dic[key]
#             self._remove(n)
#             self._add(n)
#             return n.val
#         return -1

#     def set(self, key, value):
#         if key in self.dic:
#             self._remove(self.dic[key])
#         n = Node(key, value)
#         self._add(n)
#         self.dic[key] = n
#         if len(self.dic) > self.capacity:
#             n = self.head.next
#             self._remove(n)
#             del self.dic[n.key]

#     def _add(self, node):
#         prev = self.tail.prev
#         prev.next = node
#         self.tail.prev = node
#         node.prev = prev
#         node.next = self.tail
        
#     def remove(self, node):
#         prev = node.prev
#         n = node.next
#         prev.next = n
#         n.prev = prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class Node: 
    def __init__(self, key: int, val: int):
        self.key = key 
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.mp1 = {}
        self.capacity = capacity

        self.dummyLeft = Node(0, 0)
        self.dummyRight = Node(0, 0)

        self.dummyLeft.next = self.dummyRight
        self.dummyRight.prev = self.dummyLeft

    
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):

        right = self.dummyRight.prev

        dummy = self.dummyRight

        node.next = dummy 
        node.prev = right
        
        right.next = node
        dummy.prev = node
  

    def get(self, key: int) -> int:


        if key in self.mp1:

            node = self.mp1[key]
            self.remove(node)
            self.insert(node)
            
            return self.mp1[key].val

        
    
        return -1



    def put(self, key: int, value: int) -> None:

        if key in self.mp1:
            self.remove(self.mp1[key])
        
        self.mp1[key] = Node(key, value)
        self.insert(self.mp1[key])
        if len(self.mp1) > self.capacity:
            lru = self.dummyLeft.next
            self.remove(lru)
            del self.mp1[lru.key]

   
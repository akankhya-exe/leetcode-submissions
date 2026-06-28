import collections

class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)

        self.left.next = self.right
        self.right.prev = self.left

        self.map = {}

    def length(self):
        return len(self.map)

    def pushRight(self, val):
        node = ListNode(val, self.right.prev, self.right)

        self.map[val] = node

        node.prev.next = node
        node.next.prev = node

    def pop(self, val):
        if val not in self.map:
            return

        node = self.map[val]

        node.prev.next = node.next
        node.next.prev = node.prev

        del self.map[val]

    def popLeft(self):
        if self.length() == 0:
            return None

        val = self.left.next.val
        self.pop(val)
        return val


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.minFreq = 0

        self.valMap = {}                          # key -> value
        self.countMap = {}                        # key -> frequency
        self.listMap = collections.defaultdict(LinkedList)   # freq -> DLL

    def counter(self, key):
        freq = self.countMap[key]

        self.listMap[freq].pop(key)

        if freq == self.minFreq and self.listMap[freq].length() == 0:
            self.minFreq += 1

        self.countMap[key] += 1
        self.listMap[freq + 1].pushRight(key)

    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1

        self.counter(key)
        return self.valMap[key]

    def put(self, key: int, value: int) -> None:

        if self.cap == 0:
            return

        # key already exists
        if key in self.valMap:
            self.valMap[key] = value
            self.counter(key)
            return

        # cache full
        if len(self.valMap) == self.cap:
            lru = self.listMap[self.minFreq].popLeft()

            del self.valMap[lru]
            del self.countMap[lru]

        # insert new key
        self.valMap[key] = value
        self.countMap[key] = 1

        self.listMap[1].pushRight(key)
        self.minFreq = 1

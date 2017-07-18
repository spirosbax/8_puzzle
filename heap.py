import helper as h
import heapq

class heap:
    def __init__(self):
        # create a new min-heap and a set for constant look-up
        self._heap = []
        self._set = set()


    def __len__(self):
        return len(self._heap)


    def __contains__(self, item):
        return item in self._set


    def __iter__(self):
        """ Get all elements ordered by asc. priority. """
        return self


    # Push an item with key into the heap.
    def push(self, key, item):
        # Priority 0 is the highest, which means that such an item will
        # be popped first.
        if key  < 0:
            raise KeyError
        item = h.to_tuple(item)
        heapq.heappush(self._heap, (key, item))
        self._set.add(item)


    def pop(self):
        # Returns the item with highest priority.
        item = heapq.heappop(self._heap)[1] # (key, item)[1] == item
        self._set.remove(item)
        return item


    def next(self):
        """ Get all elements ordered by their priority (lowest first). """
        try:
            return self.pop()
        except IndexError:
            raise StopIteration


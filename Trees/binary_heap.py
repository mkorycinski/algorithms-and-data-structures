class BinHeap:
    """List representation of a binary heap"""
    def __init__(self):
        """Initializes an 'empty' list to store heap inside
        and sets current heap size to 0. 0 at the beginning is not used,
        it's just for simplification.
        """
        self.heapList = [0]
        self.currentSize = 0

    def siftUp(self, i):
        """Insert method"""

        # get the parent from a left child (oppose to 2*P)
        while i // 2 > 0:

            # if current node is smaller than the parent
            if self.heapList[i] < self.heapList[i // 2]:

                # store parent
                tmp = self.heapList[i // 2]

                # set parent to the value from a current node
                self.heapList[i // 2] = self.heapList[i]

                # set current node value to the parent
                self.heapList[i] = tmp

            # go up a node
            i //= 2

    def insert(self, k):
        """Wrapper method for inserting value to the heap"""
        self.heapList.append(k)
        self.currentSize += 1
        self.siftUp(self.currentSize)

    def percDown(self, i):
        """place root in proper place - reconstruct correct heap structure"""
        # while child is still there
        while (i * 2) <= self.currentSize:

            # get list index of minimal child
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        """ Get list index of minimal child"""

        # If right child is bigger than the list size (does not exist)
        if i * 2 + 1 > self.currentSize:

            # return left child
            return i * 2
        # if right child exists (is in the list)
        else:
            # if left child is smaller than right child
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                # return left child
                return i * 2
            else:
                # otherwise return right child
                return i * 2 + 1

    def delMin(self):
        # save the value from the root
        retval = self.heapList[1]

        # make the last leaf a root node
        self.heapList[1] = self.heapList[self.currentSize]
        # decrease size counter of the heaplist
        self.currentSize -= 1

        # remove last leaf which is already the root of heap
        self.heapList.pop()

        # place root in proper place - reconstruct correct heap structure
        self.percDown(1)

        # return min value (old root)
        return retval

    def buildHeap(self, alist):
        """builds binary heap from a list of keys"""

        # we start in the middle of the heap
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i -= 1

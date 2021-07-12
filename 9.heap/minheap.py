class MinHeap:

    def __init__(self):
        self.heap = [0]
        self.size = 0

    def __up(self, i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i//2]:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i // 2

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.__up(self.size)

    def __min_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heap[i*2] < self.heap[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def __down(self, i):
        while i * 2 <= self.size:
            idx = self.__min_child(i)
            if self.heap[i] > self.heap[idx]:
                self.heap[i], self.heap[idx] = self.heap[idx], self.heap[i]
            i = idx

    def min_pop(self):
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]
        val = self.heap.pop()
        self.size -= 1
        self.__down(1)
        return val


if __name__ == '__main__':

    heap = MinHeap()

    heap.insert(3)
    heap.insert(1)
    heap.insert(7)
    heap.insert(5)

    # print(heap.size)

    print(heap.min_pop())
    print(heap.min_pop())
    print(heap.min_pop())
    print(heap.min_pop())





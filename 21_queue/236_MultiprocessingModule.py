from multiprocessing import Queue

customQueue = Queue(maxsize=3)
print(customQueue.empty())
print("-----------------------")
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.full())
print("-----------------------")
print(customQueue.get())
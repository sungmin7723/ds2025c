from queue import Queue

q = Queue()
q.put("DataBase")
q.put("Data Structure")
q.put("JavaScript")

print(q.qsize())
print(q.get())
print(q.qsize())
print(q.get())
print(q.qsize())
print(q.get())
# print(q.dequeue()) => 큐 안에 아무것도 없어서 IndexError 발생


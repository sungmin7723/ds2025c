from collections import deque

d = deque([17, 55, 123])
d.append(7)
d.append(-91)

for i in range(len(d)):
    print(d.popleft())

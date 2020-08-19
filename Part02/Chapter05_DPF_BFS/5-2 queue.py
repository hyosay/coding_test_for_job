from collections import deque
queue = deque([10])

queue.append(1)
queue.append(2)
queue.append(5)
queue.append(6)
a = queue.popleft()
print(a)
print(queue)


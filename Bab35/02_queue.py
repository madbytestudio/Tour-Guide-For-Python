from collections import deque

queue = deque(["A", "B", "C"])

print(queue)
print(queue.popleft())
print(queue)

queue.append("D")
print(queue)

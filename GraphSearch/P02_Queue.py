"""
큐 자료구조
FIFO
입구와 출구가 모두 뚫려 있는 터널 같은 형태
"""

from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)    # 먼저 들어온 순서대로 출력 (FIFO) deque([3, 7, 1, 4])
queue.reverse()    # 역순으로 바꾸기
print(queue)    # 나중에 들어온 원소부터 출력 deque([4, 1, 7, 3])
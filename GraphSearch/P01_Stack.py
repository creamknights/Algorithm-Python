"""
스택 자료구조
LIFO
입구와 출구가 동일
"""

stack = []    # 리스트의 가장 왼쪽 원소가 가장 처음에 들어온 원소

stack.append(5)    # 삽입 O(1)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()    # 삭제 O(1)
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1])    # 순서를 뒤집어서 최상단 원소부터 출력 [1, 3, 2, 5] (LIFO)
print(stack)    # 최하단 원소부터 출력하면 [5, 2, 3, 1]
""" 
정렬 알고리즘
데이터를 특정한 기준에 따라 순서대로 나열

데이터의 개수가 적을 때
데이터의 개수가 많지만 데이터의 범위가 특정 범위로 한정되어 있을 때
데이터가 이미 거의 정렬되어 있을 때

"""

""" 
<선택 정렬>
처리되지 않은 데이터 중에서
가장 작은 데이터를 선택해
맨 앞에 있는 데이터와 바꾸는 것을 반복

[시간 복잡도]
N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 한다.
전체 연산 횟수는 N + (N-1) + (N-2) + ... + 2 = (N^2+N-2)/2
빅오 표기법 -> O(N^2)
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i    # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]    # 스와프
    
print(array)
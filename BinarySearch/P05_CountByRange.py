""" 
정렬된 배열에서 특정 수의 개수 구하기
N개의 원소를 포함한 오름차순 수열에서 x가 등장하는 횟수 계산
{1, 1, 2, 2, 2, 2, 3}이 있을 때 x = 2라면, 4를 출력
단, 시간 복잡도 O(logN)으로 설계해야 한다. Linear Search로는 시간 초과.

[문제 해결 아이디어]
데이터가 정렬되어 있기 때문에 '이진 탐색'을 수행할 수 있다.
특정 값이 등장하는 첫 번째 위치와 마지막 위치를 찾아 위치 차이를 계산

"""

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value] 범위에 있는 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

n, x = map(int, input().split())    # 데이터의 개수 N, 찾고자 하는 값 x 입력 받기
array = list(map(int, input().split()))    # 전체 데이터 입력 받기

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)
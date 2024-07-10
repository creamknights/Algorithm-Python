""" 시간 제한 2초
N이 1이 될 때까지 두 과정 중 하나를 반복적으로 수행
1. N - 1
2. N / K (나누어 떨어지는 경우만)

전체 실행 횟수 = N을 1로 만드는 최소 횟수 구하는 문제

(문제 해결 아이디어)
최대한 많이 나누기를 수행. N의 값을 줄일 때 2 이상의 수로 나누는 작업이 1을 빼는 작업보다 수를 훨씬 많이 줄일 수 있다.
나눌 수 없다면 1을 빼준다.
(정당성 분석) 최적의 해를 항상 보장할까? YES

[시간 복잡도]
반복문이 한 번 반복 될 때마다 N이 K로 나누어지는 연산이 수행되기 때문에
반복 횟수에 따라서 N이 기하급수적으로 빠르게 줄어든다. -> log 시간 복잡도

"""

# N, K를 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True: 
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기 (과정 1)
    target = (n // k) * k #  (*) K로 나누어 떨어지는 가장 가까운 수
    result += (n - target) # target이 될 때까지 빼주는 과정 반복
    n = target # (n - target) 만큼 빼줬으므로
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기 (과정 2)
    result += 1 # 나누는 연산 1번 수행 
    n //= k

# 마지막으로 남은 수에 대하여 1씩 1이 되도록 빼기 (n < k)
result += (n - 1)
print(result)

"""
(*) N을 k로 나눈 몫에 다시 k를 곱해줌으로써 K로 나누어 떨어지는 수 중에 N과 가장 가까운 수를 구한다.
N이 K로 나누어 떨어지지 않는다고 했을 때 '가장 가까운 K로 나누어지는 수'가 어떤 건지 찾을 수 있다.
1을 빼는 과정을 몇 번 반복해야 K로 나누어 떨어지는 target을 만들 수 있는지 구한다. (n - target)

(25 // 3) * 3 = 8 * 3 = 24
25 - 24 = 1 # 1을 1번 빼준다.

"""
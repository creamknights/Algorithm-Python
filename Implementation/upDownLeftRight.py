""" 시뮬레이션 및 완전 탐색 문제 - 2차원 공간 방향 벡터 """
# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 현재 위치
x, y = 2, 2

for i in range(4):
    # 다음 위치
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)

""" 시뮬레이션 유형 - 상하좌우 문제
N x N 크기의 정사각형 공간, 가장 왼쪽 위 좌표는 (1,1) 가장 오른쪽 아래 좌표는 (N, N)
시작 좌표는 (1,1), 정사각형 공간을 벗어나는 움직임은 무시한다."""

# N 입력 받기
n = int(input())
x, y = 1, 1    # 시작 좌표
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]    # Left로 이동하면 행은 그대로, 열은 왼쪽으로 한 칸 이동하므로 dx로는 0, dy로는 -1 좌표 이동한다.
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny
        
print(x, y) 
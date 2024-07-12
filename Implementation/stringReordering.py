""" 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다.
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에
그 뒤에 모든 숫자를 더한 값을 이어서 출력한다.
K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력한다.

split해서 문자로 담은 후 반복문을 돌려서 알파벳과 숫자를 구분해서 리스트에 담는다.
sort 정렬한다. 알파벳 문자열과 숫자 문자열을 더한다.
"""
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자인 경우 더하기
    else: 
        value += int(x)
        
# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환)
print(''.join(result))
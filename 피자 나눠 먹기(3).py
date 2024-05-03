# LEVEL0: 피자 나눠 먹기(1)
def solution(slice, n):
    answer = 0
    if n % 7 != 0:
        answer = (n // 7) + 1
    else:
        answer = n // 7
    return answer

# 출력문 예시
print(solution(7, 10))
print(solution(4, 12))
# LEVEL0: 세균 증식
def solution(n, t):
    answer = n * (2 ** t)
    return answer

# 출력문 예시
print(solution(2, 10))
print(solution(7, 15))

# LEVEL0: 짝수의 합
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            answer += i
    return answer

# 출력문 예시
print(solution(10))
print(solution(4))
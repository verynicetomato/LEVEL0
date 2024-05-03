# LEVEL0: 중복된 숫자 개수
def solution(n):
    answer = []
    for i in range(1, n + 1):
        if i % 2 == 1:
            answer.append(i)
    return answer

# 출력문 예시
print(solution(10))
print(solution(15))
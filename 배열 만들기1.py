# LEVEL0: 배열 만들기1
def solution(n, k):
    answer = []
    for i in range(1, n + 1):
        if i % k == 0:
            answer.append(i)
    return answer

# 출력문 예시
print(solution(10, 3))
print(solution(15, 5))
# LEVEL0: 중복된 숫자 개수
def solution(array, n):
    answer = 0
    for i in range(len(array)):
        if array[i] == n:
            answer += 1
    return answer

# 출력문 예시
print(solution([1, 1, 2, 3, 4, 5], 1))
print(solution([0, 2, 3, 4], 1))
# LEVEL0: n번째 원소까지
def solution(num_list, n):
    answer = num_list[:n]
    return answer

# 출력문 예시
print(solution([2, 1, 6], 1))
print(solution([5, 2, 1, 7, 5], 3))
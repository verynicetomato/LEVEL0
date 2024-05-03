# LEVEL0: 배열 뒤집기
def solution(num_list):
    answer = []
    for i in range(len(num_list) - 1, -1, -1):
        answer.append(num_list[i])
    return answer

# 출력문 예시
print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))
print(solution([1, 0, 1, 1, 1, 3, 5]))
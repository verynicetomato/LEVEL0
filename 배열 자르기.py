# LEVEL0: 배열 자르기
def solution(numbers, num1, num2):
    answer = []
    for i in range(num1, num2 + 1):
        answer.append(numbers[i])
    return answer

# 출력문 예시
print(solution([1, 2, 3, 4, 5], 1, 3))
print(solution([1, 3, 5], 1, 2))
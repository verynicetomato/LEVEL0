# LEVEL0: 배열의 평균값
def solution(numbers):
    answer = 0
    for i in numbers:
        answer += i
    return answer / len(numbers)

# 출력문 예시
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))
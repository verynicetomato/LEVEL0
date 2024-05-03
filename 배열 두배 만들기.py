# LEVEL0: 배열 두배 만들기
def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i * 2)
    return answer

# 출력문 예시
print(solution([1, 2, 3, 4, 5]))
print(solution([1, 2, 100, -99, 1, 2, 3]))
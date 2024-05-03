# LEVEL0: 숫자 비교하기
def solution(num1, num2):
    answer = -1
    if num1 == num2:
        answer = 1
    return answer

# 출력문 예시
print(solution(2, 3))
print(solution(11, 11))
print(solution(7, 99))
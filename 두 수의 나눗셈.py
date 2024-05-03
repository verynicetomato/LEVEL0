# LEVEL0: 두 수의 나눗셈
def solution(num1, num2):
    answer = int((num1 / num2) * 1000)
    return answer

# 출력문 예시
print(solution(3, 2))
print(solution(7, 3))
print(solution(1, 16))

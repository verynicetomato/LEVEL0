# LEVEL0: 정수 부분
def solution(number):
    answer = int(number) % 9 
    return answer

# 출력문 예시
print(solution("123"))
print(solution("78720646226947352489"))
# LEVEL0: 문자 반복 출력하기
def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i * n
    return answer

# 출력문 예시
print(solution("hello", 3))
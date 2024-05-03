# LEVEL0: 자릿수 더하기
def solution(n):
    answer = 0
    n = str(n)
    for i in n:
        answer += int(i)
    return answer

# 출력문 예시
print(solution(1234))
print(solution(930211))
# LEVEL0: 카운트 업
def solution(start_num, end_num):
    answer = []
    for i in range(start_num, end_num + 1):
        answer.append(i)
    return answer

# 출력문 예시
print(solution(3, 10))
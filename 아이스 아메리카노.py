# LEVEL0: 아이스 아메리카노
def solution(money):
    answer = [money // 5500, money % 5500]
    return answer


# 출력문 예시
print(solution(5500))
print(solution(15000))
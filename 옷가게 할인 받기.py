# LEVEL0: 옷가게 할인 받기
def solution(price):
    answer = 0
    discount = 0
    if price >= 500000:
        discount = 0.2
    elif price >= 300000:
        discount = 0.1
    elif price >= 100000:
        discount = 0.05
    answer = int(price * (1 - discount))
    return answer

# 출력문 예시
print(solution(150000))
print(solution(580000))
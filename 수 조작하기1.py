# LEVEL0: 수 조작하기1
def solution(n, control):
    for i in control:
        if i == "w":
            n += 1
        elif i == "a":
            n -= 10
        elif i == "s":
            n -= 1
        elif i == "d":
            n += 10
    return n

# 출력문 예시
print(solution(0, "wsdawsdassw"))
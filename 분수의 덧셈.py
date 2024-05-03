# LEVEL0: 분수의 덧셈
def solution(numer1, denom1, numer2, denom2):
    numer = (numer1 * denom2) + (numer2 * denom1)
    denom = denom1 * denom2
    
    gcd_value = gcd(numer, denom)
    numer = numer // gcd_value
    denom = denom // gcd_value
     
    return [numer, denom]

# 최대공약수 구하는 함수
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 출력문 예시
print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))
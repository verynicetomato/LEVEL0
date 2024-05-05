# LEVEL0: A 강조하기
def solution(myString):
    answer = ''
    for i in myString:
        if i == "a" or i == "A":
            answer += i.upper()
        else:
            answer += i.lower()
    return answer

# 출력문 예시
print(solution("abstract algebra"))
print(solution("PrOgRaMmErS"))
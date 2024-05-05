# LEVEL0: 배열에서 문자열 대소문자 변환하기
def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if (i + 1) % 2 == 0:
            answer.append(strArr[i].upper())
        elif (i + 1) % 2 == 1:
            answer.append(strArr[i].lower())
    return answer

# 출력문 예시
print(solution(["AAA","BBB","CCC","DDD"]))
print(solution(["aBc","AbC"]))
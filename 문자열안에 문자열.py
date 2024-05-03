# LEVEL0: 문자열안에 문자열
def solution(str1, str2):
    answer = 2
    if str2 in str1:
        answer = 1
    return answer

# 출력문 예시
print(solution("ab6CDE443fgh22iJKlmn1o", "6CD"))
print(solution("ppprrrogrammers", "pppp"))
print(solution("AbcAbcA", "AAA"))
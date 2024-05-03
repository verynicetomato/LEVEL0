# LEVEL0: 대문자와 소문자
def solution(my_string):
    answer = ''
    my_string_lower = my_string.lower()
    for i in range(len(my_string)):
        if my_string[i] == my_string_lower[i]:
            answer += my_string[i].upper()
        else:
            answer += my_string[i].lower()
    return answer

# 출력문 예시
print(solution("cccCCC"))
print(solution("abCdEfghIJ"))
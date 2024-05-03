# LEVEL0: 모음 제거
def solution(my_string):
    vowels = ["a", "e", "i", "o", "u"]
    for vowel in vowels:
        my_string = my_string.replace(vowel, "")
    return my_string

# 출력문 예시
print(solution("bus"))
print(solution("nice to meet you"))
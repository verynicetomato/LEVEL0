# LEVEL0: 머쓱이보다 키 큰 사람
def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer

# 출력문 예시
print(solution([149, 180, 192, 170], 167))
print(solution([180, 120, 140], 190))
# LEVEL0: 최빈값 구하기
def solution(array):
    num = 0
    ansewr = 0
    for i in set(array):
        if array.count(i) > num:
            num = array.count(i)
            answer = i
        elif array.count(i) == num:
            answer = -1
    return answer

# 출력문 예시
print(solution([1, 2, 3, 3, 3, 4]))
print(solution([1, 1, 2, 2]))
print(solution([1]))
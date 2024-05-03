# LEVEL0: 중앙값 구하기
import math

def solution(array):
    answer = 0
    array1 = sorted(array)
    answer = array1[math.ceil((len(array) / 2)) -1] # math.ceil(): 0.5 반올림 하는 방법
    return answer

# 출력문 예시
print(solution([1, 2, 7, 10, 11]))
print(solution([9, -1, 0]))

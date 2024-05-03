# LEVEL0: 첫 번째로 나오는 음수
def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1

# 출력문 예시
print(solution([12, 4, 15, 46, 38, -2, 15]))
print(solution([13, 22, 53, 24, 15, 6]))
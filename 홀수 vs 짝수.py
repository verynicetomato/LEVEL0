# LEVEL0: 홀수 vs 짝수
def solution(num_list):
    even_answer = 0
    odd_answer = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            odd_answer += num_list[i]
        elif i % 2 == 1:
            even_answer += num_list[i]
    return max(even_answer, odd_answer)

# 출력문 예시
print(solution([4, 2, 6, 1, 7, 6]))
print(solution([-1, 2, 5, 6, 3]))
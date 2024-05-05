# LEVEL0: 5명씩
def solution(names):
    answer = []
    for i in range(len(names)):
        if i % 5 == 0:
            answer.append(names[i])
    return answer

# 출력문 예시
print(solution(["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]))
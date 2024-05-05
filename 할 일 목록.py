# LEVEL0: 할 일 목록
def solution(todo_list, finished):
    answer = []
    for i in range(len(todo_list)):
        if finished[i] == False:
            answer.append(todo_list[i])
    return answer

# 출력문 예시
print(solution(["problemsolving", "practiceguitar", "swim", "studygraph"], [True, False, True, False]))
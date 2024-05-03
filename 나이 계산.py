# LEVEL0: 나이 계산(PCCE 기출문제 3번)
year = int(input("출생 연도를 입력해주세요: "))
age_type = input("나이의 종류를 입력해주세요: ")

if age_type == "Korea":
    answer = (2030 - year) + 1
elif age_type == "Year":
    answer = 2030 - year

print(answer)
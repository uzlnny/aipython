# 1. 멜론 100곡 출력
# 2. 멜론 50곡 출력
# 3. 멜론 10곡 출력
# 4. AI 추천곡 출력
# 5. 가수 이름 검색
print("===================")
print("1. 멜론 100")
print("2. 멜론 50")
print("3. 멜론 10")
print("4. AI 추천 노래")
print("5. 가수 이름 검색")
print("===================")
# 메뉴선택(숫자입력): 1
n = input("메뉴선택(숫자입력): ")
print(f"당신이 입력한 값은? {n}") 
# 여기까지는 n 이 문자열
# n = int(n) # 숫자로 변경(연산을 해야 된다면)
# 여기서 부터는 n은 숫자(정수)

# 만약에 1을 입력하면
# 멜론 100 출력
if n == "1":
    print("멜론 100")
# else:
#     print("1이 아닙니다.")
# 만약에 2를 입력하면
# 멜론 50 출력
elif n == "2":
    print("멜론 50")

elif n == "3":
    print("멜론 10")

elif n == "4":
    print("AI 추천곡")

elif n == "5":
    print("가수 이름 검색")
# ...
# 5를 입력하면 가수 이름 검색할 수 있게 입력창이 또 나와야함
# 이름을 입력하면 해당 가수 이름의 노래 리스트가 출력
else:
    print("1~5까지 입력하세요")

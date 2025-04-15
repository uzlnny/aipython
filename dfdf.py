# 아스키 코드 그림 출력 하기

# 만약에 1을 입력 하면 1번 캐릭터 출력
# 만약에 2를 입력 하면 2번 캐릭터 출력
# 3을 입력 하면 3번 캐릭터 출력
# 잘못 입력 하면 잘못 입력 했다고 출력 

# 아스키 코드 그림 출력하기
# 고양이 출력 함수
def print_cat():
    cat = [
        " /\_/\  ",
        "( o.o ) ",
        " > ^ <  "
    ]
    for line in cat:
        print(line)

# 토끼 출력 함수
def print_rabbit():
    rabbit = [
        " (\\(\\  ",
        " ( -.-) ",
        " o_(\")(\")"
    ]
    for line in rabbit:
        print(line)

# 강아지 출력 함수
def print_dog():
    dog = [
        " / \\__",
        "(    @\\____",
        " /         O",
        "/   (_____/",
        "/_____/   U"
    ]
    for line in dog:
        print(line)

# 선택한 번호에 따라 아스키 아트를 출력하는 함수
def print_cute_ascii_art(n):
    if n == 1:
        print_cat()
    elif n == 2:
        print_rabbit()
    elif n == 3:
        print_dog()
    else:
        print("잘못 입력했습니다. 1, 2, 3 중 하나를 입력해주세요.")

# 메인 프로그램
print("그림 출력 프로그램")
print("-----------------")
print("1. 고양이")
print("2. 토끼")
print("3. 강아지")
print("-----------------")

try:
    n = int(input("선택: "))
    print_cute_ascii_art(n)
except ValueError:
    print("숫자를 입력해주세요.")
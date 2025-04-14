from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import random
import time
import os

# 크롬 드라이버 경로 지정 (적절한 경로로 수정해줘)
driver_path = '/path/to/chromedriver'  # 예: 'C:/chromedriver.exe'

# 크롬 드라이버 서비스 설정
service = Service(driver_path)
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 브라우저 창 안 띄우는 옵션
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=service, options=options)

# Spotify 차트 페이지 접속
url = 'https://charts.spotify.com/charts/view/regional-global-daily/latest'
driver.get(url)
time.sleep(5)  # 렌더링 기다리기

# 페이지 소스 가져와서 파싱
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

# 곡 리스트 수집
songs = []
entries = soup.select('div[data-testid="chart-table"] tbody tr')

for i, entry in enumerate(entries, 1):
    title = entry.select_one('td:nth-of-type(4) span').get_text(strip=True)
    artist = entry.select_one('td:nth-of-type(5) span').get_text(strip=True)
    songs.append((str(i), title, artist))

# 메뉴 출력
print("====================")
print("1. 스포티파이 100")
print("2. 스포티파이 50")
print("3. 스포티파이 10")
print("4. AI 추천 노래")
print("5. 가수 이름 검색")
print("====================")

n = input("메뉴선택(숫자입력): ")
print(f"당신이 입력한 값은? {n}")

if len(songs) == 0:
    print("차트 데이터를 불러올 수 없습니다. 웹 구조가 변경되었거나 접근이 차단되었습니다.")
else:
    if n == "1":
        print("스포티파이 100")
        for i in range(min(100, len(songs))):
            print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

    elif n == "2":
        print("스포티파이 50")
        for i in range(min(50, len(songs))):
            print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

    elif n == "3":
        print("스포티파이 10")
        for i in range(min(10, len(songs))):
            print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

    elif n == "4":
        ai_song = random.choice(songs)
        print(f"오늘의 추천곡: {ai_song[1]} - {ai_song[2]}")

    elif n == "5":
        artist_name = input("가수 이름을 입력하세요: ")
        artist_name_lower = artist_name.lower()

        matched_songs = [s for s in songs if artist_name_lower in s[2].lower()]
        if matched_songs:
            print(f"{artist_name}의 노래 리스트:")
            for s in matched_songs:
                print(f"{s[0]}. {s[1]} - {s[2]}")
        else:
            print(f"{artist_name}의 노래 리스트를 찾을 수 없습니다")

    else:
        print("1~5까지의 숫자를 입력하세요")
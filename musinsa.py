import requests
from bs4 import BeautifulSoup
import pandas as pd

# 무신사 브랜드 랭킹 URL
url = 'https://search.musinsa.com/ranking/brand'

# HTTP 요청 헤더 설정
headers = {
    'User-Agent': 'Mozilla/5.0'
}

# 페이지 요청
response = requests.get(url, headers=headers)
response.raise_for_status()  # 요청이 성공했는지 확인

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 브랜드 랭킹 리스트 선택
brands = soup.select('li.brand-list-item')

# 브랜드 정보 저장을 위한 리스트
brand_data = []

# 각 브랜드에 대해 정보 추출
for brand in brands:
    rank = brand.select_one('p.txt-num').text.strip()
    name = brand.select_one('p.brand-name').text.strip()
    brand_data.append({'순위': rank, '브랜드명': name})

# 데이터프레임 생성
df = pd.DataFrame(brand_data)

# 결과 출력
print(df)
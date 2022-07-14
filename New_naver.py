from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook

# 엑셀 파일 열기
xlsx = Workbook()

# Step1 검색할 키워드 입력
query = input('검색 키워드 입력 : ')
time.sleep(3)

# 엑셀 검색키워드 이름으로 시트 생성 후 title URL 첫 행에 만들기
xlsx.create_sheet(query)
sheet = xlsx[query]
sheet.append(['title','URL'])

# Step2. 크롬드라이버로 원하는 URL 접속
url = 'https://www.naver.com/'
driver = webdriver.Chrome()
driver.get(url)  # url 주소로 웹 브라우저 이동
time.sleep(2)

# Step3. naver 검색창에 키워드 입력 후 Enter
search = driver.find_element(By.ID,'query')
search.send_keys(query) # 검색창에 콘솔창에서 입력한 값 넣기
search.send_keys(Keys.RETURN) # 검색창 엔터

# Step4. 뉴스 탭 클릭
driver.find_element(By.XPATH,'//*[@id="main_pack"]/section[3]/div/div[3]/a').click()
time.sleep(2)

# Step5. 검색 결과 페이지에서 원하는 뉴스기사 내용 수집
all_news = driver.find_elements(By.CLASS_NAME,'news_tit')

for news in all_news:
    print(news.text)                     # 뉴스 기사
    print(news.get_attribute('href'))    # 뉴스 링크 주소
    title = news.text
    url = news.get_attribute('href')
    sheet.append([title,url])              # 위에서 엑셀파일 내 키워드 시트에 해드라인 및 URL 첨부

driver.quit()  # 작업 중인 웹브라우저 끔

del xlsx['Sheet']      # 기본 시트 삭제
filename = query + '_NewsList.xlsx'
xlsx.save(filename)     # 통합문서 저장
xlsx.close()            # 통합문서 종료
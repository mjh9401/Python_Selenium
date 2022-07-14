from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook

# 엑셀 파일 열기
xlsx = Workbook()

# 엑셀 시트 생성 및 헤더 생성
xlsx.create_sheet('서울시 공시지가')
sheet = xlsx['서울시 공시지가']
sheet.append(['공시기준','단지명','동명','호명','전용면적(㎡)','공동주택가격(원)'])
del xlsx['Sheet']

driver = webdriver.Chrome()
driver.get("https://www.realtyprice.kr/notice/town/nfSiteLink.htm")

# 서울시 선택
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/form/dl/dd/select[1]/option[1]').click()
time.sleep(1)

# 강남구 선택
driver.find_element(By.XPATH,'//*[@id="sigungu"]/option[1]').click()
time.sleep(1)

# ㄱ~ㅎ 선택 후 도로명 선택
driver.find_element(By.XPATH,'//*[@id="initialword"]/option[1]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="road"]/option[1]').click()
time.sleep(1)

# 단지명 선택
driver.find_element(By.XPATH,'//*[@id="apt"]/option').click()
time.sleep(1)

# 동 선택
driver.find_element(By.XPATH,'//*[@id="dong"]/option').click()
time.sleep(1)

# 호 선택
ho = driver.find_element(By.ID,'ho')
ho_len= ho.get_attribute("length")

for i in range(int(ho_len)):
    driver.find_element(By.XPATH,'//*[@id="ho"]/option['+str(i+1)+']').click()
    time.sleep(1)

    # 열람하기 클릭
    driver.find_element(By.CLASS_NAME,'btn-src3').click()
    time.sleep(1)

    # 2022년 공시지가 담기
    publicInfoTag = driver.find_element(By.XPATH,'//*[@id="dataList"]/tr[1]')
    publicInfo = publicInfoTag.get_attribute('outerText').replace('\t', " ").replace('\n',"")
    publicInfoList = publicInfo.split(' ')

    gongSiGiJun = publicInfoList[0]
    danJiMyung = publicInfoList[1]
    dongMyung = publicInfoList[2]
    hoMyung = publicInfoList[3]
    junyoungMyunJuk= publicInfoList[4]
    gongDongJuTekGagyuk = publicInfoList[5]

    sheet.append([gongSiGiJun,danJiMyung,dongMyung,hoMyung,junyoungMyunJuk,gongDongJuTekGagyuk])  # 엑셀시트에 공시지가 정보 첨부

driver.quit()
xlsx.save('Test.xlsx')
xlsx.close()

# 시군구 데이터들 25개
# sigungu= driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/form/dl/dd/select[2]/option[]')
# number = 1

# while True :
#     driver.find_element(By.XPATH,'//*[@id="sigungu"]/option['+str(number)+']').click()
#     number = number +1
#     time.sleep(1)
    
#     if number > 25:
#         break


# driver.close()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook, load_workbook


driver = webdriver.Chrome()       # 위에서 만든 크롬 옵션 적용하여 크롬드라이버 생성   
driver.get("https://www.realtyprice.kr/notice/town/nfSiteLink.htm")     

# 기존 엑셀 파일 가져오기
wb =load_workbook(filename='부동산공시가격.xlsx')

# 엑셀 시트 선택
sheet = wb['강남구']

# 서울시 선택
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/form/dl/dd/select[1]/option[1]').click()
time.sleep(2)

# 강남구 선택
driver.find_element(By.XPATH,'//*[@id="sigungu"]/option[1]').click()
time.sleep(2)

# ㄱ~ㅎ 선택 후 도로명 선택
driver.find_element(By.XPATH,'//*[@id="initialword"]/option[1]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="road"]/option[8]').click()
time.sleep(2)


# 단지명 선택
driver.find_element(By.XPATH,'//*[@id="apt"]/option[12]').click()
time.sleep(2)

# 동 선택
driver.find_element(By.XPATH,'//*[@id="dong"]/option').click()
time.sleep(2)


# 호 선택
ho = driver.find_element(By.ID,'ho')
ho_len= ho.get_attribute("length")

for i in range(int(ho_len)):
    try:
        driver.find_element(By.XPATH,'//*[@id="ho"]/option['+str(i+1)+']').click()
        time.sleep(2)

        # 열람하기 클릭
        driver.find_element(By.CLASS_NAME,'btn-src3').click()
        time.sleep(2)

    except:
        pass

    # 2022년 공시지가 담기
    address = driver.find_element(By.XPATH,'//*[@id="spanFullAddrName"]').get_attribute('outerText')
    addrList = address.split('(')
    adress = addrList[0]

    publicInfoTag = driver.find_element(By.XPATH,'//*[@id="dataList"]/tr[1]')
    publicInfo = publicInfoTag.get_attribute('outerText').replace('\t', " ").replace('\n',"")
    publicInfoList = publicInfo.split(' ')

    gongSiGiJun = publicInfoList[0]
    danJiMyung = publicInfoList[1]
    dongMyung = publicInfoList[2]
    hoMyung = publicInfoList[3]
    junyoungMyunJuk= publicInfoList[4]
    gongDongJuTekGagyuk = publicInfoList[5]
                     
    chuengSu = hoMyung
    if len(hoMyung) == 3:
        chuengSu = hoMyung[:1]
    elif len(hoMyung) == 4:
        chuengSu == hoMyung[:2]
    print(len(chuengSu))
    print(chuengSu)

    sheet.append([adress,gongSiGiJun,danJiMyung,dongMyung,hoMyung,chuengSu,junyoungMyunJuk,gongDongJuTekGagyuk])  # 엑셀시트에 공시지가 정보 첨부
    wb.save('부동산공시가격.xlsx')

driver.quit()
wb.close()

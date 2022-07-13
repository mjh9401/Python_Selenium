from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.realtyprice.kr/notice/town/nfSiteLink.htm")
# 서울시 선택
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/form/dl/dd/select[1]/option[1]').click()
time.sleep(3)
# 시군구 데이터들 25개
# sigungu= driver.find_elements(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/form/dl/dd/select[2]/option[]')
number = 1

while True :
    driver.find_element(By.XPATH,'//*[@id="sigungu"]/option['+str(number)+']').click()
    number = number +1
    time.sleep(1)
    
    if number > 25:
        break


# driver.close()

from cgitb import text
from operator import contains
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.realtyprice.kr/notice/town/nfSiteLink.htm")
sido = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/form/dl/dd/select[1]/option[1]').click()
sigungu = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/form/dl/dd/select[2]/option[contains(text(),"강남구")]')


# driver.close()

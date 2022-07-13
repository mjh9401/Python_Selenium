from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser =webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')

browser.switch_to.frame('iframeResult')

# car에 해당하는 element를 찾고, 드롭다운 내부에 있는 2번쨰 옵션을 선택
# elem = browser.find_element(By.XPATH,'//*[@id="cars"]/option[2]')
# elem.click()

# 완전히 일치하는 텍스트 값을 통해서 선택하는 방법
# elem = browser.find_element(By.XPATH,'//*[@id="cars"]/option[text() = "Audi"]')
# elem.click()

# 텍스트 값이 부분 일치하는 항목 선택하는 항목
elem = browser.find_element(By.XPATH,'//*[@id="cars"]/option[contains(text(),"Au")]')
elem.click()

# select태그에 있는 옵션의 총 갯수 = select의 길이
select = browser.find_element(By.XPATH,'//*[@id="cars"]')
length = select.get_attribute("length")
print(length)

time.sleep(5)


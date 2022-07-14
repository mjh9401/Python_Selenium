from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook

# chrome_option = webdriver.ChromeOptions()              # webdriver의 크롬 옵션 객체 생성
# chrome_option.add_experimental_option("debuggerAddress", "127.0.0.1:9222") # 크롬 디버거 모드 옵션 추가
driver = webdriver.Chrome()       # 위에서 만든 크롬 옵션 적용하여 크롬드라이버 생성   
driver.get("https://www.realtyprice.kr/notice/town/nfSiteLink.htm")     

# 엑셀 파일 열기
xlsx = Workbook()
# 기존 Sheet 삭제
del xlsx['Sheet']


# 엑셀 시트 생성 및 헤더 생성

xlsx.create_sheet('강남구')
sheet = xlsx['강남구']
sheet.append(['공시기준','단지명','동명','호명','전용면적(㎡)','공동주택가격(원)'])

# 서울시 선택
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/form/dl/dd/select[1]/option[1]').click()
time.sleep(0.5)

# 강남구 선택
driver.find_element(By.XPATH,'//*[@id="sigungu"]/option[1]').click()
time.sleep(0.5)

# ㄱ~ㅎ 선택 후 도로명 선택
driver.find_element(By.XPATH,'//*[@id="initialword"]/option[1]').click()
time.sleep(0.5)
driver.find_element(By.XPATH,'//*[@id="road"]/option[2]').click()
time.sleep(0.5)

cnt = 0

while True :   
    # 단지명 선택
    danji = driver.find_element(By.ID,'apt')
    danji_len = danji.get_attribute("length")
    print('카운트 값 : '+ str(cnt))
    print('선택박스 길이 : '+ str(danji_len))

    if int(danji_len) <= cnt :
        break

    if int(danji_len) == 1:
        driver.find_element(By.XPATH,'//*[@id="apt"]/option').click()
        time.sleep(0.5)

    elif int(danji_len) > 1:
        for i in range(int(danji_len)):
            driver.find_element(By.XPATH,'//*[@id="apt"]/option['+str(i+1)+']').click()
            time.sleep(2)

            # 동 선택
            dong =driver.find_element(By.ID,'dong')
            dong_len = dong.get_attribute("length")

            if int(dong_len) == 1:
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

                cnt = cnt + 1    
            
            elif int(dong_len) > 1:
                for i in range(int(dong_len)):
                    driver.find_element(By.XPATH,'//*[@id="dong"]/option['+str(i+1)+']').click()
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

                    cnt = cnt + 1


    # 동 선택
    dong =driver.find_element(By.ID,'dong')
    dong_len = dong.get_attribute("length")

    if int(dong_len) == 1:
        driver.find_element(By.XPATH,'//*[@id="dong"]/option').click()

    elif int(dong_len) >= 2:
        for i in range(int(dong_len)):
            driver.find_element(By.XPATH,'//*[@id="dong"]/option['+str(i+1)+']').click()
            time.sleep(0.5)

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

            cnt = cnt + 1

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

    cnt = cnt + 1

driver.quit()
xlsx.save('Test.xlsx')
xlsx.close()

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook, load_workbook


# chrome_option = webdriver.ChromeOptions()              # webdriver의 크롬 옵션 객체 생성
# chrome_option.add_experimental_option("debuggerAddress", "127.0.0.1:9222") # 크롬 디버거 모드 옵션 추가
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
driver.find_element(By.XPATH,'//*[@id="road"]/option[31]').click()
time.sleep(2)

# 단지명 선택
danji = driver.find_element(By.ID,'apt')
danji_len = danji.get_attribute("length")




# 단지 1개일때
if int(danji_len) == 1:
    driver.find_element(By.XPATH,'//*[@id="apt"]/option').click()
    time.sleep(2)

    # 동 길이
    dong_len = driver.find_element(By.ID,'dong').get_attribute("length")
    
    # 동 1개일 때
    if int(dong_len) == 1:
        driver.find_element(By.XPATH,'//*[@id="dong"]/option').click()
        time.sleep(2)

        # 호 선택
        ho_len = driver.find_element(By.ID,'ho').get_attribute("length")
        
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
            now = datetime.now()

            chuengSu = hoMyung 
            if len(hoMyung) == 3:
                chuengSu = hoMyung[:1]
            else :
                chuengSu == hoMyung[:2]

            sheet.append([adress,gongSiGiJun,danJiMyung,dongMyung,hoMyung,chuengSu,junyoungMyunJuk,gongDongJuTekGagyuk,now.date()])  # 엑셀시트에 공시지가 정보 첨부
            wb.save('부동산공시가격.xlsx')

    # 동 여러 개일때
    elif int(dong_len) > 1:
        for i in range(int(dong_len)):
            driver.find_element(By.XPATH,'//*[@id="dong"]/option['+str(i+1)+']').click()
            time.sleep(2)

            # 호 선택
            ho_len = driver.find_element(By.ID,'ho').get_attribute("length")
        
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
                now = datetime.now()

                chuengSu = hoMyung 
                if len(hoMyung) == 3:
                    chuengSu = hoMyung[:1]
                else :
                    chuengSu == hoMyung[:2]

                sheet.append([adress,gongSiGiJun,danJiMyung,dongMyung,hoMyung,chuengSu,junyoungMyunJuk,gongDongJuTekGagyuk,now.date()])  # 엑셀시트에 공시지가 정보 첨부
                wb.save('부동산공시가격.xlsx')




# 단지 여러 개일때
elif int(danji_len) > 1:

    for i in range(int(danji_len)):
        driver.find_element(By.XPATH,'//*[@id="apt"]/option['+str(i+1)+']').click()
        time.sleep(2)

        # 동 길이
        dong_len = driver.find_element(By.ID,'dong').get_attribute("length")

        # 동 한 개일 경우
        if int(dong_len) == 1:
            driver.find_element(By.XPATH,'//*[@id="dong"]/option').click()
            time.sleep(2)

            # 호 선택
            ho_len = driver.find_element(By.ID,'ho').get_attribute("length")
            
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
                now = datetime.now()

                chuengSu = hoMyung 
                if len(hoMyung) == 3:
                    chuengSu = hoMyung[:1]
                else :
                    chuengSu == hoMyung[:2]

                sheet.append([adress,gongSiGiJun,danJiMyung,dongMyung,hoMyung,chuengSu,junyoungMyunJuk,gongDongJuTekGagyuk,now.date()])  # 엑셀시트에 공시지가 정보 첨부
                wb.save('부동산공시가격.xlsx')

        # 동 여러 개일 경우
        elif int(dong_len) > 1:
            for i in range(int(dong_len)):
                driver.find_element(By.XPATH,'//*[@id="dong"]/option['+str(i+1)+']').click()
                time.sleep(2)

                # 호 선택
                ho_len = driver.find_element(By.ID,'ho').get_attribute("length")
                
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
                    now = datetime.now()

                    chuengSu = hoMyung 
                    if len(hoMyung) == 3:
                        chuengSu = hoMyung[:1]
                    else :
                        chuengSu == hoMyung[:2]

                    sheet.append([adress,gongSiGiJun,danJiMyung,dongMyung,hoMyung,chuengSu,junyoungMyunJuk,gongDongJuTekGagyuk,now.date()])  # 엑셀시트에 공시지가 정보 첨부
                    wb.save('부동산공시가격.xlsx')

# 크롬 드라이버 종료
driver.quit()
# openpyxl 닫기
wb.close()

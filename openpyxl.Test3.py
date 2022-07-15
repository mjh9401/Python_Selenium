from openpyxl import Workbook, load_workbook

# 엑셀 파일 불러오기
wb = load_workbook(filename='부동산공시가격.xlsx')

# 엑셀 값 넣음
sheet = wb['강남구']
sheet.append(['서울','2022.01.01','달나라','동 없음','호 없음','층 없음','0'])

wb.save("부동산공시가격.xlsx")

wb.close()
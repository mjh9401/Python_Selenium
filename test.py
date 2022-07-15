from posixpath import split


# address = '서울특별시 강남구 가로수길 55-6(강남구 신사동   533-15)'
# addrList = address.split('(')
# print(addrList)
# address = addrList[0]
# print(address)

nubmer = '1603'
# print(len(nubmer))  # 문자열 구하기

if len(nubmer) == 3:
    print(nubmer[:1])
elif len(nubmer) ==4:
    print(nubmer[:2])       

# print(nubmer[:1])


# for i in range(25,155):
#     print(i)


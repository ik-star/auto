import time
import json
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome("C:\selenium\chromedriver_win32\chromedriver.exe")

# 위메프 페이지 열기
driver.get("https://front.wemakeprice.com")

# sleep 삭제 -> WebDriverWait 사용하기
# 검색 입력 필드 찾을 때 까지 대기
searchInputBox = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "_searchKeyword"))
)

# 해당 검색창에 '라면'값 전달
searchInputBox.send_keys("라면")

# 검색 버튼 클릭
searchBtn = driver.find_element_by_xpath('//*[@id="_searchKeywordBtn"]')
searchBtn.click()

# 검색 리스트 찾을 때 까지 대기
searchList = WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "list_conts_wrap"))
)

prodList = []

for element in searchList:
    index = len(prodList)
    title = element.find_element_by_class_name("info_text").text
    label = element.find_elements_by_class_name("item_noti")

    # 배열의 크기가 1보다 작으면(찾은 값이 없으면)
    # 라벨 정보는 있거나 없어서 분기처리 참고해서 작성함 ㅜㅜ
    if len(label) < 1 or label == "":
        label = None
    else:
        if label[0].text != "":
            label = label[0].text
        else:  # 라벨 자체는 존재하는데 값이 없을때도 있는것 같아서, 결과가 자꾸 "" 빈값으로 나와 한번 더 분기해줌
            label = None
    # 카탈로그 품목 정보ctl_prd_info
    ctlProdInfo = element.find_elements_by_class_name("ctl_prd_info")
    if len(ctlProdInfo) < 1 or ctlProdInfo == "":
        ctlProdInfo = None
    else:
        if ctlProdInfo[0].text != "":
            ctlProdInfo = ctlProdInfo[0].text
        else:
            ctlProdInfo = None

    # 별정 정보 area_star
    areaStar = element.find_elements_by_class_name("area_star")
    if len(areaStar) < 1 or areaStar == "":
        areaStar = None
    else:
        if areaStar[0].text != "":
            areaStar = areaStar[0].text
        else:
            areaStar = None

    # 구매 또는 판매처 정보 purchase
    purchase = element.find_elements_by_class_name("purchase")
    if len(purchase) < 1 or purchase == "":
        purchase = None
    else:
        if purchase[0].text != "":
            purchase = purchase[0].text
        else:
            purchase = None

    # 배송비 정보 price_deli_txt
    priceDeliTxt = element.find_elements_by_class_name("price_deli_txt")
    if len(priceDeliTxt) < 1 or priceDeliTxt == "":
        priceDeliTxt = None
    else:
        if priceDeliTxt[0].text != "":
            priceDeliTxt = priceDeliTxt[0].text
        else:
            priceDeliTxt = None

    # 할인 혜택가 정보 price_text
    priceText = element.find_elements_by_class_name("price_text")
    if len(priceText) < 1 or priceText == "":
        priceText = None
    else:
        if priceText[0].text != "":
            priceText = priceText[0].text
        else:
            priceText = None

    # 할인율 정보 price_sale
    priceSale = element.find_elements_by_class_name("price_sale")
    if len(priceSale) < 1 or priceSale == "":
        priceSale = None
    else:
        if priceSale[0].text != "":
            priceSale = priceSale[0].text
        else:
            priceSale = None

    # 가격 정보
    priceNum = element.find_element_by_tag_name("em").text

    info = {
        "index": index,
        "상품명": title,
        "라벨 정보": label,
        "카탈로그 품목 정보": ctlProdInfo,
        "별점 정보": areaStar,
        "구매나 판매처 정보": purchase,
        "배송 정보": priceDeliTxt,
        "할인혜택가 정보": priceText,
        "할인율": priceSale,
        "상품 금액": priceNum,
    }
    prodList.append(info)

for i in prodList:
    print(i)


# WebDriver를 종료 (브라우저 닫기)
driver.quit()

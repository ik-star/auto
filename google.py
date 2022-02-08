import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome("C:\selenium\chromedriver_win32\chromedriver.exe")

# 위메프 페이지 열기
driver.get("https://front.wemakeprice.com")
time.sleep(2)

# 검색창에서 검색 하기
element = driver.find_element_by_id("_searchKeyword")
element.send_keys("라면")
driver.find_element_by_xpath('//*[@id="_searchKeywordBtn"]').click()
time.sleep(2)

# 검색 완료 내용 크롤링하기
searchProdElement = driver.find_elements_by_class_name("list_conts_wrap")

# # 이쁘게 안하고 전부 엘리먼트 가져오는 코드ㅠㅠ
# for item in searchProdElement:
#     elements = item.text
#     print("호잇" + elements)

# 하나씩 가져오는 코드 ㅠㅠ
for item in searchProdElement:
    # 엘리먼트 없는 경우도 있어서, 예외처리 진행
    title = item.find_element_by_class_name("info_text").text
    priceInfo = item.find_element_by_class_name("price_info").text

    try:
        deliveryDate = item.find_element_by_class_name("item_noti").text
        starPoint = item.find_element_by_class_name("area_star").text
        purchase2 = item.find_element_by_class_name("purchase").text
        priceText = item.find_element_by_class_name("price_text").text

    except NoSuchElementException:
        deliveryDate = "발송예정일 없음"
        starPoint = "별점 없음"
        purchase2 = "구매수량 또는 판매처 수량 없음"
        priceText = "원가 정보 없음"

    print("상품명 : " + title)
    print("발송 or 쿠폰 정보 : " + deliveryDate)
    print("별점 정보 : " + starPoint)
    print("구매수량 또는 판매처 정보 : " + purchase2)  # 왜 판매처 수량은 못가져 오는지 모르겠음..
    print("원가 정보 : " + priceText)  # 얘는 왜 공란으로 노출되는겨..ㅠㅠ
    print("금액 정보 : " + priceInfo)
    print("--------------------------------------------------------------")

time.sleep(3)

# WebDriver를 종료 (브라우저 닫기)
driver.quit()

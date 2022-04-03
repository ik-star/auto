from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome("C:\selenium\chromedriver_win32\chromedriver.exe")
driver.get("https://front.wemakeprice.com/main")

# element 찾을때까지 5초간 0.5초마다 트라이
search_box = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@class="lay_ico ui_input_search"]/input')
    )
)
search_box.send_keys("라면")

search_button = driver.find_element_by_xpath('//*[@class="btn_search"]/button')
search_button.click()

# element 찾을때까지 5초간 0.5초마다 트라이
search_box_list = WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "list_conts_wrap"))
)

# 결과 저장된 변수
deal_info_list = []

# 리스트 총 개수 몇개인지 확인
print("list len : {0}".format(len(search_box_list)))

# index를 사용하기 위해 enumerate사용
for i, element in enumerate(search_box_list):
    name = element.find_element_by_class_name("info_text").text
    price = element.find_element_by_xpath(
        '//*[@class="price_info"]//*[@class="num"]'
    ).text
    ship_fee = element.find_element_by_class_name("price_deli_txt").text

    # 배송날짜가 있는지 없는지 확인 하기위해 find_elements로 배열로 받아옴
    ship_date = element.find_elements_by_class_name("txt_noti")

    # 배열의 크기가 1보다 작으면(찾은 값이 없으면)
    if len(ship_date) < 1:
        # 배송날짜에 None입력
        ship_date = None
    else:
        # 배송날짜 가져오기
        # ship_date는 배열로 받아 왔으니 ship_date 뒤에 배열 중 어떤 값인지 적어줘야함
        # 여기선 리스트 안에 price_deli_txt이름의 클래스 명은 1개 뿐이므로 무조건 0번째를 가져옴
        # 만약 price_deli_txt 클래스명이 여러개면 [0]을 쓰면 안됨
        ship_date = ship_date[0].text

    # 사전 형식으로 저장
    info = {
        "index": i,
        "name": name,
        "price": price,
        "shipFee": ship_fee,
        "shipDate": ship_date,
    }

    # 저장된 사전 형식을 배열에 넣기
    deal_info_list.append(info)


# 수집한 엘리먼트 정보 print
for info in deal_info_list:
    print(info)

print("done")

driver.quit()

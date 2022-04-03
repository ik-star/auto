from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome("C:\selenium\chromedriver_win32\chromedriver.exe")
driver.get("https://front.wemakeprice.com/main")


search_box = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@class="lay_ico ui_input_search"]/input')
    )
)
search_box.send_keys("라면")


search_button = driver.find_element_by_xpath('//*[@class="btn_search"]/button')
search_button.click()

search_box_list = WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "list_conts_wrap"))
)

deal_info_list = []

for element in search_box_list:
    i = 0
    name = element.find_element_by_class_name("info_text").text
    price = element.find_element_by_xpath(
        '//*[@class="price_info"]//*[@class="num"]'
    ).text
    ship_fee = element.find_elements_by_class_name("price_deli_txt").
    info = {"index": i, "name": name, "price": price, "shipFee": ship_fee}
    # print('상품명 : {0}'.format(name))
    # print('가격 : {0}'.format(price))
    # print('배송비 : {0}'.format(ship_fee))
    deal_info_list.append(info)
    i += 1

print(deal_info_list[0])
print("done")

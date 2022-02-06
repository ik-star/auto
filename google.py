import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome("C:\selenium\chromedriver_win32\chromedriver.exe")

# 위메프 페이지 열기
driver.get("https://front.wemakeprice.com")
time.sleep(4)

# 검색창에서 검색 하기


# 검색 완료 내용 크롤링하기


# WebDriver를 종료 (브라우저 닫기)
driver.quit()

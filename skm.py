# skm.py
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import chrome

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
#cookies
driver.get("http://www.skm.pkp.pl/")
akceptuj = driver.find_element_by_class_name("button")
akceptuj.click()

driver.implicitly_wait(5)

#stacja 1
stacja1 = driver.find_element_by_class_name("select2-selection__placeholder")
stacja1.click()

driver.implicitly_wait(5)

ENTER = u'\ue007'

wejherowo =driver.find_element_by_class_name("select2-search__field")
wejherowo.send_keys("Wejherowo Nanice", ENTER)

driver.implicitly_wait(5)

#stacja 2

stacja2 = driver.find_element_by_class_name("select2-selection__placeholder")
stacja2.click()

reda =driver.find_element_by_class_name("select2-search__field")
reda.send_keys("REDA", ENTER)

driver.implicitly_wait(5)

#godzina

BCK = u'\ue003'

time = driver.find_element_by_class_name("time")
time.click()
time.send_keys(BCK, BCK, BCK, BCK, "1500", ENTER)

driver.implicitly_wait(5)

#wyszukaj

wy = driver.find_element_by_xpath("//input[@value='Wyszukaj połączenie'][@type='submit']")
wy.click()

#dane

driver.implicitly_wait(5)

main = driver.find_element_by_id("center")
print(main.text)




driver.quit()






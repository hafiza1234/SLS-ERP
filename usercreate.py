from selenium import webdriver
import time
browser = webdriver.Chrome("C:\SE\chromedriver.exe")
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
time.sleep(2)
browser.maximize_window()
browser.get('http://139.162.35.76:8070/login')
time.sleep(3)
browser.find_element_by_name("email").send_keys("super@skylarksoft.com")
time.sleep(3)
browser.find_element_by_name("password").send_keys("Staging!Er$#P@2021")
time.sleep(3)
browser.find_element_by_name("login").click()
browser = browser.find_element_by_xpath("//span[@class='nav-text'][contains(.,'General Settings')]")
browser.location_once_scrolled_into_view
browser.click()
time.sleep(2)
browser.find_element_by_xpath("(//span[contains(.,'Users')])[2]").click()
time.sleep(2)
browser.find_element_by_xpath("//h2[contains(.,'User List')]")
browser.click()
time.sleep(2)



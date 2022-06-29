from selenium import webdriver
import time
browser = webdriver.Chrome("C:\SE\chromedriver.exe")
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
time.sleep(2)
browser.maximize_window()
browser.get('http://139.162.35.76:8070/login')
time.sleep(2)
browser.find_element_by_name("email").send_keys("super@skylarksoft.com")
time.sleep(2)
browser.find_element_by_name("password").send_keys("Staging!Er$#P@2021")
time.sleep(2)
browser.find_element_by_name("login").click()
time.sleep(2)
browser.find_element_by_xpath("(//span[@class='nav-text'][contains(.,'Marketing')])[1]").click()
time.sleep(2)
browser.find_element_by_xpath("//span[contains(.,'Sales Target Determination')]").click()
time.sleep(2)
browser.find_element_by_xpath("(//i[@class='fa fa-times'])[13]").click()
time.sleep(2)
browser.find_element_by_xpath("(//button[contains(.,'Yes')])[1]").click()
time.sleep(2)
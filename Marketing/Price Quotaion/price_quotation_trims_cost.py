from selenium import webdriver
import time
browser = webdriver.Chrome("C:\SE\chromedriver.exe")
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
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
browser.find_element_by_xpath("(//span[@class='nav-text'][contains(.,'Price Quotation')])[1]").click()
time.sleep(2)
browser.find_element_by_xpath("(//i[contains(@class,'fa fa-edit')])[1]").click()
time.sleep(2)
browser.find_element_by_xpath("//button[contains(.,'Update')]").click()
time.sleep(2)
browser.find_element_by_xpath("//button[contains(.,'Costing Section')]").click()
time.sleep(2)
a = browser.find_element_by_xpath("//input[@name='trims_cost']")
action = ActionChains(browser)
action.double_click(a).perform()
time.sleep(3)
a1 = Select(browser.find_element_by_id("group_id"))
a1.select_by_index(2)
time.sleep(2)
browser.find_element_by_xpath("//input[@id='item_description']").send_keys("Good")
time.sleep(2)
browser.find_element_by_xpath("//input[@id='cons_gmts']").send_keys(".05")
time.sleep(2)
browser.find_element_by_xpath("//input[contains(@id,'percent')]").send_keys("15")
time.sleep(2)
browser.find_element_by_xpath("(//input[@step='4'])[2]").send_keys(".435")
time.sleep(2)
a2 = Select(browser.find_element_by_id("nominated_supplier_id"))
a2.select_by_index(1)
time.sleep(2)
browser.find_element_by_xpath("//button[@id='not_is_edit_mode']").click()
time.sleep(4)
browser.find_element_by_xpath("//span[@id='select2-group_id-container']").click()
time.sleep(2)
browser.find_element_by_xpath("(//li[contains(.,'Fabric')])[1]").click()
time.sleep(5)
browser.find_element_by_xpath("(//button[@type='button'])[2]").click()
time.sleep(2)
browser.find_element_by_xpath("//a[contains(.,'Save & Go Back')]").click()
time.sleep(2)
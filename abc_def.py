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
browser.find_element_by_xpath("//a[contains(.,'New Entry')]").click()
time.sleep(2)
browser.find_element_by_xpath("//input[contains(@id,'revised_no')]").send_keys("002")
time.sleep(2)
browser.find_element_by_xpath("//input[@id='location']").send_keys("Mirpur")
a1 = Select(browser.find_element_by_id("buyer_id"))
a1.select_by_index(2)
a2 = Select(browser.find_element_by_name("product_department_id"))
a2.select_by_index(3)
time.sleep(2)
browser.find_element_by_xpath("//input[@id='style_name']").send_keys("new_kurti")
time.sleep(2)
browser.find_element_by_xpath("//input[contains(@id,'style_desc')]").send_keys("good")
time.sleep(2)
browser.find_element_by_xpath("//input[@id='offer_qty']").send_keys("200")
time.sleep(3)
a3 = Select(browser.find_element_by_id("season_id"))
a3.select_by_index(3)
a4 = Select(browser.find_element_by_name("garment_item_val"))
a4.select_by_index(2)
time.sleep(2)
browser.find_element_by_xpath("(//input[@type='text'])[19]").send_keys("1")
time.sleep(1)
browser.find_element_by_xpath("//input[@name='smv_val']").send_keys("7")
time.sleep(2)
browser.find_element_by_xpath("(//i[@class='fa fa-plus'])[2]").click()
time.sleep(2)
browser.find_element_by_xpath("(//button[@type='submit'])[1]").click()
time.sleep(7)
browser.find_element_by_xpath("//button[contains(.,'Costing Section')]").click()
time.sleep(2)
a = browser.find_element_by_xpath("//input[@name='fab_cost']")
action = ActionChains(browser)
action.double_click(a).perform()
time.sleep(3)
a5 = Select(browser.find_element_by_id("color_type_id"))
a5.select_by_index(1)
time.sleep(2)
a7 = Select(browser.find_element_by_id("fabric_composition_id"))
a7.select_by_index(2)
time.sleep(2)
browser.find_element_by_xpath("//input[contains(@id,'code')]").send_keys("2345")
time.sleep(2)
a9 = Select(browser.find_element_by_id("supplier_id"))
a9.select_by_index(1)
time.sleep(2)
browser.find_element_by_xpath("//input[@id='gsm']").send_keys("160")
time.sleep(2)
browser.find_element_by_xpath("//span[@title='Select']").click()
time.sleep(3)
browser.find_element_by_xpath("//li[contains(.,'Pcs')]").click()
time.sleep(2)
browser.find_element_by_xpath("//span[@id='select2-body_part_id-container']").click()
time.sleep(2)
browser.find_element_by_xpath("(//li[@role='option'])[2]").click()
time.sleep(2)
b = browser.find_element_by_xpath("//input[@id='fabric_cons']")
action = ActionChains(browser)
action.double_click(b).perform()
time.sleep(2)
browser.find_element_by_xpath("//input[@id='gmts_size']").send_keys("Large")
time.sleep(2)
browser.find_element_by_xpath("//input[@id='dia']").send_keys("68")
time.sleep(2)
browser.find_element_by_xpath("//input[@id='cons']").send_keys("160")
time.sleep(2)
browser.find_element_by_xpath("//input[@id='process_loss']").send_keys(".1")
time.sleep(2)
browser.find_element_by_xpath("(//input[@id='rate'])[2]").send_keys("2")
time.sleep(5)
browser.find_element_by_xpath("(//button[@type='button'])[5]").click()
time.sleep(10)
browser.find_element_by_xpath("(//button[@type='button'])[4]").click()
time.sleep(20)
browser.find_element_by_xpath("(//i[contains(@class,'fa fa-plus')])[3]").click()
time.sleep(10)


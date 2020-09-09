print("hello")
from selenium import webdriver
import time

item_name = 'hello'
area = "Gilbert"
zip="85234"
postingbody = ""
manufacturer = ''
model = ''
email = ''
phone_num = ''
name = ''
street = ''
street1 = ''
price = ''

driver = webdriver.Chrome('C:/Users/hwank/PycharmProjects/untitled/Craiglistbot/chromedriver.exe')

driver.get("https://phoenix.craigslist.org/")

step1 = driver.find_element_by_link_text('create a posting')
step1.click()
driver.find_element_by_css_selector("input[type='radio'][value='2']").click()
time.sleep(1.2)
driver.find_element_by_css_selector("input[type='radio'][value='fso']").click()
time.sleep(13)

driver.find_element_by_id("PostingTitle").send_keys(item_name)
driver.find_element_by_id("GeographicArea").send_keys(area)
driver.find_element_by_id("postal_code").send_keys(zip)
driver.find_element_by_id("PostingBody").send_keys(postingbody)
driver.find_element_by_name("sale_manufacturer").send_keys(manufacturer)
driver.find_element_by_name("price").send_keys(price)
driver.find_element_by_name("sale_model").send_keys(model)
driver.find_element_by_name("FromEMail").send_keys(email)
driver.find_element_by_name("show_phone_ok").click()
driver.find_element_by_name("contact_text_ok").click()
driver.find_element_by_name("contact_phone").send_keys(phone_num)
driver.find_element_by_name("contact_name").send_keys(name)
driver.find_element_by_name("city").send_keys(area)
driver.find_element_by_name("go").click()
driver.find_element_by_name("cryptedStepCheck").click()
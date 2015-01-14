from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

username = "random1122"
email = "random1122@yahooo.com"
password = "chiatay1122"
driver = webdriver.Firefox()
mouse = webdriver.ActionChains(driver)    

driver.get("https://github.com/login")

element = driver.find_element_by_id("login_field")
element.send_keys(username)

element = driver.find_element_by_id("password")
element.send_keys(password)
element.submit()


driver.get("https://github.com/nguyenph88/")
#driver.get("https://github.com/users/follow?target=nguyenph88")
#element = driver.find_element_by_xpath("//a[@id='AddToCartButton']")
#mouse.move_to_element(element).click().perform()
element = driver.find_element_by_class_name("js-toggler-form")
element.submit()

driver.get("https://github.com/nguyenph88/AutoDropBox")

element = driver.find_element_by_xpath("//form[@action='/nguyenph88/AutoDropBox/star']")
element.submit()

driver.close()
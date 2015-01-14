'''
Auto create new github user
'''
from selenium import webdriver
import string, random

number_of_account = 10

for i in range(0, number_of_account):
	username = ''.join(random.choice(string.ascii_lowercase) for i in range((7)))
	email = username + "@gmail.com"
	password = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(7)])

	#driver = webdriver.Firefox()
	driver = webdriver.PhantomJS('./Phantomjs.exe')
	driver.get("https://github.com/join")

	element = driver.find_element_by_id("user_login")
	element.send_keys(username)

	element = driver.find_element_by_id("user_email")
	element.send_keys(email)

	element = driver.find_element_by_id("user_password")
	element.send_keys(password)

	element = driver.find_element_by_id("user_password_confirmation")
	element.send_keys(password)

	element.submit()

	with open("users.txt", "a") as myfile:
	    myfile.write(username + "|" + password + "\n")

	print username + "|" + password + "\n"
	driver.quit()
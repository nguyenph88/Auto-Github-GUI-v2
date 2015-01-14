import wx, sys, thread, MainFormAG
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class AutoGithubTool(MainFormAG.MainFrame):
	#constructor
	def __init__(self,parent):
		#initialize parent class
		MainFormAG.MainFrame.__init__(self,parent)

	def buttonStartEvent(self, event):
		self.isFollow = self.boxFollow.GetValue()
		self.isStar = self.boxStar.GetValue()
		self.isFork = self.boxFork.GetValue()
		self.quantity = self.fieldQuantity.GetValue()
		self.profile = self.fieldProfile.GetValue()
		self.repos = [x.strip() for x in self.fieldRepos.GetValue().split(',')]
		self.accountList = self.getAccountList()
		self.profile_user = self.profile.split("/")[3]

		# ignore the sanity check that quanlity > num account
		for i in range(0, int(self.quantity)):
			self.start(i)
			#thread.start_new_thread( self.start, ("i",) )

		self.statusBar.SetStatusText("Done!")

	def getAccountList(self):
		return [line.strip() for line in open("users.txt")]

	def start(self, i):
		driver = webdriver.Firefox()
		parts = self.accountList[i].split("|")
		username = parts[0]
		password = parts[1]
		self.doLogin(driver, username, password)
		if self.isFollow:
			self.doFollow(driver)
		if self.isStar:
			self.doStar()
		if self.isFork:
			self.doFork()
		
		driver.close()

	def doLogin(self, driver, username, password):
		self.statusBar.SetStatusText("Login:" + username + " / " + password)
		driver.get("https://github.com/login")
		element = driver.find_element_by_id("login_field")
		element.send_keys(username)
		element = driver.find_element_by_id("password")
		element.send_keys(password)
		element.submit()

	def doFollow(self, driver):
		self.statusBar.SetStatusText("Following " + self.profile)
		driver.get(self.profile)
		element = driver.find_element_by_class_name("js-toggler-form")
		element.submit()

	def doStart(self):
		for repo in self.repos:
			self.statusBar.SetStatusText("Staring: " + repo)
			driver.get(self.profile + repo)
			xpath = "//form[@action='/" + self.profile_user + "/" + repo + "/star']"
			element = driver.find_element_by_xpath(xpath)
			element.submit()

	def doFork():
		pass




###########################################
# DO NOT CHANGE ANYTHING BELOW THIS LINE  #
###########################################
#mandatory in wx, create an app, True stands for not deteriction stdin/stdout

app = wx.App()
import MainFormAG

frame = AutoGithubTool(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()
'''
lines = [line.strip() for line in open("users.txt")]
for line in lines:
	if ("|" in line) or (":" in line):
		parts = line.split("|")
		username = parts[0]
		password = parts[1]
		print "User: " + username + " -- Pass: " + password
'''
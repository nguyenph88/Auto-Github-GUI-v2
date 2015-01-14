import wx, sys, thread, MainFormAG
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class AutoGithubTool(MainFormAG.MainFrame):
	#constructor
	def __init__(self,parent):
		#initialize parent class
		MainFormAG.MainFrame.__init__(self,parent)
		self.driver = webdriver.Firefox()

	def buttonStartEvent(self, event):
		self.isFollow = self.boxFollow.GetValue()
		self.isStar = self.boxStar.GetValue()
		self.isFork = self.boxFork.GetValue()
		self.quantity = self.fieldQuantity.GetValue()
		self.profile = self.fieldProfile.GetValue()
		self.repos = self.fieldRepos.GetValue()
		self.accountList = self.getAccountList()

		self.start()

	def getAccountList(self):
		return [line.strip() for line in open("users.txt")]

	def start(self):
		# ignore the sanity check that quanlity > num account
		for i in range(0, int(self.quantity)):
			parts = self.accountList[i].split("|")
			username = parts[0]
			password = parts[1]
			if self.isFollow:
				self.doFollow(username, password)

	def doFollow(self, username, password):
		




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
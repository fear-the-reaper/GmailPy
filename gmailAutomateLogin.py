from selenium import webdriver
from selenium.webdriver.common.by import By
from getpass import getpass
import time #so that we can use the sleep function
import random
	
class GoogleLogin():
	def __init__(self, email, pwd):
		self.driver = None
		self.email = email
		self.pwd = pwd

	def googleHandler(self, usr, pwd):
		usrNameBox = self.driver.find_element_by_id("identifierId")
		usrNameBox.send_keys(usr)
		NxtBtn = self.driver.find_element_by_id("identifierNext")
		NxtBtn.click()
		time.sleep(2) #Now Before Passing and locating the password we must wait as a new page is loaded therefore a new tags, id and classes come !!!
		pwdBox = self.driver.find_element_by_css_selector("input.whsOnd.zHQkBf")
		pwdBox.send_keys(pwd)
		log = self.driver.find_element_by_id("passwordNext")
		log.click()

	def stackoverflowHandler(self):
		print("Stackoverflow Handler was called")
		url = "https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent"
		self.driver.get(url)
		google = self.driver.find_element(By.CSS_SELECTOR, "button.grid--cell.s-btn.s-btn__icon.s-btn__google.bar-md.ba.bc-black-3")
		google.click()
		return True

	def soundcloudHandler(self):
		print("Soundcloud Handler was called")
		url = "https://soundcloud.com/"
		self.driver.get(url)
		time.sleep(2)
		signUp = self.driver.find_element(By.CSS_SELECTOR, "div.frontHero__cta")
		signUpBtn = signUp.find_element(By.CSS_SELECTOR, "button.g-opacity-transition.frontHero__ctaButton.sc-button.sc-button-cta.sc-button.sc-button-medium.signupButton")
		signUpBtn.click()
		time.sleep(2)
		frame = self.driver.find_element(By.CSS_SELECTOR, "iframe.webAuthContainer__iframe")
		time.sleep(2)
		self.driver.switch_to.frame(frame)
		container = self.driver.find_element(By.CSS_SELECTOR, "body > div#app > div.vertically-centered > div.sign-in-up-form > div.connect-form-pane > div")
		providerBtn = container.find_element(By.CSS_SELECTOR, "div.provider-buttons")
		google = providerBtn.find_element(By.CSS_SELECTOR, "button.provider-button.sc-button.sc-button-large.google-plus-signin.sc-button-google")
		google.click()
		time.sleep(2)
		print(self.driver.window_handles)
		googleSignWindow = self.driver.window_handles[2]
		self.driver.switch_to.window(googleSignWindow)
		return True


	def deezerHandler(self):
		print("deezer Handler was called")	
		url = "https://www.deezer.com/en/register"
		self.driver.get(url)
		cookieBtn = self.driver.find_element(By.CSS_SELECTOR, "a.cookie-btn")
		cookieBtn.click()
		time.sleep(2)
		googleBtn = self.driver.find_element(By.ID, "home_account_gp")
		googleBtn.click()
		time.sleep(2)
		googleSignWindow = self.driver.window_handles[2]
		self.driver.switch_to.window(googleSignWindow)
		return True


	def randomKey(self, sites):
		random.shuffle(sites)
		randNum = random.randint(0, len(sites) - 1)
		return sites[randNum]

	def redirect(self):
		sites = {
			"stackoverflow": self.stackoverflowHandler,
			"soundcloud": self.soundcloudHandler,
			"deezer": self.deezerHandler
		}
		siteList = list(sites.keys())
		key = self.randomKey(siteList)
		self.driver = webdriver.Chrome("chromedriver.exe")
		func = sites.get(key)
		redirected = func()
		if redirected:
			self.googleHandler(self.email, self.pwd)
			if key == "soundcloud" or key == "deezer":
				if key == "deezer":
					time.sleep(2)
					self.driver.close()
				self.driver.switch_to.window(self.driver.window_handles[0])
				self.driver.switch_to.default_content()
			url = "https://mail.google.com"
			time.sleep(5)
			self.driver.get(url)


def main():
	usr = input("Enter Your Username or Email : ")
	pwd = getpass("Enter Password : ") #the getpass("input prompt") will ensure that your password wont be revealed 
	google = GoogleLogin(usr, pwd)
	google.redirect()
	input("Program has ended!!!")

main()
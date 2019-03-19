from selenium import webdriver
from getpass import getpass
import time #so that we can use the sleep function
usr = input("Enter Your Username or Email : ")
pwd = getpass("Enter Password : ") #the getpass("input prompt") will ensure that your password wont be revealed 

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLsogin")

usrNameBox = driver.find_element_by_id("identifierId")
usrNameBox.send_keys(usr)
NxtBtn = driver.find_element_by_id("identifierNext")
NxtBtn.click()

time.sleep(2) #Now Before Passing and locating the password we must wait as a new page is loaded therefore a new tags, id and classes come !!!
 # in seconds

pwdBox = driver.find_element_by_name('password')
pwdBox.send_keys(pwd)
log = driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span')
log.click()
time.sleep(1)
input("")

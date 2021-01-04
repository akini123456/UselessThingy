# Import Statements Needed For Program
import time
from selenium import webdriver

# Status Variables
forever = True

# Username and Password
username = ""
password = ""

# Instagram URL
url = "https://teams.microsoft.com"

# Opens Instagram
driver = webdriver.Chrome('C:\chromedriver.exe')
driver.get(url)
time.sleep(1)

driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]").send_keys(username)
driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/input").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/input").send_keys(password)
driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div/form/div/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input").click()
time.sleep(10)
divTry = "/html/body/div[2]/div[2]/div[2]/div[1]/teams-grid/div/div[2]/div[1]/div[1]/div/div[1]/div[3]/div[5]/div/ng-include/div/div"
driver.find_element_by_xpath(divTry).click()
time.sleep(3)



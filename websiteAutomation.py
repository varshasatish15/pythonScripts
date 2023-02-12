from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome()
def firstPage():
 driver.get("https://www.thesparksfoundationsingapore.org/")
 knowMore=driver.find_element(By.XPATH,"/html/body/div[2]/
div/div[2]/a").click()
 # contactUs=driver.find_element(By.XPATH,"/html/body/
div[1]/div/div[2]/nav/div[2]/nav/ul/li[6]/a").click()
 time.sleep(5)
 driver.get(driver.current_url)
 time.sleep(3)
 guiding_principles=driver.find_element(By.XPATH,"/html/
body/div[2]/div/div[2]/div/ul/li[2]/a").click()
 time.sleep(3)
 advisory=driver.find_element(By.XPATH,"/html/body/div[2]/
div/div[2]/div/ul/li[3]/a").click()
 time.sleep(3)
 executive=driver.find_element(By.XPATH,"/html/body/div[2]/
div/div[2]/div/ul/li[4]/a").click()
 time.sleep(3)
 parterns=driver.find_element(By.XPATH,"/html/body/div[2]/
div/div[2]/div/ul/li[5]/a").click()
 time.sleep(3)
 news=driver.find_element(By.XPATH,"/html/body/div[2]/div/
div[2]/div/ul/li[7]/a").click()
 time.sleep(3)
 # Experts=driver.find_element(By.XPATH,"/html/body/div[2]/
div/div[2]/div/ul/li[6]/a").click()
firstPage()
def secondPage():
 driver.get("https://www.thesparksfoundationsingapore.org/")
 time.sleep(3)
 programs=driver.find_element(By.XPATH,"/html/body/div[4]/
div/div[1]/a").click()
secondPage()
def thirdPage():
 driver.get("https://www.thesparksfoundationsingapore.org/")
 time.sleep(3)
 explore=driver.find_element(By.XPATH,"/html/body/div[5]/
div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div[1]/p/
a").click()
 time.sleep(10)
thirdPage()

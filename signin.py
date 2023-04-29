from selenium import webdriver
import time

#specify where your chrome driver present in your pc
PATH=r"chromedriver.exe"

#get instance of web driver
driver = webdriver.Chrome('./chromedriver')


#provide website url here
driver.get("http://demo.guru99.com/test/newtours/")

#find input text fields
user_name = driver.find_element("name","userName")
password = driver.find_element("name","password")

#find submit button
submit = driver.find_element("name","submit")

#fill input text fields
user_name.send_keys("mercury")
password.send_keys("mercury")

#submit form
submit.click()
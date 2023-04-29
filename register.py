from selenium import webdriver
import time

#specify where your chrome driver present in your pc
PATH=r"chromedriver.exe"

#get instance of web driver
driver = webdriver.Chrome('./chromedriver')


#provide website url here
driver.get("https://demo.guru99.com/test/newtours/register.php")


# maximize page
driver.maximize_window()
# print title
print(driver.title)


#find input text fields
firstName = driver.find_element("name","firstName")
lastName = driver.find_element("name","lastName")
phone = driver.find_element("name","phone")
email = driver.find_element("name","userName")

address = driver.find_element("name","address1")
city = driver.find_element("name","city")
state = driver.find_element("name","state")
postalCode = driver.find_element("name","postalCode")
country = driver.find_element("name","country")

userName = driver.find_element("name","email")
password = driver.find_element("name","password")
confirmPassword = driver.find_element("name","confirmPassword")


#find submit button
submit = driver.find_element("name","submit")

#fill input text fields
firstName.send_keys("mercury")	
lastName.send_keys("mercury")	
phone.send_keys("mercury")	
email.send_keys("mercury")

time.sleep(4)

address.send_keys("mercury")	
city.send_keys("mercury")	
state.send_keys("mercury")	
postalCode.send_keys("mercury")
#Country:

time.sleep(4)

userName.send_keys("mercury")
password.send_keys("mercury")
confirmPassword.send_keys("mercury")

time.sleep(4)

#submit form
submit.click()


# Get the network timings from the performance logs
performance = driver.execute_script("return window.performance.timing")

# Calculate the relevant timings
protocol = driver.current_url.split(":")[0] # Get the protocol (e.g. https)
response_time = performance['responseEnd'] - performance['requestStart'] # Calculate the response time
throughput = len(driver.page_source) / (response_time / 1000) # Calculate the throughput


#Use Navigation Timing API to calculate the timings
navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

backendPerformance_calc = responseStart - navigationStart
frontendPerformance_calc = domComplete - responseStart

pid = driver.service.process.pid
memory_usage = psutil.Process(pid).memory_info().rss



# Output the results
print(f"Protocol: {protocol}")
print(f"Response time: {response_time}ms")
print(f"Throughput: {throughput} bytes/s")
print(f"Memory usage: {memory_usage} bytes")

print("Back End performance: %s" % backendPerformance_calc)
print("Front End performance: %s" % frontendPerformance_calc)



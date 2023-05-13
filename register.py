from selenium import webdriver
import time
import psutil


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


# Get the network timings from the performance logs
performance = driver.execute_script("return window.performance.timing")

# Get the start time
start_time = time.monotonic()


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

#time.sleep(2)

address.send_keys("mercury")	
city.send_keys("mercury")	
state.send_keys("mercury")	
postalCode.send_keys("mercury")
#Country:

#time.sleep(2)

userName.send_keys("mercury")
password.send_keys("mercury")
confirmPassword.send_keys("mercury")

#time.sleep(2)

#submit form
submit.click()


# Get the network timings from the performance logs
performance = driver.execute_script("return window.performance.timing")

# Get the start time
start_time = time.monotonic()

# Calculate the relevant timings
protocol = driver.current_url.split(":")[0] # Get the protocol (e.g. https)
response_time = performance['responseEnd'] - performance['requestStart'] # Calculate the response time
throughput = len(driver.page_source) / (response_time / 1000) # Calculate the throughput


#Use Navigation Timing API to calculate the timings
navigation_start = performance['navigationStart']
response_start = performance['responseStart']
dom_loaded = performance['domContentLoadedEventEnd']
load_time = performance['loadEventEnd'] - navigation_start
frontend_duration = dom_loaded - navigation_start
backend_duration = response_start - navigation_start

pid = driver.service.process.pid
memory_usage = psutil.Process(pid).memory_info().rss


# Calculate the relevant timings
request_sent_time = performance['requestStart'] - performance['navigationStart'] # Calculate the request sent time
waiting_time = performance['responseStart'] - performance['requestStart'] # Calculate the waiting time (TTFB)
content_download_time = performance['responseEnd'] - performance['responseStart'] # Calculate the content download time


# Output the results
print(f"Protocol: {protocol}")
print(f"Response time: {response_time}ms")
print(f"Throughput: {throughput} bytes/s")
print(f"Memory usage: {memory_usage} bytes")

print(f"Request sent time: {request_sent_time}ms")
print(f"Waiting time (TTFB): {waiting_time}ms")
print(f"Content download time: {content_download_time}ms")

print(f"Frontend duration: {frontend_duration}ms")
print(f"Backend duration: {backend_duration}ms")
print(f"Load time: {load_time}ms")



# Get the performance data
perf_data = driver.execute_script("return window.performance.getEntries();")

# Save the performance data to a file
with open("traffic_result .txt", "w") as file:
    for data in perf_data:
        file.write(str(data) + "\n")



# Close the WebDriver
driver.quit()

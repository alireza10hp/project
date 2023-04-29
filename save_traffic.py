from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

# Navigate to the target webpage
driver.get("https://demo.guru99.com/test/newtours/register.php")

# Get the performance data
perf_data = driver.execute_script("return window.performance.getEntries();")

# Save the performance data to a file
with open("traffic_result .txt", "w") as file:
    for data in perf_data:
        file.write(str(data) + "\n")

# Quit the WebDriver instance
driver.quit()
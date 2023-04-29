from browsermobproxy import Server
from selenium import webdriver

# Set up the BrowserMob-Proxy server
server = Server("path/to/browsermob-proxy")
server.start()
proxy = server.create_proxy()

# Set up the Selenium WebDriver to use the proxy server
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--proxy-server={0}".format(proxy.proxy))
driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)

# Start capturing network traffic
proxy.new_har("example")

# Navigate to the target webpage
driver.get("https://demo.guru99.com/test/newtours/register.php")

# Do something with the webpage

# Stop capturing network traffic
har = proxy.har

# Save the network traffic to a file
with open("example.har", "w") as file:
    file.write(json.dumps(har, indent=4))

# Quit the WebDriver instance
driver.quit()

# Stop the BrowserMob-Proxy server
server.stop()

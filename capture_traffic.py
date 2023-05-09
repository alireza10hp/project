from browsermobproxy import Server
from selenium import webdriver
import pyshark

# Start the browsermob-proxy server
server = Server('C:/browsermob-proxy-2.1.4/bin/browsermob-proxy.bat')
server.start()
proxy = server.create_proxy()

# Set up the Selenium WebDriver to use the proxy
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the website you want to capture traffic from
driver.get('https://www.example.com')

# Retrieve the captured traffic data
har = proxy.har

# Stop the browsermob-proxy server and close the Selenium WebDriver
proxy.close()
server.stop()
driver.quit()

# Save the captured traffic data in PCAP format using pyshark
capture = pyshark.FileCapture('captured_traffic.pcap', display_filter='http')
for entry in har['log']['entries']:
    capture.write(entry['response']['content']['text'])
capture.close()

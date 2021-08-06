from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

URL = "https://demo--nyfulcrum-auctioneer.netlify.app/auctions/"
chrome_driver_path = "/Users/coachrye/SeleniumWebDriverProjects/chromedriver"


options = Options()
options.add_argument("--headless")
options.add_argument("window-size=2560,1440")
driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path) #, service_args=["--log-path=./Logs/DubiousDan.log"])

driver.get(URL)
print ("Headless Chrome Initialized")
# print(driver.get_window_size())
# driver.set_window_size(2560, 1440)
size = driver.get_window_size()
print("Window size: width = {}px, height = {}px".format(size["width"], size["height"]))


# first_name = driver.find_element_by_name("fName")
# first_name.send_keys("Yeba")
driver.implicitly_wait(30)
driver.save_screenshot("images/test.png")

driver.quit()
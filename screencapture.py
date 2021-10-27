from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


URL = "https://demo--nyfulcrum-auctioneer.netlify.app/auctions/"
chrome_driver_path = "/Users/coachrye/SeleniumWebDriverProjects/chromedriver"


options = Options()
# options.add_argument("--headless")
# options.add_argument("window-size=2560,1440")
# options.add_argument("window-size=2560,1463")
driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path) #, service_args=["--log-path=./Logs/DubiousDan.log"])

driver.get(URL)
# print(driver.get_window_size())
driver.set_window_size(2560, 1463)
size = driver.get_window_size()
print("Window size: width = {}px, height = {}px".format(size["width"], size["height"]))


# first_name = driver.find_element_by_name("fName")
# first_name.send_keys("Yeba")
driver.implicitly_wait(60)
driver.save_screenshot("images/test-normal.png")
print("Screenshot Normal")

element_to_hover_over = driver.find_element_by_xpath('//*[@id="LA-state"]')
hover = ActionChains(driver).move_to_element(element_to_hover_over)
hover.perform()

driver.implicitly_wait(60)
driver.save_screenshot("images/test-hover.png")
print("Screenshot Hover")

# driver.quit()
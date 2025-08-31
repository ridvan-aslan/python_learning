from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com")

time.sleep(2)

driver.maximize_window()

# driver.save_screenshot("youtube.png")

time.sleep(2)

driver.get("https://www.google.com")

driver.back()
# driver.forward()

if "YouTube" in driver.title:
    driver.save_screenshot("youtube.png")
    
print(driver.title)

driver.quit()



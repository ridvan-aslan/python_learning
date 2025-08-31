from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://www.youtube.com")

input("Press Enter to continue...")

driver.quit()
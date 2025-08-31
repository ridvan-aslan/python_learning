from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://github.com/")

search_input = driver.find_element(By.CLASS_NAME, "header-search-button")
search_input.click()
# search = driver.find_element(By.NAME, "query-builder-test")
search = driver.find_element(By.XPATH, '//*[@id="query-builder-test"]')

search.send_keys("python")

search.send_keys(Keys.ENTER)

wait = WebDriverWait(driver, 10)

# result = driver.page_source

result = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "search-title")))

for title in result:
    print(title.text)

driver.quit()
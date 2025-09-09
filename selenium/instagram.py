from instagram_user_info import instagram_username, instagram_password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.wait = WebDriverWait(self.browser, 10)

    def login(self):
        self.browser.get("https://www.instagram.com")
        time.sleep(2)
        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[1]/div/label/input').send_keys(self.username)
        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[2]/div/label/input').send_keys(self.password)
        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[3]/button').click()
        time.sleep(5)


    def get_followers(self):
        self.browser.get("https://www.instagram.com/ridvanaslan.dev/")
        
        time.sleep(3) 
        
        followers_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href$="/followers/"]'))
        )
        followers_link.click()

        time.sleep(5)
        
        scrollable_div = WebDriverWait(self.browser, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@role='dialog']//div[contains(@class,'x1rife3k')]")
        ))

        time.sleep(5)

        last_height = self.browser.execute_script("return arguments[0].scrollHeight;", scrollable_div)
        scroll_step = 200 
        current_scroll = 0 

        while current_scroll < last_height:
            self.browser.execute_script("arguments[0].scrollTop = arguments[1];", scrollable_div, current_scroll)
            time.sleep(0.5) 
            current_scroll += scroll_step  
            last_height= self.browser.execute_script("return arguments[0].scrollHeight;", scrollable_div)
        
        followers = scrollable_div.find_elements(By.XPATH, "//span[contains(@class, 'xjp7ctv')]//span[@dir='auto']")

        for i in followers:
            print(i.text)

        self.browser.quit()
        
instagram = Instagram(instagram_username, instagram_password)
instagram.login()
instagram.get_followers()
from instagram_user_info import instagram_username, instagram_password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class Instagram:
    def __init__(self, username, password):
        self.browser_profile = webdriver.ChromeOptions()
        self.browser_profile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome(options=self.browser_profile)
        self.username = username
        self.password = password
        self.wait = WebDriverWait(self.browser, 10)

    def login(self):
        self.browser.get("https://www.instagram.com")
        time.sleep(2)
        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[1]/div/label/input').send_keys(self.username)
        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[2]/div/label/input').send_keys(self.password)
        self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[3]/button').click()
        time.sleep(10)


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

        print(f"Your number of followers: {len(followers)}")

        return followers

    def follow_user(self, username):

        self.browser.get(f"https://www.instagram.com/{username}")
        time.sleep(2)

        try:
            follow_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button//div[text()='Follow']"))
            )
            follow_btn.click()
            
            time.sleep(5)

            print("User is followed")

        except TimeoutException:
            print("User is already followed")
        
    def unfollow_user(self, username):

        self.browser.get(f"https://www.instagram.com/{username}")
        time.sleep(2)

        try:
            unfollow = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button//div[text()='Following']"))
            )
            unfollow.click()

            unfollow_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='Unfollow']"))
            )
            unfollow_btn.click()
            
            time.sleep(5)

            print("User is unfollowed")

        except TimeoutException:
            print("User is not followed")

    def print_followers(self):
        get_followers = self.get_followers()

        try:
            with open("selenium/followers.txt", "w+", encoding="utf-8") as file:
                for follower in get_followers:
                    file.write(follower.text + "\n")

                file.seek(0)
                print(file.read())

        except Exception as e:
            print(e)
        
instagram = Instagram(instagram_username, instagram_password)
instagram.login()
instagram.print_followers()

# users = ["ridvanaslan.dev"]

# for user in users:
#     instagram.follow_user(user)
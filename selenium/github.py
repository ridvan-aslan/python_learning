from github_user_info import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Github:
    def __init__(self, username, password, account):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.account = account
        self.wait = WebDriverWait(self.browser, 10)
        self.fallowers = []

    def sign_in(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element(By.XPATH, '//*[@id="login_field"]').send_keys(self.username)
        self.browser.find_element(By.XPATH, '//*[@id="password"]').send_keys(self.password)

        self.browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div/div[2]/form/div[3]/input').click()
        time.sleep(2)

    def load_fallowers(self):
        result = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#user-profile-frame .Link--secondary")))

        for i in result:
            self.fallowers.append(i.text)


        next_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pagination a:last-child")))
        next_btn.click()

        self.wait.until(EC.staleness_of(next_btn))
    
    def get_fallowers(self):
        self.browser.get(f"https://github.com/{self.account}?tab=followers")
        while True:
            try:
                self.load_fallowers()
                
            except Exception as e:
                print(e)
                break

        print("---------")
        print(len(self.fallowers))
        self.browser.quit()

github = Github(username, password, "ridvan-aslan")
github.sign_in()
github.get_fallowers()





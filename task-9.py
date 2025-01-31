import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "https://www.saucedemo.com/v1/"
driver.get("https://www.saucedemo.com/v1/")
time.sleep(3)
get_title = driver.title
driver.maximize_window()
print(get_title)
get_url = driver.current_url
print("The current url is:"+str(get_url))
try:
    username =driver.find_element(By.ID,"user-name")
    username.click()
    username.send_keys("standard_user")
    password=driver.find_element(By.ID,"password")
    password.click()
    password.send_keys("secret_sauce")
    login=driver.find_element(By.ID,"login-button")
    login.click()
    time.sleep(3)
    def save_webpage_content(url, filename):
    # Initialize Chrome webdriver
        driver = webdriver.Chrome()
        import time
    # Open the webpage
        driver.get(url)

    # Get the entire webpage content
    webpage_content = driver.page_source
    time.sleep(2)

    # Save the content to a text file
    with open("webpage_task_11.txt", "w", encoding="utf-8") as file:
        file.write(webpage_content)


# URL of the Swag Labs webpage
    url = "https://www.saucedemo.com/"

# Name of the text file to save the content
    filename = "webpage_task_11.txt"

# Call the function to save webpage content to the text file
    save_webpage_content(url, filename)

finally:
        driver.quit()

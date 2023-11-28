from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.speedtest.net/")

speedtest = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
speedtest.click()
time.sleep(60)
html = driver.find_element(By.TAG_NAME, value="html")
html.send_keys(Keys.END)
time.sleep(3)
close_button = driver.find_element(By.CLASS_NAME, value="pure-button-primary")
close_button.click()
html.send_keys(Keys.UP)
time.sleep(3)
download = driver.find_element(By.CLASS_NAME, value="download-speed")
down = download.text

upload = driver.find_element(By.CLASS_NAME, value="upload-speed")
up = upload.text

print(f"Your download speed is {down} and your upload speed is {up}.")

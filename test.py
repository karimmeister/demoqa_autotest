from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://demoqa.com/")
assert "ToolsQA" in driver.title
wait = WebDriverWait(driver, 10)

# Locating and clicking Card with name Elements
elements_card = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[2]')))
elements_card.click()

# Locating and clicking tab with name Radio Button
radio_button_nav = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="item-2"]/span')))
radio_button_nav.click()

# Asserting that we redirected to page "Radio Button"
page_title = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/div')))
assert "Radio Button" in driver.page_source

# Locating and clikcing imprassibe button
radio_ipmressive = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/label')))
radio_ipmressive.click()

# Locating and clikcing yes button
radio_yes = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label')))
radio_yes.click()

driver.close()
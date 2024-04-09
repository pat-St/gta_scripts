#!/bin/env python
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

import os
import time

# Install driver
os.makedirs("chromedriver",exist_ok=True)
chromedriver_autoinstaller.install(path=os.path.abspath("chromedriver"))

# Start Browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--mute-audio")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.twitch.tv/nomoneymaker")

driver.implicitly_wait(5)
elements = driver.find_elements(By.XPATH, "//button[@aria-label='Settings'][@aria-haspopup='menu'][@data-a-target='player-settings-button']")
if len(elements) > 0:
    ActionChains(driver).move_to_element(elements[0]).click(elements[0]).perform()

driver.implicitly_wait(3)
elements = driver.find_element(By.XPATH, "//button[@data-a-target='player-settings-menu-item-quality']")
if len(elements) > 0:
 ActionChains(driver).move_to_element(elements[0]).click(elements[0]).perform()

driver.implicitly_wait(3)
elements = driver.find_elements(By.XPATH, "//input[@name='player-settings-submenu-quality-option'][@data-a-target='tw-radio']")
if len(elements) > 0:
    ActionChains(driver).move_to_element(elements[-1]).click(elements[-1]).perform()

# Quit Browser
time.sleep(50)
driver.quit()


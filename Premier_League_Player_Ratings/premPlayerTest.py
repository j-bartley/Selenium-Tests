from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set Browser
driver = webdriver.Firefox()

# Go to Pitchfork
driver.get("https://espn.com/")

# Check Pitchfork Reached
assert "ESPN" in driver.title

# Close Browser
driver.close()

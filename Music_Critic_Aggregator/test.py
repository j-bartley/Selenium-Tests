from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set Browser
driver = webdriver.Firefox()

# Go to Pitchfork
driver.get("https://pitchfork.com/")

# Check Pitchfork Reached
assert "Pitchfork" in driver.title

# Go To Search
searchBtn = driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div[6]/header/div[2]/div[1]/div[3]/a')
searchBtn.click()

# Input Search
searchElem = driver.find_element(By.XPATH, '//*[@id="empty-search-header"]/div/div/div/div/div/form/input')
driver.implicitly_wait(2)
searchElem.send_keys("To Pimp A Butterfly")
driver.implicitly_wait(2)
searchElem.send_keys(Keys.RETURN)

# Find Reviews
reviewElem = driver.find_element(By.ID, "result-albumreviews")
reviewCountHolder = reviewElem.find_element(By.CLASS_NAME, "results-count")
print(reviewCountHolder.text)
reviewCount = len(reviewCountHolder.text)
reviewCountString = reviewCountHolder.text
if reviewCount < 5 and reviewCount > 3:
    print("More than 10")
elif reviewCount < 4 and reviewCount > 2:
    print("Less than 10")
    reviewCountString = reviewCountString.replace("(", "")
    reviewCountString = reviewCountString.replace(")", "")
    print(reviewCountString)
else:
    print("Undefined Reviews")
#try:
    
#except:
#    print("No Reviews Available")

# Close Browser
driver.close()
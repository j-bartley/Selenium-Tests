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
artistName = input("Enter an Artist Name: ")
albumName = input("Enter an Album Name: ")
reviewName = artistName + ' ' + albumName
searchElem.send_keys(reviewName)
driver.implicitly_wait(2)
searchElem.send_keys(Keys.RETURN)

# Find Reviews
reviewElem = driver.find_element(By.ID, "result-albumreviews")
reviewCountHolder = reviewElem.find_element(By.CLASS_NAME, "results-count")
# v This grabs the unedited review count
# print(reviewCountHolder.text)
reviewCount = len(reviewCountHolder.text)
reviewCountString = reviewCountHolder.text
reviewCountString = reviewCountString.replace("(", "")
reviewCountString = reviewCountString.replace(")", "")
print("There are " + reviewCountString + " review(s) available.")

# Open Single Review or Choose From Multiple
if(reviewCountString == "1"):
    # Load Review
    singleReviewElem = driver.find_element(By.XPATH, '//*[@id="result-albumreviews"]/ul/li/div')
    singleReviewElem.click()
    # In case of overlay popping up:
    # overlayCrud = driver.find_element(By.XPATH, '//*[@id="bx-close-inside-1643994"]/svg')
    # overlayCrud.click()
    #reviewScoreElem = driver.find_element(By.XPATH, '//*[@id="main-content"]/article/div[1]/header/div[1]/div[2]/div/div[2]/div/div[2]/p')
    reviewScoreElem = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/article/div[1]/header/div[1]/div[2]/div/div[2]/div/div/p')
    
    reviewScore = reviewScoreElem.text
    print("The review score for " + albumName + " is " + str(reviewScore))
else:
    print("Choose Which Review:")
    multReviewCount = int(reviewCountString)
    i = 1
    while i <= multReviewCount:
        print(i)
        tempAlbumName = driver.find_element(By.XPATH, '//*[@id="result-albumreviews"]/ul/li[' + str(i) + ']/div/a/div[2]/h2/em')
        print(tempAlbumName)
        i = i + 1

# Close Browser
driver.close()

# Notes:
# - [FIXED] Album Scores on Pitchfork have different xpath if over 9 score or under 9 score (ex. The Slow Rush by Tame Impala)
# - Album Results have different xpath if notch included
#   - Recommend: Add if/then that checks for special album
#   - Only be needed for duplicate album reviews
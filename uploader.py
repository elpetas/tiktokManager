from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

# Replace with the path to your web driver executable
driver_path = 'C:\cosas personales\chromedriver.exe'

# Replace with the path to your video file
video_path = 'videos\video1.mp4'

# Open a new Chrome browser window
browser = webdriver.Chrome(executable_path=driver_path)
browser.get('https://www.tiktok.com/login')

# Wait for the user to manually login for 300 seconds
try:
   time.sleep(500)
except:
    print("Timed out waiting for login")
else:
    # Navigate to the TikTok upload page
    browser.get('https://www.tiktok.com/upload')

    # Fill in the video file field
    video_field = browser.find_element(By.XPATH, '//input[@type="file"]')
    video_field.send_keys(video_path)

    # Fill in any captions or hashtags
    caption_field = browser.find_element(By.XPATH, '//textarea[@name="description"]')
    caption_field.send_keys('My awesome video! #cool #fun')

    # Click the upload button
    upload_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    upload_button.click()

    # Wait for the upload to complete
    WebDriverWait(browser, 60).until(
        EC.url_contains('https://www.tiktok.com/@')
    )

    # Close the browser window
    browser.quit()

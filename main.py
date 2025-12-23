from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Start browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Open a test website
driver.get("https://www.geeksforgeeks.org/python/python-automation/")

# Wait until heading is visible
wait = WebDriverWait(driver, 10)
heading = wait.until(
    EC.visibility_of_element_located((By.TAG_NAME, "h1"))
)

print("Page heading:", heading.text)


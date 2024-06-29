import time
import pandas as pd
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options to disable image loading
chrome_options = Options()
chrome_prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", chrome_prefs)
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")

# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open the URL
url = "https://bsky.app/search?q=doi.org"
driver.get(url)

# Wait for the page to load
time.sleep(5)

# Wait for the user to click the "Latest" button
input("Please click on the 'Latest' tab and press Enter to continue :-)")

# Scroll down until the end of the page or until 'E' is pressed
last_height = driver.execute_script("return document.body.scrollHeight")

print("Scrolling... Press 'E' to end scrolling and save files.")

while True:
    # Scroll down to the bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)  # Wait for new content to load

    # Check if 'E' key is pressed
    if keyboard.is_pressed('e'):
        print("Ending scroll and saving files...")
        break

    # Calculate new scroll height and compare with the last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        print("Reached the end of the page.")
        break
    last_height = new_height

# Collect all the links from the page
links = driver.find_elements(By.TAG_NAME, "a")
link_urls = [link.get_attribute("href") for link in links if link.get_attribute("href") is not None]

# Get the full HTML content of the page
page_content = driver.page_source

# Close the WebDriver
driver.quit()

# Save the links to a CSV file
df = pd.DataFrame(link_urls, columns=["Links"])
df.to_csv("links.csv", index=False)

# Save the full HTML content to an HTML file
with open("page_content.html", "w", encoding="utf-8") as file:
    file.write(page_content)

print("Links have been saved to links.csv")
print("HTML content has been saved to page_content.html")

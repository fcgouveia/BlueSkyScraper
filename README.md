# BlueSkyScraper
**A simple BlueSky Scraper in Python3 using Selenium Libray**

In this example, I was collecting posts that cite DOIs. You can change the search URL to what you want. A file with all the links on the page and the full page will be saved at the end. BlueSky enables you to scroll back 6 months of posts and also you may need to limit your scrape based on the amount of memory you have. A chromium browser with the correct chromedriver is required. The script will wait for you to log into your account and change the view tab from **top** to **latest**. You can type "E" anytime to end the scrape. This code was generated with the help of ChatGPT 3.5

**Dependencies:**
Ensure you have the necessary libraries installed:

```
pip install selenium pandas webdriver-manager keyboard
```

**Running the Script:**

1. Run the script.
2. Wait for the browser to open and load the page.
3. Log to your BlueSky Account - optional
4. Manually click on the "Latest" tab.
5. Press Enter in the console where the script is running to continue execution.
6. The script will scroll down and automatically save the files either when the end of the page is reached or when you press 'E'.

```
python3 blueskyscrape.py
```

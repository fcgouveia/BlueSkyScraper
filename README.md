# BlueSkyScraper
A simple BlueSky Scraper in Python3 using Selenium Libray

In this example, I was collecting posts that cite DOIs. You can change the search URL to what you want. At the end, a file with all the links on the page and the full page will be saved. BlueSky enables you to scroll back 6 months of posts and also you may need to limit your scrape based on the amount of memory you have. A chromium browser with the correct chromedriver is required. The script will wait for you to log into your account and change the view tab from top to latest. You can type "E" anytime to end the scrape.

from  playwright.sync_api import sync_playwright # used to synchronously control the browser

with sync_playwright() as p:
    # Launch the browser (Chromium, Firefox, or WebKit)
    browser = p.chromium.launch(headless=True)  # Set headless=True for headless mode false to see the browser window
    page.goto("https://google.com")
    page.screenshot(path="screenshot.png")  # Take a screenshot of the page
    browser.close()  # Close the browser after the operations are done
    
   
    
    
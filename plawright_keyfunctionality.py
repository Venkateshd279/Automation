from playwright.sync_api import sync_playwright, Error as PlaywrightError

ACCUWEATHER_URL = "https://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671?type=locality&city=chennai"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

# navigate to a webpage and take a screenshot
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://google.com")
    page.wait_for_load_state("networkidle")
    page.screenshot(path="screenshot.png")
    print("Google screenshot saved.")
    browser.close()

# navigate to weather page and take a screenshot
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--disable-http2"])
    page = browser.new_page(user_agent=USER_AGENT)
    try:
        page.goto(ACCUWEATHER_URL, timeout=60000)
        page.wait_for_load_state("networkidle", timeout=60000)
        page.screenshot(path="weather_screenshot.png")
        print("Weather screenshot saved.")
    except PlaywrightError as e:
        print(f"Skipping weather screenshot: {e}")
    finally:
        browser.close()

# clicking on a specific element (temperature) and taking a screenshot
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--disable-http2"])
    page = browser.new_page(user_agent=USER_AGENT)
    try:
        page.goto(ACCUWEATHER_URL, timeout=60000)
        page.wait_for_load_state("networkidle", timeout=60000)
        page.wait_for_selector("div.temp", timeout=15000)
        temperature_element = page.query_selector("div.temp")
        if temperature_element:
            temperature_element.screenshot(path="temperature_screenshot.png")
            print("Temperature element screenshot saved.")
        else:
            print("Temperature element not found.")
    except PlaywrightError as e:
        print(f"Skipping temperature screenshot: {e}")
    finally:
        browser.close()

# typing text into a search box and taking a screenshot of the results
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.wait_for_load_state("networkidle")
    search_box = page.query_selector("input[name='q']")
    if search_box:
        search_box.type("Playwright Python")
        page.keyboard.press("Enter")
        page.wait_for_selector("h3")
        page.wait_for_load_state("networkidle")
        page.screenshot(path="search_results_screenshot.png")
        print("Search results screenshot saved.")
    browser.close()

# extracting text from a specific element (temperature) and printing it
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--disable-http2"])
    page = browser.new_page(user_agent=USER_AGENT)
    try:
        page.goto(ACCUWEATHER_URL, timeout=60000)
        page.wait_for_load_state("networkidle", timeout=60000)
        page.wait_for_selector("div.temp", timeout=15000)
        temperature_element = page.query_selector("div.temp")
        if temperature_element:
            temperature_text = temperature_element.inner_text()
            print(f"Current temperature in Chennai: {temperature_text}")
        else:
            print("Temperature element not found.")
    except PlaywrightError as e:
        print(f"Skipping temperature extraction: {e}")
    finally:
        browser.close()

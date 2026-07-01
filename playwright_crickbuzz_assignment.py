from playwright.sync_api import sync_playwright

# copy the details of first match and store it in a text file
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.cricbuzz.com/cricket-series/10119/icc-womens-t20-world-cup-2026/matches")
    page.wait_for_load_state("networkidle")
    
    # Wait for the first match element to be visible
    page.wait_for_selector(".cb-col.cb-col-100.cb-ltst-wgt-hdr", timeout=15000)
    
    # Get the text of the first match
    first_match_element = page.query_selector(".cb-col.cb-col-100.cb-ltst-wgt-hdr")
    if first_match_element:
        first_match_text = first_match_element.inner_text()
        
        # Store the details in a text file
        with open("first_match_details.txt", "w") as file:
            file.write(first_match_text)
        print("First match details stored in 'first_match_details.txt'.")
    else:
        print("First match element not found.")
    
    browser.close()

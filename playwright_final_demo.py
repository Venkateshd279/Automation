import asyncio
from datetime import datetime
from playwright.async_api import async_playwright

async def main():
    print("Starting the Playwright script...")
    print(f"Current date and time: {datetime.now()}")

    async with async_playwright() as p:
        print("Launching the browser...")
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        print("Navigating to the website...")
        await page.goto("https://www.nseindia.com/")

        print("Waiting for the page to load...")
        await page.wait_for_load_state("networkidle")

        print("Taking a screenshot of the page...")
        await page.screenshot(path="nse_screenshot.png")
        print("Screenshot saved as nse_screenshot.png")

        print("Waiting for Nifty 50 elements to appear...")
        await page.wait_for_selector("p.symbol", timeout=30000)

        print("Extracting the Nifty 50 index value...")
        nifty_50_value = await page.evaluate(
            '''() => {
                const symbols = Array.from(document.querySelectorAll('p.symbol'));
                for (const symbol of symbols) {
                    if (symbol.textContent.trim().toUpperCase() === 'NIFTY 50') {
                        const valueElement = symbol.nextElementSibling;
                        if (valueElement && valueElement.classList.contains('value')) {
                            return valueElement.textContent.trim();
                        }
                    }
                }
                return null;
            }'''
        )

        if nifty_50_value:
            with open("nifty_50_value.txt", "w") as f:
                f.write(nifty_50_value)
            print(f"Nifty 50 index value saved in nifty_50_value.txt: {nifty_50_value}")
        else:
            print("Nifty 50 index value element not found.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
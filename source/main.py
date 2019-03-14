import scrape
import word_cloud


driver = scrape.initialize_browser(headless=True)
scrape.scrape_data(driver, "YourQuoraID")

word_cloud.generate_word_cloud()

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def initialize_browser(headless=False):
    """
    Creates an instance of Firefox web browser. Make sure `geckodriver` is present in the `browser` directory..

    :param headless: turn headless mode on/off
    :return: browser instance
    """

    options = Options()
    options.headless = headless
    driver = webdriver.Firefox(options=options, executable_path="..\\browser\geckodriver.exe")

    return driver


def scrape_data(driver, profile_name):
    """
    Scrapes the answers and writes it onto physical storage.

    :param driver: selenium browser's driver
    :param profile_name: string
    :return: None
    """

    driver.get("https://www.quora.com/profile/{}".format(profile_name))

    answers_count = int(driver.find_element_by_xpath("//span[contains(@class, 'list_count')]").text)
    answers_found = 0

    while answers_found < answers_count:
        expand_link = driver.find_element_by_xpath("//a[contains(@class, 'ui_qtext_more_link')]")
        expand_link.click()

        expanded_answer = driver.find_elements_by_xpath("//div[contains(@class, 'ui_qtext_expanded')]")
        print(expanded_answer)

        answers_found += 1

    driver.close()


dr = initialize_browser()
scrape_data(dr, "Amal-Rajan-5")

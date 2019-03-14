import time

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
    driver = webdriver.Firefox(
        options=options, executable_path="..\\browser\geckodriver.exe")

    return driver


def scrape_data(driver, profile_name):
    """
    Scrapes the answers and writes it onto physical storage.

    :param driver: selenium browser's driver
    :param profile_name: string
    :return: None
    """

    driver.get("https://www.quora.com/profile/{}".format(profile_name))

    answers_count = int(driver.find_element_by_xpath(
        "//span[contains(@class, 'list_count')]").text)
    answer_links = []

    while len(answer_links) < answers_count:
        answer_links = driver.find_elements_by_class_name("question_link")
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    view_more_links = driver.find_elements_by_xpath(
        "//a[contains(@class, 'ui_qtext_more_link')]")

    for view_more_link in view_more_links:
        view_more_link.click()

    expanded_answers = driver.find_elements_by_xpath(
        "//div[contains(@class, 'ui_qtext_expanded')]")

    out_file = open("answer_blob.txt", "w", encoding="utf-8")

    for answer in expanded_answers:
        out_file.write(str(answer.text))
        out_file.write('\n')

    out_file.close()

    driver.close()

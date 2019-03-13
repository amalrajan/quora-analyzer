import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = False
driver = webdriver.Firefox(options=options, executable_path="..\\browser\\geckodriver.exe")
driver.get("https://www.quora.com/profile/Amal-Rajan-5")

answer_count = int(driver.find_element_by_xpath("//span[contains(@class, 'list_count')]").text)
answer_links = []

print(answer_count)

while len(answer_links) < answer_count:
    answer_links = driver.find_elements_by_class_name("question_link")
    print(len(answer_links))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

view_more_links = driver.find_elements_by_xpath("//a[contains(@class, 'ui_qtext_more_link')]")

for view_more_link in view_more_links:
    view_more_link.click()

expanded_answers = driver.find_elements_by_xpath("//div[contains(@class, 'ui_qtext_expanded')]")

for answer in expanded_answers:
    print(answer.text, end='\n')

driver.close()

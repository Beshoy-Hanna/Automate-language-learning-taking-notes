import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

def main():
    translate_from = input('Translate From: ')
    translate_into = input('Translate Into: ')

    options = Options()
    options.add_experimental_option('detach', True)

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    driver.get(f'https://www.deepl.com/en/translator#{translate_from}/{translate_into}/')
    driver.maximize_window()
    time.sleep(5)

    text_area_field = '//*[@id="textareasContainer"]/div[1]/section/div/div[1]/d-textarea'
    translation_area = '//*[@id="textareasContainer"]/div[3]/section/div[1]/d-textarea/div/p'

    text_area = driver.find_element('xpath', text_area_field)

    with open('translations.md', 'w', newline='', encoding='utf-8') as mdfile:
        csvwriter = csv.writer(mdfile)
        mdfile.write("| German | Translation |\n")
        mdfile.write("| ------ | ----------- |\n")

        with open('german_phrases.txt', 'r', encoding="utf-8") as file:
            for line in file:
                text_area.send_keys(Keys.CONTROL + "a")
                text_area.send_keys(Keys.DELETE)

                phrase = line.rstrip()
                text_area.send_keys(phrase)
                time.sleep(10)

                translation_element = driver.find_element('xpath', translation_area)
                translation = translation_element.text

                mdfile.write(f"| {phrase} | {translation} |\n")

    driver.quit()

if __name__ == "__main__":
    main()

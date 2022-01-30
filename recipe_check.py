# noinspection PyUnresolvedReferences
import time

# Seleniumの中のwebdriverをインポート
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://cookpad.com"  # グローバル変数


def search_by_food(driver, food):
    driver.get(f"{URL}")
    driver.implicitly_wait(10)

    driver.find_element(By.ID, "keyword").send_keys(food)  # 検索にfoodの内容を入力すべし
    driver.find_element(By.ID, "submit_button").click()  # 検索ボタンを押すべし

    time.sleep(10)


def get_recipes(driver):
    recipe_previews = driver.find_elements(By.CLASS_NAME, "recipe-preview")
    # print(recipe_previews)

    for recipe_preview in recipe_previews:
        recipe_title = recipe_preview.find_element(By.CLASS_NAME, "recipe-title").text
        recipe_url = recipe_preview.find_element(By.CLASS_NAME, "recipe-title").get_attribute('href')
        print(recipe_title, recipe_url)


def main():
    food = 'トマト'

    # 前の方法
    # driver = webdriver.Chrome()
    # driver.get("")
    # driver.implicitly_wait(10)
    # driver.close()

    # withの方法(ドライバーclose忘れ防止)
    with webdriver.Chrome() as driver:
        search_by_food(driver, food)
        get_recipes(driver)


if __name__ == '__main__':
    main()

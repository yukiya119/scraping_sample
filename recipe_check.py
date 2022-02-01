import time

# noinspection PyUnresolvedReferences
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://cookpad.com"  # グローバル変数


def chromedriver_options():
    # オプション設定
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # ヘッドレスモード
    # options.add_argument("--blink-settings=imagesEnabled=false")  # 画像無効
    # options.add_argument("--enable-javascript")  # JS無効
    return options


def search_by_food(driver, food):
    driver.get(f"{URL}")
    driver.implicitly_wait(10)

    driver.find_element(By.ID, "keyword").send_keys(food)  # 検索にfoodの内容を入力
    driver.find_element(By.ID, "submit_button").click()  # 検索ボタンを押す
    # time.sleep(10)


def get_recipes(driver):
    recipe_previews = driver.find_elements(By.CLASS_NAME, "recipe-preview")
    # print(recipe_previews)

    recipes = []
    for recipe_preview in recipe_previews:
        recipe_title = recipe_preview.find_element(By.CLASS_NAME, "recipe-title").text
        recipe_url = recipe_preview.find_element(By.CLASS_NAME, "recipe-title").get_attribute('href')
        recipes.append({
            "title": recipe_title,
            "url": recipe_url})
    return recipes


def main():
    food = 'トマト'

    # 前の方法
    # driver = webdriver.Chrome()
    # driver.get("")
    # driver.implicitly_wait(10)
    # driver.close()

    # withの方法(close忘れ防止)
    with webdriver.Chrome(options=chromedriver_options()) as driver:
        search_by_food(driver, food)
        recipes = get_recipes(driver)

        for recipe in recipes:
            print(f"レシピ名 {recipe['title']}, URL:{recipe['url']}")


if __name__ == '__main__':
    start = time.time()  # 開始の時間
    main()
    print(time.time() - start)  # 終了の時間 - 開始の時間

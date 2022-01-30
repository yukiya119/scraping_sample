# noinspection PyUnresolvedReferences
import time

# Seleniumの中のwebdriverをインポート
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def main():
    food = 'トマト'
    # ドライバーの立ち上げ
    driver = webdriver.Chrome()
    # Googleにアクセス
    driver.get('https://google.com/')

    driver.find_element(By.NAME, "q").send_keys(food)
    driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)

    time.sleep(1)
    # ドライバーを閉じる
    driver.close()


if __name__ == '__main__':
    main()

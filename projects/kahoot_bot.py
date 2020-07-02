from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = r"C:\Users\annaf\Downloads\Python\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://kahoot.it/v2/")

game_pin = "364117" 
number_of_bots = 10

try:
    input_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "game-input"))
    )
    input_box.click()
    input_box.send_keys(game_pin)

    enter_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "enter-button__EnterButton-sc-1o9b9va-0"))
    )
    enter_box.click()

    nickname =  WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "nickname"))
    )
    enter_game = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "enter-button__EnterButton-sc-1o9b9va-0"))
    )

    for i in range(1, number_of_bots):
    	nickname.send_keys(" bot " + str(i))
    	enter_game.click()
    	break


except Exception as e:
    driver.quit()
    print('Error', e)

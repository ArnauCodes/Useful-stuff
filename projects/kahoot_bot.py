from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Install selenium in the cmd

# You must use your own path for the executable webdriver at: https://chromedriver.chromium.org/downloads

# Happy 4th of July!!


PATH = r"C:\Users\annaf\Downloads\Python\chromedriver.exe" 


driver = webdriver.Chrome(PATH)

game_pin = str()
number_of_bots = int() 


def flood_bots():
	try:
		driver.get("https://kahoot.it/v2/")

		for i in range(1, number_of_bots + 1):

			# In kahoot.com, there is a delay of n seconds (around 3) when you enter more than 7 times in x time.

			if i >= 8:
				sleep(10)

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

			nickname.send_keys(" bot " + str(i))
			nickname.clear() 
			enter_game.click()

			if i == number_of_bots + 1:
				break

			sleep(2)

			driver.back()
			driver.switch_to_alert().accept()

	except Exception as e:
	    driver.quit()
	    print("Error:", e)

flood_bots()

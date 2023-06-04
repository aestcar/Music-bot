import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://myfreemp3.app/')

main_window = driver.current_window_handle

print('Programa hecho por Albert Esteve')
print('Durante la ejecución se te abrirá Google Chrome, no lo toques, se cerrará cuando el programa haya acabado.')

with open('lista_canciones.txt', 'r') as file:
    file_content = file.read()
    songs_list = file_content.splitlines()

for song in songs_list:

	print('Intentando descargar: '+ song)

	try:

		input_field = driver.find_element(By.NAME, "query")

		input_field.click()
		input_field.clear()
		input_field.send_keys(song)
		input_field.send_keys(Keys.ENTER)

		time.sleep(4)  

		element = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/button[2]")

		if element:
				element.click()

		time.sleep(6)  

		element = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[2]/a")
		if element:
				element.click()

		time.sleep(4)

		driver.switch_to.window(driver.window_handles[-1])
		driver.close()

		print('Se ha descargado correctamente: '+ song)

		driver.switch_to.window(main_window)

		time.sleep(2)
	except NoSuchElementException:
		print('Ha habido un problema descargando la canción: ' + song)

print('Todas las canciones han sido descargadas, que tengas un gran dia :)')

driver.quit()
sys.exit()
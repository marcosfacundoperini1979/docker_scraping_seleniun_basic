from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
# Ruta al ejecutable del controlador de Chrome
chrome_driver_path = "/app/chromedriver"

# Configuración del controlador de Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Ejecutar en modo sin cabeza (sin interfaz gráfica)
chrome_options.add_argument("--disable-gpu")  # Necesario en sistemas Linux para prevenir errores
chrome_options.add_argument("--no-sandbox")  # Agrega esta línea para prevenir problemas en algunos entornos


# Crear el controlador de Chrome con la configuración
driver = webdriver.Chrome(options=chrome_options)


try:
    print('mirando google.com',datetime.now())
    # Abrir una página de ejemplo (puedes cambiar la URL)
    driver.get("https://www.google.com")

    # Encontrar el campo de búsqueda por su nombre (puedes usar otros selectores)
    search_box = driver.find_element("name", "q")

    # Escribir en el campo de búsqueda
    search_box.send_keys("Prueba de Selenium en Kali Linux")

    # Enviar la búsqueda
    search_box.send_keys(Keys.RETURN)

    # Esperar unos segundos para que la búsqueda se realice (puedes ajustar este tiempo)
    time.sleep(5)

    # Capturar una captura de pantalla del resultado de la búsqueda
    driver.save_screenshot("/app/screenshot.png")
    print('Tarea realizada con éxito')

finally:
    # Cerrar el navegador al finalizar
    driver.quit()

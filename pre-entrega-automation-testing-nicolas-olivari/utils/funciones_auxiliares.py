"""Funciones auxiliares para los tests de SauceDemo.

Estas funciones sirven para no repetir codigo en los tests. Los tests actuales
hacen el login "a mano" (inline), asi que por ahora estas funciones quedan
disponibles para usarlas cuando haga falta.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL_BASE = "https://www.saucedemo.com/"
USUARIO = "visual_user"
PASSWORD = "secret_sauce"


def login(driver, usuario=USUARIO, password=PASSWORD):
    """Abre SauceDemo, completa el formulario y hace clic en Login."""
    driver.get(URL_BASE)
    driver.find_element(By.ID, "user-name").send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


def obtener_primer_producto(driver):
    """Devuelve (nombre, precio) del primer producto del catalogo."""
    primer_producto = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
    )
    nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
    return nombre, precio

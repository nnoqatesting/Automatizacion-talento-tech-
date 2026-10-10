from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_cart():
    driver = webdriver.Chrome()
    
    try:
        # Asignamos el tiempo de espera explícita
        wait = WebDriverWait(driver, 10)

        driver.get("https://www.saucedemo.com/")  

        # Localizar elementos del login
        usuario = driver.find_element(By.ID, "user-name") 
        contraseña = driver.find_element(By.ID, "password") 
        boton_login = driver.find_element(By.ID, "login-button")

        # Completar credenciales y hacer login
        usuario.send_keys("visual_user")
        contraseña.send_keys("secret_sauce")
        boton_login.click()

        # Encontramos el contenedor de los productos usando la espera
        primer_producto = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))
        
        #  Buscamos el nombre del producto dentro del contenedor usando el selector correcto (By.CLASS_NAME)
        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text

        # Seleccionamos el botón para agregar al carrito y hacemos clic
        boton_agregar = primer_producto.find_element(By.TAG_NAME, "button")
        boton_agregar.click()

        # Validamos que el contador del carrito sume un item
        contador_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))

        # (agregado) verificamos que el contador marque 1 producto
        assert contador_carrito.text == "1"

        # Hacemos clic en el icono del carrito para ir a la vista de compra
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

        # Validamos la etiqueta del item del producto en el carrito
        nombre_producto_carrito = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))).text

        # Assert final para comprobar que es el mismo producto
        assert nombre_producto == nombre_producto_carrito

    finally:
        
        driver.quit()

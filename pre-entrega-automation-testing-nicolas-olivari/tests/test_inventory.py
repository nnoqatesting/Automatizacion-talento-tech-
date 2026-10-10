from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# CATALOGO (agregado): esta prueba no estaba en los archivos originales, la pide la consigna
def test_catalogo():
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

        # Esperamos a que carguen los productos del catalogo
        productos = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

        # Verificamos que el titulo de la pagina sea el correcto
        assert driver.title == "Swag Labs"

        # Comprobamos que haya productos visibles
        assert len(productos) > 0

        # Verificamos elementos importantes: el menu y el filtro
        menu = driver.find_element(By.ID, "react-burger-menu-btn")
        assert menu.is_displayed()

        filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert filtro.is_displayed()

        # Obtenemos y mostramos el nombre y el precio del primer producto
        primer_producto = productos[0]
        nombre_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
        precio_producto = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
        print(f"\nPrimer producto -> Nombre: {nombre_producto} | Precio: {precio_producto}")

        assert nombre_producto != ""
        assert precio_producto.startswith("$")

    finally:
        driver.quit()

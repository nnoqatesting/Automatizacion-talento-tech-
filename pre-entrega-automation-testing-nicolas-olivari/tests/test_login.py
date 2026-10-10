# Importa la herramienta principal de Selenium para controlar el navegador web (en este caso, Chrome).
from selenium import webdriver

# Importa la estrategia 'By', que permite especificar cómo buscar un elemento en el HTML (por ID, CLASS_NAME, XPATH, etc.).
from selenium.webdriver.common.by import By

# (agregado) para esperar a que aparezca el titulo "Products" despues del login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_exitoso():
    driver = webdriver.Chrome() #elijo el navegador que voy a utilizar en este caso     

    try:
        driver.get("https://www.saucedemo.com/")  #asigno la web que voy a utilizar 


        #localizar elementos 
        usuario = driver.find_element(By.ID,"user-name") # aca ingreso el ID y en .sendkeys agrego el usuario en cuestion
        contraseña = driver.find_element(By.ID,"password") #lo mismo que el ID en pw y se le agrega la accion click
        boton_login = driver.find_element(By.ID,"login-button")

        #Previamente podria ser el comando driver.find_element(By.ID,"user-name").send_keys("visual_user")  lo mismo con la contraseña, pero
        # es mejor agregarle una variable por si en algun momento hay una modificacion de usuario o pw  y ejecutar la accion 

        #completar el formulario (variables)
        usuario.send_keys("visual_user")
        contraseña.send_keys("secret_sauce")

        #hacer click en el login
        boton_login.click()

        #validacion de login con un assert

        assert driver.current_url == "https://www.saucedemo.com/inventory.html"  #apunta al url, si es igual la prueba seria valida   #estoy definiendo el login exitoso en este caso

        # (agregado) validamos tambien que aparezca el titulo "Products" en la pagina
        wait = WebDriverWait(driver, 10)
        titulo_products = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        assert titulo_products.text == "Products"

    finally:
        # (agregado) cerramos el navegador siempre, pase o falle la prueba
        driver.quit()

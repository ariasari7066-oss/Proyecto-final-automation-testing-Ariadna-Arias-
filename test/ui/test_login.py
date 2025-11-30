from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_exitoso(driver, logger):
    logger.info("Inicio del test de login exitoso") #LOGGER

    login = LoginPage(driver)
    logger.info("Abriendo la página de login") #LOGGER
    login.abrir()

    logger.info("Realizando login con usuario y contraseña válidos") #LOGGER
    login.login()

    inventory = InventoryPage(driver)
    titulo = inventory.obtener_titulo()
    logger.info(f"Se obtuvo el título de la página: '{titulo}'") #LOGGER

    assert titulo == "Products"
    logger.info("Test finalizado correctamente") #LOGGER

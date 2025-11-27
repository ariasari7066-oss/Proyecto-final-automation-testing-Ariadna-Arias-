from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_login_exitoso(driver):
    login=LoginPage(driver)
    login.abrir()

    login.login()

    inventory = InventoryPage(driver)

    assert inventory.obtener_titulo()=="Products"
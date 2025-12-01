from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventario(driver):
    """Test interfaz de inventario"""
    login = LoginPage(driver)
    login.abrir()
    login.login()

    inventory = InventoryPage(driver)

    assert inventory.obtener_titulo() == "Products"
    assert inventory.hay_productos_visibles() is True
    assert inventory.elementos_interfaz_presentes() is True

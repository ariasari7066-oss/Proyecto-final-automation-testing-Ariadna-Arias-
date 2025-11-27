from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_carrito(driver):
    # Login
    login = LoginPage(driver)
    login.abrir()
    login.login()

    inventory = InventoryPage(driver)

    # 1. Agregar producto
    inventory.agregar_backpack_al_carrito()

    # 2. Verificar incremento del carrito
    assert inventory.obtener_conteo_carrito() == 1

    # 3. Ir al carrito
    inventory.ir_al_carrito()

    cart = CartPage(driver)

    # 4. Verificar que el producto está en el carrito
    assert cart.producto_backpack_esta_presente() is True

    # (Opcional) Verificar cantidad
    assert cart.cantidad_de_items() == 1

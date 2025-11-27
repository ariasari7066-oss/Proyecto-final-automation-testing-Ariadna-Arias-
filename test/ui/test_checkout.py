from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.helpers import NOMBRE, APELLIDO, CODIGO_POSTAL

def test_checkout_completo(driver):
    # Login
    login = LoginPage(driver)
    login.abrir()
    login.login()

    # Inventario: agregar 1 producto
    inventory = InventoryPage(driver)
    inventory.agregar_backpack_al_carrito()
    inventory.ir_al_carrito()

    # Carrito
    cart = CartPage(driver)
    assert cart.obtener_titulo() == "Your Cart"
    cart.ir_a_checkout()

    # Checkout Step 1
    checkout = CheckoutPage(driver)
    assert checkout.obtener_titulo() == "Checkout: Your Information"
    checkout.completar_formulario(NOMBRE, APELLIDO, CODIGO_POSTAL)
    checkout.continuar()

    # Checkout Step 2
    assert checkout.obtener_titulo() == "Checkout: Overview"

    # Finalizar compra
    checkout.finalizar_compra()

    # Confirmación
    assert checkout.obtener_titulo() == "Checkout: Complete!"

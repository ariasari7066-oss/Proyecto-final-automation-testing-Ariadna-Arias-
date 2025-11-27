from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.actions_page import ActionsPage


class CartPage(ActionsPage):

    CART_TITLE = (By.CLASS_NAME, "title")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    BACKPACK_NAME = (By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']")
    CHECKOUT_BTN = (By.ID, "checkout")

    def obtener_titulo(self):
        return self.obtener_texto(self.CART_TITLE)

    def producto_backpack_esta_presente(self):
        """Revisa si el producto agregado aparece en el carrito."""
        try:
            self.encontrar(self.BACKPACK_NAME)
            return True
        except:
            return False

    def cantidad_de_items(self):
        items = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_all_elements_located(self.CART_ITEMS))
        return len(items)
    
    # --- MÉTODOS DEL CHECKOUT--

    def ir_a_checkout(self):
        self.click(self.CHECKOUT_BTN)
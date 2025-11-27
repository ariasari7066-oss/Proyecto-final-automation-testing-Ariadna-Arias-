from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.actions_page import ActionsPage


class InventoryPage(ActionsPage):
    """Page Object para la página de inventario"""

    # LOCALIZADORES
    TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    FILTER_SELECT = (By.CLASS_NAME, "product_sort_container")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")


    # --- LOCALIZADORES DEL CARRITO ---
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    
    def obtener_titulo(self):
        """Devuelve el texto del título de la página."""
        return self.obtener_texto(self.TITLE)
    
    def hay_productos_visibles(self):
        """Verifica que haya al menos un producto visible."""
        productos = self.driver.find_elements(*self.INVENTORY_ITEM)
        return len(productos) > 0
    
    def elementos_interfaz_presentes(self):
        """Valida que existan menú, filtros y carrito."""
        try:
            self.encontrar(self.MENU_BTN)
            self.encontrar(self.FILTER_SELECT)
            self.encontrar(self.CART_LINK)
            return True
        except:
            return False
    

        # --- MÉTODOS DEL CARRITO ---
    def agregar_backpack_al_carrito(self):
        """Hace clic en el botón 'add to cart' del Backpack."""
        self.click(self.ADD_BACKPACK)

    def obtener_conteo_carrito(self):
        """Devuelve el número del carrito o 0 si no hay badge."""
        try:
            return int(self.obtener_texto(self.CART_BADGE))
        except:
            return 0

    def ir_al_carrito(self):
        """Hace clic en el icono del carrito para navegar."""
        self.click(self.CART_LINK)

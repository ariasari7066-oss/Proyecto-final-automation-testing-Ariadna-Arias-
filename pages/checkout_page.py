from selenium.webdriver.common.by import By
from pages.actions_page import ActionsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage(ActionsPage):
    """Page Object para el proceso de checkout"""

    # Paso 1: Información del cliente
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")

    # Paso 2: Confirmación de compra
    FINISH_BTN = (By.ID, "finish")
    TITLE = (By.CLASS_NAME, "title")

    # Validación
    SUCCESS_MSG = (By.CLASS_NAME, "complete-header")

    def completar_formulario(self, nombre, apellido, codigo_postal):
        """Completa los campos del checkout con los datos del usuario."""
        self.escribir(self.FIRST_NAME, nombre)
        self.escribir(self.LAST_NAME, apellido)
        self.escribir(self.POSTAL_CODE, codigo_postal)

    def continuar(self):
        """Hace clic en Continue."""
        self.click(self.CONTINUE_BTN)
        WebDriverWait(self.driver, 10).until(
        EC.text_to_be_present_in_element(self.TITLE, "Overview")
    )

    def finalizar_compra(self):
        """Hace clic en Finish."""
        self.click(self.FINISH_BTN)

    def obtener_titulo(self):
        """Devuelve el texto del título de la página."""
        return self.obtener_texto(self.TITLE)

    def obtener_mensaje_exito(self):
        """Devuelve el mensaje final de compra exitosa."""
        return self.obtener_texto(self.SUCCESS_MSG)
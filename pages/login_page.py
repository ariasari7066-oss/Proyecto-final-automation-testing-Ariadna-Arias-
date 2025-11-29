from pages.actions_page import ActionsPage
from selenium.webdriver.common.by import By
from utils.helpers import USERNAME,PASSWORD,URL

class LoginPage(ActionsPage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')

    def abrir(self):
        self.navegar(URL)
    
    def login(self):
        self.escribir(self.USERNAME_INPUT, USERNAME)
        self.escribir(self.PASSWORD_INPUT, PASSWORD)
        self.click(self.LOGIN_BUTTON)


       # método para login parametrizados
    def login_con_datos(self, usuario, clave):
        self.escribir(self.USERNAME_INPUT, usuario)
        self.escribir(self.PASSWORD_INPUT, clave)
        self.click(self.LOGIN_BUTTON)
    
    #método para obtener mensaje de error
    def obtener_mensaje_error(self):
        return self.obtener_texto(self.ERROR_MESSAGE)


from utils.data_reader import leer_csv_login
import pytest
from pages.login_page import LoginPage

datos = leer_csv_login("data/data_login.csv")

@pytest.mark.parametrize("usuario, clave, debe_funcionar", datos)
def test_login_parametrizado(driver, usuario, clave, debe_funcionar):
    login = LoginPage(driver)
    login.abrir()
    
    login.login_con_datos(usuario, clave)
    
    if debe_funcionar:
        # login exitoso → inventario
        assert "inventory.html" in driver.current_url
    else:
        # login fallido
        assert "inventory.html" not in driver.current_url
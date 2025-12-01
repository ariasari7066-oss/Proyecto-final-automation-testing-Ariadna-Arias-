import pytest
from pages.login_page import LoginPage

class TestLoginNegativo:

    def test_login_credenciales_invalidas(self, driver):
        """Login con credenciales invalidas"""
        login = LoginPage(driver)
        login.abrir()

        login.login_con_datos("usuario_falso", "password_invalido")

        error = login.obtener_mensaje_error()

        assert "Epic sadface" in error

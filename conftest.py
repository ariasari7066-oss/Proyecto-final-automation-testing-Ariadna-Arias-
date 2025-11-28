import pytest
from utils.helpers import get_driver
import os
from datetime import datetime

@pytest.fixture
def driver():
    # configuracion para consultar a selenium web driver
    driver = get_driver()
    yield driver
    driver.quit()



# Carpeta para guardar capturas
os.makedirs("screenshots", exist_ok=True)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Ejecuta el test
    outcome = yield
    result = outcome.get_result()

    # Si el test falla y tiene fixture 'driver'
    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver")
        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshots/{item.name}_{timestamp}.png"
            driver.save_screenshot(filename)
            print(f"\n[SCREENSHOT] Captura guardada en: {filename}")
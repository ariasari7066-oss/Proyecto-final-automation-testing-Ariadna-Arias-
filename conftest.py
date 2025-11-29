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



# Crear ruta absoluta a la carpeta screenshots
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(
                SCREENSHOTS_DIR, f"{item.name}_{timestamp}.png"
            )

            try:
                driver.save_screenshot(filename)
                print(f"\n📸 Screenshot guardado en: {filename}")
            except Exception as e:
                print(f"\n⚠ No se pudo guardar screenshot: {e}")
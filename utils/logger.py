import logging
import os
from datetime import datetime

def get_logger(test_name):
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_dir = os.path.join(base_path, "reports")
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(
        log_dir,
        f"{test_name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    )

    # Crear SIEMPRE un logger nuevo, sin reusar handlers
    logger = logging.getLogger(f"{test_name}_{datetime.now().timestamp()}")
    logger.setLevel(logging.DEBUG)

    # File handler
    fh = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)

    # Consola handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(ch)

    return logger

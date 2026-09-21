from pathlib import Path
import logging

logger = logging.getLogger(__name__)

INVALID_CHARS = '<>:"/\\|?*'

WINDOWS_RESERVED_NAMES = {
    "CON",
    "PRN",
    "AUX",
    "NUL",
    "COM1",
    "COM2",
    "COM3",
    "COM4",
    "COM5",
    "COM6",
    "COM7",
    "COM8",
    "COM9",
    "LPT1",
    "LPT2",
    "LPT3",
    "LPT4",
    "LPT5",
    "LPT6",
    "LPT7",
    "LPT8",
    "LPT9",
}


def validate_num_start(num_start: str, digits: int) -> bool:
    try:
        num_value = int(num_start)
        if 0 <= num_value < 10**digits:
            return True

        msg = f"El valor de inicio {num_start} sale del rango permitido (0-{10**digits - 1})."
        logger.error(msg)
        print(msg)
        return False
        
    except ValueError:
        msg = f"El valor {num_start} no es un número."
        logger.error(msg)
        print(msg)
        return False


def validate_user_path(user_path: Path) -> bool:

    if not user_path.exists():
        msg = f"La ruta especificada ({user_path}) no existe."
        logger.error(msg)
        print(msg)
        return False
            
    if not user_path.is_dir():
        msg = f"{user_path} no es una carpeta."
        logger.error(msg)
        print(msg)
        return False

    if not any(item.is_file() for item in user_path.iterdir()):
        msg = f"La carpeta especificada por el usuario ({user_path}) no tiene archivos."
        logger.error(msg)
        print(msg)
        return False

    return True


def validate_user_name(user_name: str) -> bool:

    if not user_name.strip():
        msg = "El nombre proporcionado está vacío."
        logger.error(msg)
        print(msg)
        return False

    for char in INVALID_CHARS:

        if char in user_name:
            msg = f"El nombre proporcionado por el usuario para renombrar ({user_name}) contiene el carácter invalido {char}"
            logger.error(msg)
            print(msg)
            return False
        
    for reserved_name in WINDOWS_RESERVED_NAMES:

        if reserved_name == user_name.upper():
            msg = f"El nombre proporcionado por el usuario para renombrar ({user_name}) esta reservado por Windows."
            logger.error(msg)
            print(msg)
            return False
        
    return True

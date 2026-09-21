from pathlib import Path
import logging

logger = logging.getLogger(__name__)


def rename_files(
    user_path: Path,
    user_name: str,
    next_num: int,
    digits: int
    ) -> bool:

    count = 0
    logger.info("Renombrando los archivos...")

    try:
        items = list(user_path.iterdir())
    except OSError as e:
        msg = f"No se pudo acceder al directorio {user_path}: {e}"
        logger.error(msg)
        print(msg)
        return False
    
    for item in items:

        if item.is_file():

            if not(0 <= next_num < 10**digits):
                msg = f"Se ha llegado al limite de renombramientos según el rango válido de numeros (0-{10**digits - 1}) ingresados."
                logger.warning(msg)
                print(msg)
                break

            
            str_num = str(next_num).zfill(digits)
            new_name = f"{user_name}_{str_num}{item.suffix}"
            new_path = item.parent / new_name

            try:
                item.rename(new_path)
                msg = f"El archivo {item.name} fue renombrado a {new_name}"
                logger.info(msg)
                print(msg)
                next_num += 1
                count += 1

            except FileExistsError:
                msg = f"""El archivo {item} no puede ser renombrado a {new_path}
debido a que ya existe un archivo con ese nombre."""
                logger.error(msg)
                print(msg)
                return False
    
            except PermissionError:
                msg = f"No se tiene permisos suficientes para renombrar el archivo: {item}."
                logger.error(msg)
                print(msg)
                return False
    
            except OSError as e:
                msg = f"Error del sistema al renombrar el archivo {item}: {e}"
                logger.error(msg)
                print(msg)
                return False


    final_msg = f"{count} archivos han sido renombrados con exito."
    logger.info(final_msg)
    print(final_msg)
    return True

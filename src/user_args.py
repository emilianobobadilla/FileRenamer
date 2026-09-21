import argparse
from pathlib import Path

def parse_user_args() -> argparse.Namespace:

    parser = argparse.ArgumentParser(
        prog="FileRenamer",
        description="Renombra los archivos de una carpeta, especificada por el usuario, con el nombre adjuntado en la terminal."
        )

    parser.add_argument(
        "--folder",
        required=True,
        type=Path,
        help="Carpeta que contiene los archivos que se van a renombrar."
        )
    parser.add_argument(
        "--name",
        required=True,
        help="Nombre base que tendran los archivos renombrados."
        )
    parser.add_argument(
        "--start",
        required=True,
        help="Número inicial de la secuencia de renombrado."
        )
    parser.add_argument(
        "--digits",
        required=True,
        choices=[1, 2, 3, 4, 5],
        type=int,
        help="Cantidad de dígitos utilizados para numerar los archivos."
        )

    return parser.parse_args()

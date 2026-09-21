from user_args import parse_user_args
from validator import (
    validate_num_start,
    validate_user_path,
    validate_user_name
    )
from renamer import rename_files
from pathlib import Path
import sys
import logging

def main():
    LOGS_DIR = Path(__file__).resolve().parent.parent / "logs"
    LOGS_DIR.mkdir(exist_ok=True)
    
    logging.basicConfig(
        filename=LOGS_DIR / "filerenamer.log",
        filemode="a",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
        )
    logger = logging.getLogger(__name__)

    logger.info("=" * 60)
    logger.info("Inicio del programa.")
    logger.info("=" * 60)

    args = parse_user_args()

    user_path = args.folder.resolve()
    if not validate_user_path(user_path):
        sys.exit(1)

    if not validate_user_name(args.name):
        sys.exit(1)

    if not validate_num_start(args.start, args.digits):
        sys.exit(1)

    if not rename_files(user_path, args.name, int(args.start), args.digits):
        sys.exit(1)

    logger.info("Programa terminado.")
    sys.exit(0)
    

if __name__ == "__main__":
    main()


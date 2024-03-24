import argparse
from pathlib import Path
import shutil
import logging

logging.basicConfig(level=logging.INFO)

def parse_argv():
    parser = argparse.ArgumentParser(description="Копіює файли в папку")
    parser.add_argument(
        "source",
        type=Path, 
        help="Шлях де початкова папка з файлами"
    )
    parser.add_argument(
        "dist",
        type=Path,
        nargs="?",
        default=Path("dist"),
        help="Шлях де папка для копіювання (за замовчуванням: 'dist')",
    )
    return parser.parse_args()


def recursive_copy(source: Path, dist: Path):
    for el in source.iterdir():
        try:
            if el.is_dir():
                recursive_copy(el, dist)
            else:
                folder = el.suffix[1:]  # Видаляємо крапку з розширення
                folder_path = dist / folder
                folder_path.mkdir(exist_ok=True, parents=True)
                shutil.copy(el, folder_path)
        except FileNotFoundError as e:
            logging.error(f"File Not Found Error: {e}")
        except PermissionError as e:
            logging.error(f"Permission Denied Error: {e}")

def main():
    args = parse_argv()
    recursive_copy(args.source, args.dist)
    logging.info(f"Файли успішно скопійовані з {args.source} до {args.dist}")

if __name__ == "__main__":
    main()

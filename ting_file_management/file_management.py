import sys


def txt_importer(path_file: str) -> list[str]:
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
        return []
    try:
        with open(path_file) as text_file:
            lines = text_file.read().split("\n")
        return lines
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return []

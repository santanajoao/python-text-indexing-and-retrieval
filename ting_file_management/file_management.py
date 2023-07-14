import sys


def txt_importer(path_file: str) -> list[str]:
    try:
        if not path_file.endswith(".txt"):
            print("Formato inválido", file=sys.stderr)
        else:
            with open(path_file) as text_file:
                content = text_file.read()
            lines = content.split("\n")
            return lines
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)

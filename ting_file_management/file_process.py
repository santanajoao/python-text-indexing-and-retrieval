import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def get_name_from_file(file: dict[str]) -> str:
    return file["nome_do_arquivo"]


def get_file_lines(
        path_file: str, file_processes: Queue) -> None | list[str]:
    file_data = file_processes.find(path_file, key=get_name_from_file)
    if file_data is not None:
        return []

    file_lines = txt_importer(path_file)
    return file_lines


def process(path_file: str, file_processes: Queue) -> None:
    file_lines = get_file_lines(path_file, file_processes)
    if len(file_lines) == 0:
        return None

    file_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines,
    }

    file_processes.enqueue(file_data)
    print(file_data)


def remove(file_processes: Queue) -> None:
    try:
        file_data: dict[str] = file_processes.dequeue()
        print(f"Arquivo {file_data['nome_do_arquivo']} removido com sucesso")
    except IndexError:
        print("Não há elementos")


def file_metadata(file_processes: Queue, position: int) -> None:
    try:
        file_data: dict[str] = file_processes.search(position)
        print(file_data)
    except IndexError:
        print("Posição inválida", file=sys.stderr)

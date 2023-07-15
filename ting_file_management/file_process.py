from .file_management import txt_importer
from .queue import Queue


def get_name_from_process(process: dict[str]) -> str:
    return process["nome_do_arquivo"]


def get_file_lines(
        path_file: str, instance: Queue) -> None | list[str]:
    process = instance.find(path_file, key=get_name_from_process)
    if process is not None:
        return None

    file_lines = txt_importer(path_file)
    if file_lines is None:
        return None

    return file_lines


def process(path_file: str, instance: Queue):
    file_lines = get_file_lines(path_file, instance)
    if file_lines is None:
        return None

    process_data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_lines),
        "linhas_do_arquivo": file_lines,
    }

    instance.enqueue(process_data)
    print(process_data)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""

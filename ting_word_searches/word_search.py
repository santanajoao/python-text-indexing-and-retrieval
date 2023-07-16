from typing import Any
from ting_file_management.queue import Queue


def find_word(word: str, lines: list[str], content: bool = False) -> list[int]:
    occurrences = []
    for index, line in enumerate(lines):
        if word.lower() in line.lower():
            occurrency = {"linha": index + 1}
            if content:
                occurrency["conteudo"] = line
            occurrences.append(occurrency)
    return occurrences


def get_ocurrencies(
    word: str,
    file_queue: Queue[dict[str, Any]],
    content: bool = False
) -> list[dict[str, Any]]:
    result = []
    for file_data in file_queue:
        ocurrences = find_word(word, file_data["linhas_do_arquivo"], content)
        if len(ocurrences) > 0:
            result.append({
                "palavra": word,
                "arquivo": file_data["nome_do_arquivo"],
                "ocorrencias": ocurrences,
            })
    return result


def exists_word(word: str, file_queue: Queue[dict[str, Any]]):
    return get_ocurrencies(word, file_queue)


def search_by_word(word: str, file_queue: Queue[dict[str, Any]]):
    return get_ocurrencies(word, file_queue, content=True)

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
        word: str, instance: Queue, content: bool = False) -> list[dict[str]]:
    result: list[dict[str]] = []
    for file_data in instance:
        ocurrences = find_word(word, file_data["linhas_do_arquivo"], content)
        if len(ocurrences) > 0:
            result.append({
                "palavra": word,
                "arquivo": file_data["nome_do_arquivo"],
                "ocorrencias": ocurrences,
            })
    return result


def exists_word(word, instance):
    return get_ocurrencies(word, instance)


def search_by_word(word, instance):
    return get_ocurrencies(word, instance, content=True)

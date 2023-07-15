def find_word(word: str, lines: list[str]) -> list[int]:
    occurrences = []
    for index, line in enumerate(lines):
        if word.lower() in line.lower():
            occurrences.append({"linha": index + 1})
    return occurrences


def exists_word(word, instance):
    result: list[dict[str]] = []
    for file_data in instance:
        ocurrences = find_word(word, file_data["linhas_do_arquivo"])
        if len(ocurrences) > 0:
            result.append({
                "palavra": word,
                "arquivo": file_data["nome_do_arquivo"],
                "ocorrencias": ocurrences,
            })
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""

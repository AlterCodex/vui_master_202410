def FirstChar(variable_name: str) -> bool:
    if variable_name:
        first_char = variable_name[0]
        return first_char.isalpha() or first_char == '_'
    return False


def _is_vocal(x: str) -> bool:
    return x in 'AEIOUaeiou'


def porcentVocal(word: str) -> float:
    if word:
        length = len(word)
        vocal_counts = len([x for x in word if _is_vocal(x)])
        return round((vocal_counts * 100) / length, 1)
    return 0.0


def nuevo_string(word: str, char_repeat: int) -> str:
    new_word = ''
    if word:
        for x in word:
            new_word += x * char_repeat if _is_vocal(x) else x
    return new_word


def notas_al_pie(notas: str) -> str:
    notes = ''
    i = 1
    for x in notas:
        if x != '*':
            notes += x
        else:
            notes += '(' + str(i) + ')'
            i += 1
    return notes


def codigo(nombre: str) -> str:
    code = ''
    if nombre:
        return ''.join(x[0] for x in nombre.split(' ')) + str(len(nombre.replace(' ', '')))
    return code


def contar_hidrogenos(compuesto: str) -> int:
    hidrogenos = 0
    for i in range(0, len(compuesto) - 1):
        if compuesto[i] == 'H':
            if compuesto[i + 1].isdigit():
                hidrogenos += int(compuesto[i + 1])
            else:
                hidrogenos += 1
    if compuesto[-1] == 'H':
        hidrogenos += 1
    return hidrogenos


def mediaTempRang(temps: list) -> float | int:
    valid_temps = [x for x in temps if 15 <= x <= 45]
    if not valid_temps:
        return -1
    median = float(sum(valid_temps)) / float(len(valid_temps))
    return round(median, 2)

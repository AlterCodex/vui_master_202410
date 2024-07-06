from math import log10, sqrt
from typing import List, Any


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


def SPL_dB(P):
    """ Calcula Sound Pressure Level en dB: 20log(x/20) x en microPascales
    """
    return 20 * log10(P / 20)


def detect2ndNdB(lst: list, N: float) -> int:
    upper_sounds_in_db = [x for x in lst if SPL_dB(x) >= N]
    if len(upper_sounds_in_db) < 2:
        return -1
    return upper_sounds_in_db[1]


def es_primo(n):
    if n <= 1: return False
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True


def primoPitagoric2(lst: list) -> int | list[int]:
    pitagoric_primes = [x for x in lst if x % 4 == 1 and es_primo(x)]
    if len(pitagoric_primes) < 2:
        return -1
    return pitagoric_primes[0:2]


def contar_pos(m: list[list]) -> int:
    positives = 0
    for row in m:
        for i in row:
            if i > 0:
                positives += 1
    return positives


def mas_denso(planetas: list)-> str :
    max_density=00.0
    most_dense_planet=""
    for planet in planetas:
        d = float(planet[1])/float(planet[2])
        if d > max_density:
            max_density=d
            most_dense_planet = planet[0]
    return  most_dense_planet


class Jugador():

    def __init__(self, *args):
        self.number = args[0]
        self.name = args[1]
        self.community = args[2]
        self.age = args[3]
        self.distance = args[4:]

    def is_community(self):
        return self.community

    def median_distance(self):
        return float(sum(self.distance))/float(len(self.distance))

    def is_valid(self,minimun_distance):
        return  self.is_community() and self.median_distance() > minimun_distance

def jugComKm(lst:list[list], x:float)->list[str]:
    jugadores = []
    for i in lst:
        jugadores.append(Jugador(*i))
    jugadores_validos = [jugador.name for jugador in jugadores if jugador.is_valid(x)]
    jugadores_validos.sort()
    return jugadores_validos
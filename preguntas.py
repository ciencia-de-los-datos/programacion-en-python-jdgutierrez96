"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.
"""

import csv

data = []
with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = '\t')
    for row in csv_reader:
        data.append(row)

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    sum = 0
    for row in data:
        sum += int(row[1])
    return sum


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    first_column = [row[0] for row in data]
    unique_letters = list(set(first_column))
    unique_letters.sort()
    letter_counts = []
    for letter in unique_letters:
        letter_counts.append((letter, first_column.count(letter)))
    return letter_counts


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    first_column = [row[0] for row in data]
    unique_letters = list(set(first_column))
    unique_letters.sort()
    letter_sums = []
    sums = [0 for letter in unique_letters]
    for index, letter in enumerate(unique_letters):
        for row in data:
            if row[0] == letter:
                sums[index] += int(row[1])
        letter_sums.append((letter, sums[index]))
    return letter_sums


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    months = [row[2].split('-')[1] for row in data]
    unique_months = list(set(months))
    unique_months.sort()
    month_counts = []
    for motnth in unique_months:
        month_counts.append((motnth, months.count(motnth)))
    return month_counts


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    first_column = [row[0] for row in data]
    unique_letters = list(set(first_column))
    unique_letters.sort()
    letter_max_min = []
    maxs = [float('-inf') for letter in unique_letters]
    mins = [float('inf') for letter in unique_letters]
    for index, letter in enumerate(unique_letters):
        for row in data:
            if row[0] == letter:
                row_value = int(row[1])
                if row_value < mins[index]:
                    mins[index] = row_value
                if row_value > maxs[index]:
                    maxs[index] = row_value
        letter_max_min.append((letter, maxs[index], mins[index]))
    return letter_max_min


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    fifth_column = [row[4].split(',') for row in data]
    fifth_column_flattened = [row.split(':') for row in sum(fifth_column, [])]
    keys = [row[0] for row in fifth_column_flattened]
    unique_keys = list(set(keys))
    unique_keys.sort()
    key_min_max = []
    mins = [float('inf') for key in unique_keys]
    maxs = [float('-inf') for key in unique_keys]
    for index, key in enumerate(unique_keys):
        for row in fifth_column_flattened:
            if row[0] == key:
                row_value = int(row[1])
                if row_value < mins[index]:
                    mins[index] = row_value
                if row_value > maxs[index]:
                    maxs[index] = row_value
        key_min_max.append((key, mins[index], maxs[index]))
    return key_min_max


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    values = [int(row[1]) for row in data]
    unique_values = list(set(values))
    unique_values.sort()
    value_letters = []
    letters = [[] for value in unique_values]
    for index, value in enumerate(unique_values):
        for row in data:
            if int(row[1]) == value:
                letters[index].append(row[0])
        value_letters.append((value, letters[index]))
    return value_letters


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    values = [int(row[1]) for row in data]
    unique_values = list(set(values))
    unique_values.sort()
    value_letters = []
    letters = [[] for value in unique_values]
    for index, value in enumerate(unique_values):
        for row in data:
            if int(row[1]) == value:
                letters[index].append(row[0])
        unique_letters = list(set(letters[index]))
        unique_letters.sort()
        value_letters.append((value, unique_letters))
    return value_letters


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    fifth_column = [row[4].split(',') for row in data]
    fifth_column_flattened = [row.split(':') for row in sum(fifth_column, [])]
    keys = [row[0] for row in fifth_column_flattened]
    unique_keys = list(set(keys))
    unique_keys.sort()
    key_counts = {}
    for key in unique_keys:
        key_counts[key] = keys.count(key)
    return key_counts


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    letter_lens = [(row[0], len(row[3].split(',')), len(row[4].split(','))) for row in data]
    return letter_lens


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    fourth_second_column_flattened = []
    for row in data:
        for letter in row[3].split(','):
            fourth_second_column_flattened.append([letter, int(row[1])])
    unique_letters = list(set([row[0] for row in fourth_second_column_flattened]))
    unique_letters.sort()
    letter_sums = {}
    sums = [0 for letter in unique_letters]
    for index, letter in enumerate(unique_letters):
        for row in fourth_second_column_flattened:
            if row[0] == letter:
                sums[index] += row[1]
        letter_sums[letter] = sums[index]
    return letter_sums


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    first_fifth_column = [[row[0], row[4].split(',')] for row in data]
    letters_values = []
    for row in first_fifth_column:
        for value in row[1]:
            letters_values.append([row[0], value.split(':')[1]])
    unique_letters = list(set([row[0] for row in letters_values]))
    unique_letters.sort()
    letter_sums = {}
    sums = [0 for letter in unique_letters]
    for index, letter in enumerate(unique_letters):
        for row in letters_values:
            if row[0] == letter:
                sums[index] += int(row[1])
        letter_sums[letter] = sums[index]
    return letter_sums
def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)


def fix_bolivian_birthday(birthday: str) -> str:
    birthday = birthday.replace(".", '-')
    birthday = birthday.replace("/", '-')
    birthday = birthday.replace(",", '')
    birthday = birthday.lower()
    months = {
        '01': 'enero',
        '02': 'febrero',
        '03': 'marzo',
        '04': 'abril',
        '05': 'mayo',
        '06': 'junio',
        '07': 'julio',
        '08': 'agosto',
        '09': 'septiembre',
        '10': 'octubre',
        '11': 'noviembre',
        '12': 'diciembre',
    }
    for month in months:
        birthday = birthday.replace(months[month], month)
    birthday = birthday.replace("del", '-')
    birthday = birthday.replace("de", '-')
    birthday = birthday.replace(" ", '')
    new_birthday = ''.join(char for char in birthday if char in '1234567890-')
    if '-' not in new_birthday:
        # adicionamos una coma cada 2, reemplazamos las comas por - 2 veces y borramos el resto
        t = iter(new_birthday)
        new_birthday = ','.join(a + b for a, b in zip(t, t))
        new_birthday = new_birthday.replace(',', '-', 2)
        new_birthday = new_birthday.replace(',', '', )
    # convirtiendo a formato DD/MM/YYYY
    new_birthday = new_birthday.replace("-", '/')
    # para el caso 12/12/66
    if len(new_birthday) == 8 and new_birthday[1].isdigit():
        new_birthday = rreplace(new_birthday, '/', '/19', 1)
    return new_birthday

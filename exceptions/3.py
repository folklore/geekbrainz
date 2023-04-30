from datetime import datetime

GREATING_TEXT = '''Введите набор данных "Фамилию Имя Отчество ДатуРождения НомерТелефона Пол"

Форматы данных:
Фамилия, Имя, Отчество - строки;
ДатаРождения - строка формата dd.mm.yyyy;
НомерТелефона - целое беззнаковое число без форматирования;
Пол - символ латиницей f или m.

Или введите "exit" для выхода.

'''

class NotEnoughParameters(AssertionError):
  pass

class OvermuchParameters(AssertionError):
  pass

PARAMS_COUNT = 6

BIRTHDAY_FORMAT = "%d.%m.%Y"

SEX_TYPES = ['f', 'm']


while True:
  payload = input(GREATING_TEXT)

  if payload == 'exit':
    break

  try:
    data = payload.split(' ')

    if len(data) < PARAMS_COUNT:
      raise NotEnoughParameters(f"{len(data)} из {PARAMS_COUNT}")
    elif len(data) > PARAMS_COUNT:
      raise OvermuchParameters(f"{len(data)} из {PARAMS_COUNT}")

    surname, name, patronymic, birthday, phone_number, sex = data

    try:
      datetime.strptime(birthday, BIRTHDAY_FORMAT)
    except ValueError:
      raise ValueError(f'\n>>> Дата рождения указана неверно. Допустимый формат {BIRTHDAY_FORMAT} <<<\n')

    if not phone_number.isdigit():
      raise ValueError(f'\n>>> Номер телефона указан неверно. Допустимы только цифры <<<\n')      

    if sex not in SEX_TYPES:
      raise ValueError(f'\n>>> Пол указан неверно. Допустимы {SEX_TYPES} <<<\n')

    line = ''.join(f"<{param}>" for param in data)

    with open(surname, 'a') as file:
      file.write("{}\n".format(line))

  except NotEnoughParameters as err:
    print(f"\n>>> Введено недостаточно данных, {err}. Введите необходимый набор <<<\n")
  except OvermuchParameters as err:
    print(f"\n>>> Введено избыточно данных, {err}. Введите необходимый набор <<<\n")
  except ValueError as err:
    print(f"{err}")
  except Exception as err:
    print(f"\n>>> Непредвиденная ошибка {err}, {type(err)}. До свидания <<<\n")

    raise

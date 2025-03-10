class IncorrectVinNumber(Exception):  # класс исключений
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class IncorrectCarNumbers(Exception):  # класс исключений
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):  # проверяет корректность vin
        if isinstance(vin_number, int) == False:  # если передано не целое число.
            raise IncorrectVinNumber('Некорректный тип для vin номер')
        if not (1000000 <= vin_number <= 9999999):  # если переданное число находится не в диапазоне
            raise IncorrectVinNumber('Некорректный диапазон vin номер')
        return True  # если исключения не были выброшены

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str) == False:  # если передана не строка.
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True  # если исключения не были выброшены


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

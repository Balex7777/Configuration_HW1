# Домашняя работа №1 - Эмулятор для языка оболочки ОС
### Постановка задачи

Разработать эмулятор для языка оболочки ОС. Необходимо сделать работу
эмулятора как можно более похожей на сеанс shell в UNIX-подобной ОС.
Эмулятор должен запускаться из реальной командной строки, а файл с
виртуальной файловой системой не нужно распаковывать у пользователя.
Эмулятор принимает образ виртуальной файловой системы в виде файла формата
tar. Эмулятор должен работать в режиме CLI.

Конфигурационный файл имеет формат json и содержит:
- Имя компьютера для показа в приглашении к вводу.
- Путь к архиву виртуальной файловой системы.
- Путь к стартовому скрипту.

Стартовый скрипт служит для начального выполнения заданного списка
команд из файла.

Необходимо поддержать в эмуляторе команды ls, cd и exit, а также
следующие команды:
1. uptime.
2. uname.

Все функции эмулятора должны быть покрыты тестами, а для каждой из
поддерживаемых команд необходимо написать 3 теста.

### Запуск программы
```bash
python start_emulator.py
```

### Запуск тестов

```bash
pip install pytest
pytest test
```
### Результаты тестов
![Tests](https://github.com/Balex7777/Configuration_HW1/raw/master/images/tests.png)

### Скрины работы программы
- Комманда ``ls``

![Tests](https://github.com/Balex7777/Configuration_HW1/raw/master/images/ls.png)

- Комманда ``cd``

![Tests](https://github.com/Balex7777/Configuration_HW1/raw/master/images/cd.png)

- Комманда ``uname``

![Tests](https://github.com/Balex7777/Configuration_HW1/raw/master/images/uname.png)

- Комманда ``uptime``

![Tests](https://github.com/Balex7777/Configuration_HW1/raw/master/images/uptime.png)

- Комманда ``exit``

![Tests](https://github.com/Balex7777/Configuration_HW1/raw/master/images/exit.png)

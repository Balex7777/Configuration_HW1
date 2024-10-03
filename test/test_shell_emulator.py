import pytest
import os
import time
import platform

from start_emulator import ShellEmulator, run_command  # Импортируем ваш модуль


@pytest.fixture
def shell():
    # Создаем временную директорию для тестирования
    root_dir = "/tmp/test_virtual_fs"
    os.makedirs(root_dir, exist_ok=True)
    return ShellEmulator(hostname="testhost", root_dir=root_dir)


def test_ls(shell):
    # Создаем несколько файлов в директории
    open(os.path.join(shell.current_dir, 'file1.txt'), 'w').close()
    open(os.path.join(shell.current_dir, 'file2.txt'), 'w').close()

    # Получаем список файлов и директории, которые должны быть в каталоге
    expected_files = ['file1.txt', 'file2.txt', 'testdir']

    # Проверяем, что ls возвращает список файлов и директорий
    assert sorted(shell.ls()) == sorted(expected_files)

    # Проверка на пустую директорию
    os.remove(os.path.join(shell.current_dir, 'file1.txt'))
    os.remove(os.path.join(shell.current_dir, 'file2.txt'))
    assert shell.ls() == ['testdir']



def test_cd(shell):
    # Создаем тестовые директории
    os.makedirs(os.path.join(shell.current_dir, 'testdir'), exist_ok=True)

    # Проверяем смену директории
    shell.cd('testdir')
    assert shell.current_dir.endswith('testdir')

    # Проверка возврата в родительскую директорию
    shell.cd('..')
    assert shell.current_dir == '/tmp/test_virtual_fs'

    # Проверка перехода в несуществующую директорию
    shell.cd('non_existent')
    assert shell.current_dir == '/tmp/test_virtual_fs'  # Директория не должна измениться


def test_uptime(shell):
    time.sleep(0.1)
    # Проверяем, что uptime возвращает значение больше нуля
    assert shell.uptime() > 0

    # Имитация длительного ожидания
    time.sleep(1)
    assert shell.uptime() > 1  # Время должно увеличиваться


def test_uname(shell):
    # Проверяем, что uname возвращает имя операционной системы
    assert shell.uname() == platform.system()


def test_prompt(shell):
    # Проверяем правильность отображения prompt
    assert shell.prompt() == "testhost:/tmp/test_virtual_fs$ "

